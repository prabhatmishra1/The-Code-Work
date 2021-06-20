<template>
  <div class="Home">
    <Navbar></Navbar>
    <section
      class="min-h-screen flex items-center justify-center px-4 bg-white"
    >
      <div
        class="
          max-w-xl
          w-full
          rounded-lg
          shadow-lg
          p-4
          flex
          md:flex-row
          flex-col
        "
      >
        <div class="flex-1">
          <h3 class="text-gray-500 my-1 text-center">
            Hello! {{ APIData.username }}
          </h3>
        </div>
        <div class="md:px-2 mt-3 md:mt-0 items-center flex"></div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import { getAPI } from "../axios-api";
import { mapState } from "vuex";
export default {
  name: "Home",

  onIdle() {
    this.$store.dispatch("userLogout").then(() => {
      this.$router.push({ name: "auth" });
    });
  },

  components: {
    Navbar,
  },
  computed: mapState(["APIData"]),
  created() {
    getAPI
      .get("/get-user/", {
        headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
      })
      .then((response) => {
        console.log("Post API has recieved data", response.data);
        this.$store.state.APIData = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>