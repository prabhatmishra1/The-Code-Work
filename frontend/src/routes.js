import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Login from './views/Login'
import Logout from './views/Logout'
import Signup from './views/Signup'
import Auth from './views/Auth'

Vue.use(VueRouter)

export default new VueRouter({
    //The default mode for Vue Router is hash mode. 
    //It uses a URL hash to simulate a full URL so that the page won’t be reloaded when the URL changes.  
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home,
            // meta: {
            //     requiresLogin: true
            // }
        },

        {
            path: '/auth',
            name: 'auth',
            component: Auth,
            props: true,
        },

        {
            path: '/login',
            name: 'login',
            component: Login,
            props: true,
        },

        {
            path: '/logout',
            name: 'logout',
            component: Logout,
        },

        {
            path: '/signup',
            name: 'signup',
            component: Signup,
        },
    ]
})
