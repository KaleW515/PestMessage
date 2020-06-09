import Vue from 'vue';
import './plugins/axios';
import App from './App.vue';
import router from './router';
import store from './store';
import './plugins/element.js';
// import './plugins/love';
import './plugins/maodian'

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://127.0.0.1:8000';
axios.defaults.withCredentials = true;
new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app');


axios.interceptors.request.use(
    config => {
        if (localStorage.getItem('X-CSRF-Token')) {
            config.headers = {
                'X-CSRFToken': localStorage.getItem('X-CSRF-Token'),
            };
            if (localStorage.getItem('Authorization')) {
                config.headers.Authorization = localStorage.getItem('Authorization');
            }

        }

        return config;
    },
    error => {
        return Promise.reject(error);
    });
