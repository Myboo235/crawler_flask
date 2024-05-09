import "./assets/main.css";

import router from "./router";
import { createApp } from "vue";
import App from "./App.vue";

import { OhVueIcon, addIcons } from "oh-vue-icons";
import * as FaIcons from "oh-vue-icons/icons/fa";
import * as OiIcons from "oh-vue-icons/icons/oi";
import * as BiIcons from "oh-vue-icons/icons/bi";

import { MotionPlugin } from "@vueuse/motion";

import VueKinesis from "vue-kinesis";

const Fa = Object.values({ ...FaIcons });
const Oi = Object.values({ ...OiIcons });
const Bi = Object.values({ ...BiIcons });

addIcons(...Fa);
addIcons(...Oi);
addIcons(...Bi);

const app = createApp(App);

app.use(VueKinesis);
app.use(MotionPlugin);
app.use(router);

app.component("v-icon", OhVueIcon);
app.mount("#app");
