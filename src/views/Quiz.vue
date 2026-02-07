<template>
  <!-- Loading -->
  <div v-if="!quiz" class="flex-1">
    <Loading />
  </div>

  <!-- Quiz Already Completed -->
  <div v-else-if="quizFinished" class="flex-1 bg-base-200 p-6 overflow-y-auto">
    <div class="max-w-3xl mx-auto text-center mt-10">
      <h2 class="text-2xl font-bold">🎉 Quiz Completed!</h2>

      <div class="mt-4 text-lg font-semibold">
        Your Score: {{ storedResult.score }} / {{ totalQuestions }}
      </div>

      <p class="mt-1">Accuracy: {{ storedResult.percentage }}%</p>

      <!-- Buttons -->
      <div class="flex justify-center gap-2 mt-6">
        <button class="btn btn-primary" @click="retakeQuiz">Retake Quiz</button>
        <button class="btn btn-outline" @click="goHome">Home</button>
      </div>
    </div>
  </div>
  <!-- Normal Quiz Flow -->
  <div
    v-else
    ref="scrollContainer"
    class="flex-1 bg-base-200 p-4 overflow-y-auto"
  >
    <!-- Header -->
    <div class="max-w-3xl mx-auto mb-6">
      <div class="card bg-primary text-primary-content shadow-lg">
        <div class="card-body text-center">
          <h1 class="text-2xl font-bold font-heading">
            {{ quiz.title }}
          </h1>
          <p>
            Section {{ currentSectionIndex + 1 }} of
            {{ quiz.total_sections }}
          </p>
        </div>
      </div>
    </div>

    <!-- CURRENT SECTION ONLY -->
    <div v-if="currentSection" class="max-w-3xl mx-auto mb-6">
      <div class="card bg-base-100 shadow-md">
        <!-- Section Header -->
        <div class="card-body border-b bg-base-100 px-6 py-4 text-center">
          <h1 class="text-xl font-bold tracking-tight text-base-content">
            {{ currentSection.section }}
          </h1>

          <div class="flex justify-center">
            <span
              class="badge badge-primary px-4 py-3 text-sm font-medium uppercase tracking-wide"
            >
              {{ currentSection.type }}
            </span>
          </div>
        </div>

        <!-- Questions -->
        <div
          v-for="question in currentSection.questions"
          :key="question.id"
          class="card-body border-t gap-4"
        >
          <p class="font-medium">Q{{ question.id }}. {{ question.question }}</p>

          <!-- Options -->
          <div class="grid grid-cols-1 gap-2">
            <button
              v-for="opt in question.options"
              :key="opt"
              class="btn btn-outline justify-start text-left"
              :class="getOptionClass(question.id, opt, question.answer)"
              @click="selectOption(question.id, opt)"
            >
              {{ opt }}
            </button>
          </div>

          <!-- Explanation -->
          <div
            v-if="answers[question.id]"
            :ref="el => (explanationRefs[question.id] = el)"
            class="alert mt-2"
            :class="
              answers[question.id] === question.answer
                ? 'alert-success'
                : 'alert-error'
            "
          >
            <div>
              <p class="font-semibold">Correct Answer: {{ question.answer }}</p>
              <p class="text-sm mt-1">
                {{ question.explanation }}
              </p>
            </div>
          </div>
        </div>

        <!-- NEXT BUTTON -->
        <div class="card-body border-t text-center">
          <button
            class="btn btn-primary"
            :disabled="!isSectionCompleted(currentSection)"
            @click="nextSection"
          >
            {{
              currentSectionIndex === quiz.quizzes.length - 1
                ? "Finish Quiz"
                : "Next Section"
            }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
  import { reactive, ref, computed, onBeforeMount, watch, nextTick } from "vue";
  import { useRoute, useRouter } from "vue-router";

  import Loading from "@/components/Loading.vue";

  import { fetchQuiz, quizComplete, getQuizResult } from "@/api";

  const route = useRoute();
  const router = useRouter();

  // Refs

  const quiz = ref(null);
  const storedResult = ref(null);

  const answers = reactive({});
  const currentSectionIndex = ref(0);

  const scrollContainer = ref(null);
  const explanationRefs = reactive({});

  // Computed

  const currentSection = computed(() => {
    return quiz.value.quizzes[currentSectionIndex.value];
  });

  const quizFinished = computed(() => {
    return !!storedResult.value;
  });

  const score = computed(() => {
    let correct = 0;

    quiz.value.quizzes.forEach(section => {
      section.questions.forEach(q => {
        if (answers[q.id] === q.answer) {
          correct++;
        }
      });
    });

    return correct;
  });

  const percentage = computed(() => {
    return Math.round((score.value / totalQuestions.value) * 100);
  });

  const totalQuestions = computed(() => {
    return quiz.value.quizzes.reduce(
      (sum, section) => sum + section.questions.length,
      0
    );
  });

  // Methods

  async function selectOption(qid, option) {
    if (!answers[qid]) {
      answers[qid] = option;

      await nextTick();

      const el = explanationRefs[qid];

      if (el && scrollContainer.value) {
        el.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });

        scrollContainer.value.scrollBy({
          top: 120,
          behavior: "smooth"
        });
      }
    }
  }

  function nextSection() {
    if (currentSectionIndex.value < quiz.value.quizzes.length - 1) {
      currentSectionIndex.value++;
    } else {
      quizComplete(route.params.name, score.value, percentage.value);

      storedResult.value = {
        name: route.params.name,
        score: score.value,
        percentage: percentage.value,
        completedAt: new Date().toISOString()
      };
    }
  }

  function retakeQuiz() {
    sessionStorage.removeItem(`quiz-${route.params.name}`);

    storedResult.value = null;

    Object.keys(answers).forEach(k => delete answers[k]);

    currentSectionIndex.value = 0;
  }

  function isSectionCompleted(section) {
    return section.questions.every(q => answers[q.id]);
  }

  function getOptionClass(id, opt, correct) {
    if (!answers[id]) return "";

    if (opt === correct) return "btn-success";

    if (answers[id] === opt && opt !== correct) return "btn-error";

    return "btn-outline";
  }

  function goHome() {
    router.push({ name: "home" });
  }

  watch(currentSectionIndex, async () => {
    await nextTick();

    if (scrollContainer.value) {
      scrollContainer.value.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    }
  });

  onBeforeMount(async () => {
    try {
      quiz.value = await fetchQuiz(route.params.name);

      // check session result
      storedResult.value = getQuizResult(route.params.name);
    } catch (err) {
      // Redirect 404
      router.push({ name: "404" });
    }
  });
</script>
