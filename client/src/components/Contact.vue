<template>
  <div id="contact-component" class="background-contact">
    <div>
      <h1 class="display-1 font-weight-thin mt-6 mb-6 text-center">
        Contactez-nous !
      </h1>
      <h3 class="text-center">N'hésitez pas à nous contacter, on vous répondra le plus vite possible.</h3>
      <v-row justify="center">
        <v-col class="text-center">
          <v-icon large color="blue">mdi-phone</v-icon> <br>
          <a class="text-decoration-none black--text" href="tel:123-456-7890">123-456-7890</a>
        </v-col>
        <v-col class="text-center">
          <v-icon large color="green">mdi-email</v-icon> <br>
          <a class="text-decoration-none black--text" href="mailto:oc.projet.django@gmail.com">oc.projet.django@gmail.com</a>
        </v-col>

      </v-row>
    </div>
  </div>
</template>

<script>
export default {
  name: "Contact",
  components: {},
  data() {
    return {};
  },
};
</script>

<style scoped lang="sass">
.background-contact
  background-color: #F5F5F5
  margin-top: 40px
  height: auto
  padding: 40px
  margin-bottom: 100px
</style>
