<template>
  <div>
    <v-parallax
      dark
      src="@/assets/armenian-cuisine.jpg"
      class="mt-6"
      height="300"
    >
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <v-card class="mx-auto account-card" max-width="344">
            <h1 class="display-1 font-weight-thin mt-6 mb-6 text-center">
              Ahoy
              <span class="font-weight-medium user-text">{{ user }}</span> !
            </h1>
          </v-card>
        </v-col>
      </v-row>
    </v-parallax>
    <v-card
      class="mt-10 pa-10 account-card mx-auto"
    >
      <v-text-field v-model="email" label="E-mail" rounded dense filled light color="grey">
      </v-text-field>
    </v-card>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  components: {},
  data() {
    return {};
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
      email: "auth/email",
    }),
  },
};
</script>

<style scoped lang="sass">
.account-card
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: 150px
  padding: 10px
  max-width: 444px
  @media (max-width: 600px)
    max-width: 344px !important

.user-text
  color: #F57F17
</style>
