<script setup>
  import Navbar from "@/components/Navbar.vue"
</script>

<template>
  <div id="main" class="h-dvh flex flex-col font-body overflow-hidden">
    <Navbar />
    <div class="flex-1 flex flex-col overflow-hidden">
      <router-view />
    </div>
  </div>
</template>

<style scoped></style>
