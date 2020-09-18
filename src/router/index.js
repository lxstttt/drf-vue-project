import Vue from 'vue'
import Router from 'vue-router'
import register from "../components/register";
import emp_admin from "../components/emp_admin";
import login from "../components/login";
import update from "../components/update";
import add_emp from "../components/add_emp";

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'register',
            component: register,
        },
        {
            path: '/register',
            name: 'register',
            component: register,
        },
        {
            path: '/login',
            name: 'login',
            component: login,
        },
        {
            path: '/emp_admin',
            name: 'emp_admin',
            component: emp_admin,
        },
        {
            path: '/emp_update/:emp',
            name: 'emp_admin',
            component: update,
        },
        {
            path: '/emp_add',
            name: 'emp_add',
            component: add_emp,
        },
    ]
})
