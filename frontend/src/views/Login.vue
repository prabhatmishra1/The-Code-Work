<template>
  <div class="w-screen h-screen flex justify-center items-center bg-gray-100">
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
        <strong class="font-bold">Holy smokes! Wrong OTP</strong>
      </div>
      <p class="mb-5 text-3xl uppercase text-gray-600">OTP</p>
      <input
        type="text"
        name="otp"
        v-model="OTP"
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
        placeholder="Enter OTP"
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
  </div>
</template>

<script>
export default {
  name: "login",
  props: ["message", "email"],
  data() {
    return {
      OTP: "",
      user: this.email,
      incorrectAuth: false,
    };
  },
  methods: {
    login() {
      console.log(this.user);
      this.$store
        .dispatch("userLogin", {
          OTP: this.OTP,
          email: this.user,
        })
        .then(() => {
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          this.login = false;
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>

<style>
body {
  background-color: #f4f4f4;
}
.login {
  background-color: #fff;
  margin-top: 10%;
}
input {
  padding: 25px 10px;
}
</style>
