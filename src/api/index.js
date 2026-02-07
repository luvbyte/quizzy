export async function fetchQuiz(name) {
  try {
    const res = await fetch(`/data/quizzes/${name}.json`);

    if (!res.ok) {
      throw new Error(`Failed to load quiz: ${name}`);
    }

    const data = await res.json();
    return data;
  } catch (err) {
    console.error("Error fetching quiz:", err);
    throw err;
  }
}

export async function fetchQuizsList() {
  try {
    const res = await fetch(`/data/index.json`);

    if (!res.ok) {
      throw new Error(`Failed to load`);
    }

    const data = await res.json();
    return data;
  } catch (err) {
    console.error("Error fetching quizzes list:", err);
    throw err;
  }
}

export function quizComplete(name, score, percentage) {
  const result = {
    name,
    score,
    percentage,
    completedAt: new Date().toISOString()
  };

  // Save to session storage
  sessionStorage.setItem(`quiz-${name}`, JSON.stringify(result));
}

export function getQuizResult(name) {
  const stored = sessionStorage.getItem(`quiz-${name}`);

  return stored ? JSON.parse(stored) : null;
}

export function quizCompleted(name) {
  return !!getQuizResult(name);
}
