import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({

    state: {
        Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : '',
        X_CSRF_Token: localStorage.getItem('X-CSRF-Token') ? localStorage.getItem('X-CSRF-Token') : '',
        newReplyNum: 0,
        newLikeNum: 0,
        newDisLikeNum: 0,
    },

    mutations: {
        changeLogin(state, user) {
            state.Authorization = user.Authorization;
            localStorage.setItem('Authorization', user.Authorization);
        },

        setCsrfToken(state, user) {
            state.X_CSRF_Token = user.X_CSRF_Token;
            localStorage.setItem('X-CSRF-Token', user.X_CSRF_Token);
        },

        setNewReplyNum(state, user) {
            state.newReplyNum = user.newReplyNum;
        },

        setNewLikeNum(state, user) {
            state.newLikeNum = user.newLikeNum;
        },

        setNewDisLikeNum(state, user) {
            state.newDisLikeNum = user.newDisLikeNum;
        },

        noticeInit(state, user) {
            state.newReplyNum = user.newReplyNum;
            state.newDisLikeNum = user.newDisLikeNum;
            state.newLikeNum = user.newLikeNum;
        }
    },
});

export default store;

