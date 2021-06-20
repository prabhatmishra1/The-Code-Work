  
<template>
  <div class="flex flex-wrap py-2">
    <div class="w-full px-4">
      <nav
        class="
          relative
          flex flex-wrap
          items-center
          justify-between
          px-2
          py-3
          bg-indigo-500
          rounded
        "
      >
        <div
          class="
            container
            px-4
            mx-auto
            flex flex-wrap
            items-center
            justify-between
          "
        >
          <div
            class="
              w-full
              relative
              flex
              justify-between
              lg:w-auto
              px-4
              lg:static
              lg:block
              lg:justify-start
            "
          >
            <a
              class="
                text-sm
                font-bold
                leading-relaxed
                inline-block
                mr-4
                py-2
                whitespace-nowrap
                uppercase
                text-white
              "
            >
              Welcome Eklavya
            </a>
          </div>
          <div class="flex lg:flex-grow items-center" id="example-navbar-info">
            <ul class="flex flex-col lg:flex-row list-none ml-auto">
              <li class="nav-item">
                <router-link
                  :to="{ name: 'Home' }"
                  exact
                  class="
                    px-3
                    py-2
                    flex
                    items-center
                    text-xs
                    uppercase
                    font-bold
                    leading-snug
                    text-white
                    hover:opacity-75
                  "
                  >Profile</router-link
                >
              </li>
              <li class="nav-item">
                <router-link
                  :to="{ name: 'logout' }"
                  exact
                  class="
                    px-3
                    py-2
                    flex
                    items-center
                    text-xs
                    uppercase
                    font-bold
                    leading-snug
                    text-white
                    hover:opacity-75
                  "
                  >Logout
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
};
</script>
