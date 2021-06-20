import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from './axios-api'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
        authUser: false,
        APIData: ''
    },
    mutations: {
        updateStorage(state, { access, refresh }) {
            state.accessToken = access
            state.refreshToken = refresh
        },
        destroyToken(state) {
            state.accessToken = null
            state.refreshToken = null
        },

        authUser(state, { user }) {
            state.authUser = user
        }
    },
    getters: {
        loggedIn(state) {
            return state.accessToken != null
        },
        isVerified(state) {
            return state.authUser
        }

    },
    actions: {
        userLogout(context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken')
            }
        },
        userLogin(context, usercredentials) {
            console.log("data", usercredentials);
            return new Promise((resolve, reject) => {
                getAPI.post('/verify-otp/', {
                    code: usercredentials.OTP,
                    email: usercredentials.email,
                })
                    .then(response => {
                        console.log("Get response", response);
                        context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },

        userVerify(context, usercredentials) {
            console.log("data", usercredentials);
            return new Promise((resolve, reject) => {
                getAPI.post('/login/', {
                    email: usercredentials.email,
                    password: usercredentials.password,
                })
                    .then(response => {
                        console.log("Get response", response);
                        context.commit('authUser', { user: true })
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        }
    }
})
