import router from './routes'
import App from './App.vue'
import { createApp } from 'vue'
import PhosphorIcons from "@phosphor-icons/vue"

const app = createApp(App);
app.use(router);
app.use(PhosphorIcons);
app.mount('#app');