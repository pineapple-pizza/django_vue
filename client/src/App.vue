<template>
  <div id="app">
    <v-app>
      <v-main>
        <my-navbar></my-navbar>
        <router-view></router-view>
        <v-container fluid class="container-edit"></v-container>
        <my-footer></my-footer>
      </v-main>
    </v-app>
  </div>
</template>
<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Home",
  components: {
    "my-navbar": Navbar,
    "my-footer": Footer,
  },
};
</script>

<style lang="sass">
.container-edit
  height: 120px

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus textarea:-webkit-autofill,
textarea:-webkit-autofill:hover textarea:-webkit-autofill:focus,
select:-webkit-autofill,
select:-webkit-autofill:hover,
select:-webkit-autofill:focus 
    -webkit-background-clip: text
</style>
