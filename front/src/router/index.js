import Vue from 'vue';
import VueRouter from 'vue-router';
import {Main} from "element-ui";

Vue.use(VueRouter);


const Login = () => import('../components/Login');
const Register = () => import('../components/Register');
const MainPage = () => import('../components/MainPage');
const AboutVirus = () => import('../components/AboutVirus');
const Volunteer = () => import('../components/Volunteer');
const Donate = () => import('../components/Donate');
const MessageBoard = () => import('../components/MessageBoard');
const MyPage = () => import('../components/MyPage');
const RevisePwd = () => import('../components/RevisePwd');
const PutMessage = () => import('../components/PutMessage');
const routes = [
    {
        path: '/',
        name: 'Home',
        redirect: '/Login',
    },
    {
        path: '/Login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/Register',
        name: 'Register',
        component: Register,
    },

    {
        path: '/MainPage',
        name: 'MainPage',
        component: MainPage,
        children: [
            {
                path: '/AboutVirus',
                name: 'AboutVirus',
                component: AboutVirus,
            },
            {
                path: '/Volunteer',
                name: 'Volunteer',
                component: Volunteer,
            },
            {
                path: '/Donate',
                name: 'Donate',
                component: Donate,
            },
            {
                path: '/MessageBoard',
                name: 'MessageBoard',
                component: MessageBoard,
            },
            {
                path: '/MyPage',
                name: 'MyPage',
                component: MyPage,
            },
            {
                path: '/RevisePwd',
                name: 'RevisePwd',
                component: RevisePwd,
            },
            {
                path: '/PutMessage',
                name: 'putMessage',
                component: PutMessage,
            },
        ],
    },
    {
        path: '/OtherPeople',
        name: 'OtherPeople',
        component: () => import('../components/OtherPeople'),
    },
];

const router = new VueRouter({
    routes,
});

router.beforeEach((to, from, next) => {
    if (to.path === '/Login') {
        next();
    } else if (to.path === '/Register') {
        next();
    } else {
        let token = localStorage.getItem('Authorization');
        if (token === null || token === '') {
            next('/Login');
        } else {
            next();
        }
    }
});

export default router;
