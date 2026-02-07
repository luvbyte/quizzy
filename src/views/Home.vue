<template>
  <div v-if="!quizes" class="flex-1">
    <Loading />
  </div>

  <div v-else class="flex-1 overflow-y-auto bg-base-200 p-6">
    <div class="max-w-5xl mx-auto">
      <!-- Header -->
      <h1 class="text-3xl font-bold mb-4 text-center font-heading">
        Available Quizzes
      </h1>

      <!-- Search -->
      <div class="mb-6 flex justify-center">
        <input
          v-model="search"
          type="text"
          placeholder="Search quizzes..."
          class="input input-bordered w-full max-w-md placeholder:opacity-60"
        />
      </div>

      <!-- Quiz Grid -->
      <div
        v-if="filteredQuizes.length"
        class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3 gap-6"
      >
        <div
          v-for="quiz in filteredQuizes"
          :key="quiz.name"
          class="card bg-base-100 shadow-xl relative h-full"
        >
          <!-- Completed Badge -->
          <span
            v-if="quizCompleted(quiz.name)"
            class="p-2 bg-success text-success-content shadow-lg rounded-b absolute top-0 right-4 z-10"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
            >
              <g fill="none">
                <circle
                  cx="12"
                  cy="12"
                  r="8"
                  fill="currentColor"
                  fill-opacity="0.25"
                />
                <path
                  stroke="currentColor"
                  stroke-width="1.2"
                  d="m8.5 11l2.894 2.894a.15.15 0 0 0 .212 0L19.5 6"
                />
              </g>
            </svg>
          </span>

          <!-- Card Body -->
          <div class="card-body items-center text-center flex flex-col h-full">
            <!-- Optional Image -->
            <div
              v-if="quiz.image"
              class="w-20 h-20 rounded-xl overflow-hidden bg-base-300"
            >
              <img
                :src="quiz.image"
                :alt="quiz.title"
                class="w-full h-full object-cover"
              />
            </div>

            <h2 class="card-title">{{ quiz.title }}</h2>

            <div class="flex gap-2 flex-wrap justify-center">
              <span class="badge badge-primary">
                {{ quiz.level }}
              </span>

              <span class="badge badge-secondary">
                {{ quiz.sections }} Sections
              </span>
            </div>

            <!-- Button pinned at bottom -->
            <div class="card-actions justify-end pt-2 mt-auto w-full">
              <RouterLink
                :to="`/quiz/${quiz.name}`"
                class="btn btn-primary btn-sm w-full"
                :class="{
                  'btn-outline': quizCompleted(quiz.name)
                }"
              >
                {{ quizCompleted(quiz.name) ? "View Result" : "Start Quiz" }}
              </RouterLink>
            </div>
          </div>
        </div>
      </div>

      <!-- No Results -->
      <p v-else class="text-center opacity-70 mt-10">No quizzes found 😕</p>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onBeforeMount } from "vue";
  import { RouterLink } from "vue-router";

  import Loading from "@/components/Loading.vue";

  import { fetchQuizsList, quizCompleted } from "@/api";

  // Refs
  const search = ref("");
  const quizes = ref(null);

  // Filter / Search
  const filteredQuizes = computed(() => {
    if (!search.value) return quizes.value;

    const term = search.value.toLowerCase();

    return quizes.value.filter(
      q =>
        q.title.toLowerCase().includes(term) ||
        q.level.toLowerCase().includes(term) ||
        q.name.toLowerCase().includes(term)
    );
  });

  // Lifecycle
  onBeforeMount(async () => {
    try {
      quizes.value = await fetchQuizsList();
    } catch (err) {
      console.error("Failed to load quizzes", err);
    }
  });
</script>
