import { createWebHistory, createRouter } from "vue-router";

import MainPage from "./pages/MainPage.vue";
import ArticlePage from "./pages/ArticlePage.vue";
import GamePage from "./pages/GamePage.vue";
import CreateArticlePage from "./pages/CreateArticlePage.vue"
import UpdateArticlePage from "./pages/UpdateArticlePage.vue"


const routes = [
  { path: "/", redirect: "/mainpage" },
  { path: "/mainpage", component: MainPage },
  { path: "/article/:id", component: ArticlePage },
  { path: "/game", component: GamePage },
  { path: "/create", component: CreateArticlePage },
  { path: "/update/:id", component: UpdateArticlePage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
