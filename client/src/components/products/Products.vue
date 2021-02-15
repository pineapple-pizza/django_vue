<template>
  <div>
    <v-parallax dark src="@/assets/photo-food.jpeg" id="parallax-home">
      <v-row no-gutters align="center" justify="center">
        <v-col class="text-center" md="6">
          <v-card class="search-form">

          <h1 class="display-1 font-weight-thin mb-4">
            Du gras, oui, mais de qualité !
          </h1>
          <h4 class="subheading">
            Trouvez un produit de substitution pour ceux que vous consommez tous
            les jours.
          </h4>
          <template v-if="authenticated">
            <search-bar class="mt-3"/>
          </template>
          <template v-else>
            <br />
            <h4>
              Mais inscrivez-vous d'abord ! :)
            </h4>
          </template>
          </v-card>
        </v-col>
      </v-row>
    </v-parallax>
  </div>
</template>

<script>
import Search from "@/components/Search.vue";
import { mapGetters } from "vuex";

export default {
  name: "Products",
  components: {
    "search-bar": Search,
  },
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  },
  mounted() {
    document.getElementById("parallax-home").style.height = "100vh";
  },
};
</script>

<style scoped lang="sass">
.search-form
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: 300px
  padding: 80px
  @media (max-width: 600px)
    height: auto
    padding: 40px
</style>
