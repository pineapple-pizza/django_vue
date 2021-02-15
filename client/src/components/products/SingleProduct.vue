<template>
  <div>
    <v-parallax dark src="@/assets/photo-food-3.jpg" class="mt-6">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <v-card class="mx-auto results-card" max-width="344">
            <v-card-text>
              {{ results.name }}
              <v-btn disabled text fab large color="green">
                {{ results.nutrition_grade }}
              </v-btn>
              <v-btn icon @mouseover="hover = true" @mouseleave="hover = false" @click="addFav">
                <v-icon>
                  mdi-star-outline
                </v-icon>
              </v-btn>
              <p v-if="hover">Ajouter ce produit aux favoris</p>
            </v-card-text>
            <v-card-actions class="pl-6">
              <v-btn depressed rounded dark color="orange darken-2" :href="url">
                voir la fiche d'openfoodfacts
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-parallax>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";

export default {
  name: "SingleProduct",
  components: {},
  data() {
    return {
      results: [],
      url: "",
      hover: false,
    };
  },
  created() {
    this.results = this.$route.params.data;
    this.url = this.results.url;
    console.log("created id", this.results.id)
  },
  methods: {
    async addFav() {
      const res = await axios.patch("products/" + this.results.id, {
        favorite: true,
      });
      console.log(res);
    }
  },
};
</script>

<style scoped lang="sass">
.results-card
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: auto
  padding: 10px
</style>
