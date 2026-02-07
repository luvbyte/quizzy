import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: Home, name: "home" },
    {
      path: "/quiz/:name",
      component: () => import("../views/Quiz.vue"),
      name: "quiz"
    },
    {
      path: "/404",
      component: () => import("../views/404.vue"),
      name: "404"
    }
  ]
});

export default router;
