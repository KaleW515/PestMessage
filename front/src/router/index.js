import Vue from 'vue';
import VueRouter from 'vue-router';
import {Main} from "element-ui";

Vue.use(VueRouter);


const Login = () => import('../components/Login');
const Register = () => import('../components/Register');
const Home = () => import('../components/Home');
const AboutVirus = () => import('../components/AboutVirus');
const Volunteer = () => import('../components/Volunteer');
const Donation = () => import('../components/Donation');
const MessageBoard = () => import('../components/MessageBoard');
const MyPage = () => import('../components/MyPage');
const PutMessage = () => import('../components/PutMessage');
const routes = [
    {
        path: '/',
        name: 'Main',
        redirect: 'login',
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
    },

    {
        path: '/home',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '/about-virus',
                name: 'AboutVirus',
                component: AboutVirus,
            },
            {
                path: '/volunteer',
                name: 'Volunteer',
                component: Volunteer,
            },
            {
                path: '/donation',
                name: 'Donation',
                component: Donation,
            },
            {
                path: '/message-board',
                name: 'MessageBoard',
                component: MessageBoard,
            },
            {
                path: '/my-page',
                name: 'MyPage',
                component: MyPage,
            },
            {
                path: '/put-message',
                name: 'putMessage',
                component: PutMessage,
            },
        ],
    },
    {
        path: '/other-people',
        name: 'OtherPeople',
        component: () => import('../components/OtherPeople'),
    },
];

const router = new VueRouter({
    routes,
});

router.beforeEach((to, from, next) => {
    if (to.path === '/login') {
        next();
    } else if (to.path === '/register') {
        next();
    } else {
        let token = localStorage.getItem('Authorization');
        if (token === null || token === '') {
            next('/login');
        } else {
            next();
        }
    }
});

export default router;
