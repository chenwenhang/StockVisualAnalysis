import { createApp } from 'vue'
import ElementPlus from 'element-plus';
import App from './App.vue'

import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";
axios.defaults.withCredentials = false;

const app = createApp(App)
app.config.globalProperties.$axios = axios;
app.use(ElementPlus)
app.mount('#app')