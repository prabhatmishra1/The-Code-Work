<template>
  <div class="w-screen h-screen flex justify-center items-center bg-gray-100">
    <div class="loader" v-if="loading"></div>
    <fieldset :disabled="loading">
      <form
        v-on:submit.prevent="signup"
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
        <!-- Error handling -->
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
          <strong class="font-bold">{{ error }}</strong>
        </div>
        <p class="mb-5 text-3xl uppercase text-gray-600">Signup</p>
        <input
          type="email"
          name="email"
          v-model="email"
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
          placeholder="Email"
          required
        />
        <input
          type="text"
          name="mobile"
          v-model="mobile"
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
          placeholder="Phone"
          required
        />
        <input
          type="password"
          name="password"
          v-model="password1"
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
        <input
          type="password"
          name="password"
          v-model="password2"
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
          placeholder="*Confirm Password"
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
          <span>Submit</span>
        </button>
        <router-link :to="{ name: 'auth' }" exact>Login Again</router-link>
      </form>
    </fieldset>
  </div>
</template>



<script>
import { getAPI } from "../axios-api";
export default {
  name: "signup",
  data() {
    return {
      email: "",
      mobile: "",
      password1: "",
      password2: "",
      incorrectAuth: false,
      error: null,
      loading: false,
    };
  },
  methods: {
    async signup() {
      (this.loading = true),
        console.log(this.email, this.mobile, this.password1, this.password2);
      if (this.password1 !== this.password2) {
        this.error = "Password did't match!";
        this.incorrectAuth = true;
        this.loading = false;
        return;
      }

      await getAPI
        .post("/signup/", {
          email: this.email,
          mobile: this.mobile,
          password: this.password1,
        })
        .then((response) => {
          console.log("Data saved");
          console.log(response);
          this.$router.push({
            name: "auth",
            params: { message: "You have been successfully registered." },
          });
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data.email);
          if (err.response.data.email) {
            this.error = err.response.data.email[0];
            this.incorrectAuth = true;
          } else {
            this.error = "Connection Error";
            this.incorrectAuth = true;
          }
        });
    },
  },
};
</script>

