# Simple automation script to add quizzes to data

from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator

import json

from pathlib import Path


def parse_file(filepath):
  with open(filepath, "r", encoding="utf-8") as file:
    return json.load(file)


DATA_PATH = Path("../public/data").resolve()
INDEX_PATH = DATA_PATH / "index.json"

QUIZZES = parse_file(INDEX_PATH)

class Question(BaseModel):
  id: int
  question: str
  options: List[str]
  answer: str
  explanation: str

  @model_validator(mode="after")
  def validate_answer_in_options(self):
    if self.answer not in self.options:
      raise ValueError("Answer must be one of the options")
    return self

class QuizSection(BaseModel):
  section: str
  type: str
  questions: List[Question]

class QuizFile(BaseModel):
  title: str
  total_sections: int
  quizzes: List[QuizSection]
  slug: str
  level: str

  @model_validator(mode="after")
  def validate_sections_count(self):
    if self.total_sections != len(self.quizzes):
      raise ValueError("total_sections does not match number of quizzes")
    return self

def validate_quiz_file(file_path: str):
  try:
    with open(file_path, "r", encoding="utf-8") as f:
      data = json.load(f)

    quiz = QuizFile.model_validate(data)
    
    return quiz

  except ValidationError as e:
    raise ValueError(f"Schema validation failed:\n{e}")
  except Exception as e:
    raise ValueError(f"Invalid file: {e}")

print("Validating quiz...\n")
quiz = validate_quiz_file("quiz.json")

print("-" * 5)
print("Title: ", quiz.title)
print("Slug: ", quiz.slug)
print("Sections: ", quiz.total_sections)
print("-" * 5)

input("\nPress enter to proceed!\n")

# username checks
def create_filepath(name):
  temp_name = name
  while True:
    filepath = DATA_PATH / "quizzes" / f"{temp_name}.json"
  
    if not filepath.exists():
      return filepath, temp_name
    
    print(f"Filename: ({temp_name}.json) already exists")
    
    temp_name = input("Enter new name: ")

# filepath
filepath, filename = create_filepath(quiz.slug)

# Create in /data/quizzes/
with open(filepath, "w", encoding="utf-8") as file:
  json.dump(
    quiz.model_dump(exclude={"slug", "level"}),
    file,
    indent=2,
    ensure_ascii=False
  )

QUIZZES.insert(0, {
  "name": filename,
  "title": quiz.title,
  "sections": quiz.total_sections,
  "level": quiz.level
})

with open(INDEX_PATH, "w", encoding="utf-8") as file:
  json.dump(QUIZZES, file, indent=2)

print("Saved:", filename)
