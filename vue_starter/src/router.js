import { createWebHistory, createRouter } from "vue-router";

import MainPage from "./pages/MainPage.vue";
import ArticlePage from "./pages/ArticlePage.vue";
import GamePage from "./pages/GamePage.vue";

const routes = [
  { path: "/", redirect: "/mainpage" },
  { path: "/mainpage", component: MainPage },
  { path: "/article", component: ArticlePage },
  { path: "/game", component: GamePage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
