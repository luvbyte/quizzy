<template>
  <div class="navbar flex justify-between px-2">
    <button @click="goHome" class="flex items-center gap-1">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="M17 7H9q-.425 0-.712-.288T8 6t.288-.712T9 5h9q.425 0 .713.288T19 6v9q0 .425-.288.713T18 16t-.712-.288T17 15zm-5 5H4q-.425 0-.712-.288T3 11t.288-.712T4 10h9q.425 0 .713.288T14 11v9q0 .425-.288.713T13 21t-.712-.288T12 20z"
        />
      </svg>
      <h1 class="text-lg font-semibold">Quizzy</h1>
    </button>
    <button @click="() => (showSidebar = true)" class="flex items-center gap-1">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="m2.53 19.65l1.34.56v-9.03l-2.43 5.86c-.41 1.02.08 2.19 1.09 2.61m19.5-3.7L17.07 3.98a2.01 2.01 0 0 0-1.81-1.23c-.26 0-.53.04-.79.15L7.1 5.95a2 2 0 0 0-1.08 2.6l4.96 11.97a2 2 0 0 0 2.6 1.08l7.36-3.05a1.994 1.994 0 0 0 1.09-2.6m-9.2 3.8L7.87 7.79l7.35-3.04h.01l4.95 11.95z"
        />
        <circle cx="11" cy="9" r="1" fill="currentColor" />
        <path
          fill="currentColor"
          d="M5.88 19.75c0 1.1.9 2 2 2h1.45l-3.45-8.34z"
        />
      </svg>
      <h1 class="text-lg font-semibold">Themes</h1>
    </button>
    <Transition name="slide-right">
      <Sidebar v-show="showSidebar" :close="() => (showSidebar = false)" />
    </Transition>
  </div>
</template>

<script setup>
  import { ref } from "vue";

  import Sidebar from "@/components/Sidebar.vue";

  import { useRouter } from "vue-router";

  const router = useRouter();

  const showSidebar = ref(false);

  function goHome() {
    router.push({ name: "home" });
  }
</script>
