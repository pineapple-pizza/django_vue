<template>
  <v-footer color="grey lighten-3" padless absolute>
    <v-row justify="center" no-gutters>
      <v-btn color="grey" text rounded class="my-2" to="terms"
        >Mentions légales</v-btn
      >

      <v-btn color="grey" text rounded class="my-2" to="/#contact-component"
        >Contact</v-btn
      >

      <v-col class="grey lighten-4 py-4 text-center grey--text" cols="12">
        {{ new Date().getFullYear() }} — <strong>Pur Beurre</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
  components: {},
  data: () => ({}),
};
</script>

<style scoped lang="sass"></style>
