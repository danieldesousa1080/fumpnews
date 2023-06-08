import router from './routes'
import App from './App.vue'
import { createApp } from 'vue'

const app = createApp(App);
app.use(router);
app.mount('#app');