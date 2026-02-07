<template>
  <div class="flex-1 flex items-center justify-center bg-base-200 p-6">
    <div class="text-center max-w-md">
      <h1 class="text-8xl font-extrabold text-primary">404</h1>

      <p class="mt-4 text-2xl font-semibold">Page Not Found</p>

      <p class="mt-2 opacity-70">
        Oops… the page you’re looking for doesn’t exist.
      </p>

      <RouterLink to="/" class="btn btn-primary mt-6">
        Back to Home
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
  import { RouterLink } from "vue-router";
</script>
