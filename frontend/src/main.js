import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';

// Configure axios to include CSRF token
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// Create and mount the Vue application
const app = createApp(App);
app.mount('#app');