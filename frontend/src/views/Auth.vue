<template>
  <div class="w-screen h-screen flex justify-center items-center bg-gray-100">
    <div class="loader" v-if="loading"></div>
    <fieldset :disabled="loading">
      <form
        v-on:submit.prevent="login"
        class="
          p-10
          bg-white
          rounded
          flex
          justify-center
          items-center
          flex-col
          shadow-md
        "
      >
        <!-- Toast Notification Danger -->
        <div
          v-if="incorrectAuth"
          class="
            bg-red-100
            border border-red-400
            text-red-700
            px-4
            py-3
            rounded
            relative
          "
          role="alert"
        >
          <strong class="font-bold"
            >Incorrect username or password entered - please try again</strong
          >
        </div>
        <!-- Signup successfuly -->
        <strong v-if="message" class="alert alert alert-success">{{
          message
        }}</strong>
        <p class="mb-5 text-3xl uppercase text-gray-600">Login</p>
        <input
          type="email"
          name="email"
          v-model="email"
          class="
            mb-5
            p-3
            w-80
            focus:border-purple-700
            rounded
            border-2
            outline-none
          "
          autocomplete="off"
          placeholder="Email"
          required
        />
        <input
          type="password"
          name="password"
          v-model="password"
          class="
            mb-4
            p-3
            w-80
            focus:border-purple-700
            rounded
            border-2
            outline-none
          "
          autocomplete="off"
          placeholder="Password"
          required
        />
        <button
          class="
            bg-purple-600
            hover:bg-purple-900
            text-white
            font-bold
            p-2
            rounded
            w-80
          "
          id="login"
          type="submit"
        >
          <span>Login</span>
        </button>
        <router-link :to="{ name: 'signup' }" exact>Create Account</router-link>
      </form>
    </fieldset>
  </div>
</template>

<script>
//import { getAPI } from "../axios-api";
export default {
  name: "auth",
  props: ["message"],
  data() {
    return {
      email: "",
      password: "",
      incorrectAuth: false,
      loading: false,
    };
  },

  created() {
    setTimeout(() => (this.message = null), 4000);
  },
  methods: {
    async login() {
      (this.loading = true),
        this.$store
          .dispatch("userVerify", {
            email: this.email,
            password: this.password,
          })
          .then(() => {
            this.$router.push({ name: "login", params: { email: this.email } });
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
            this.incorrectAuth = true;
          });
    },
  },
};
</script>

<style>
.loader {
  /* Loader Div Class */
  position: absolute;
  top: 0px;
  right: 0px;
  width: 100%;
  height: 100%;
  background-color: #eceaea;
  background-image: url("../assets/ajax-loader.gif");
  background-size: 50px;
  background-repeat: no-repeat;
  background-position: center;
  z-index: 10000000;
  opacity: 0.4;
  filter: alpha(opacity=40);
}
</style>