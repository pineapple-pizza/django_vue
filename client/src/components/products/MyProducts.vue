<template>
  <div>
    <v-parallax dark src="@/assets/photo-food-4.jpeg" class="mt-6" height="300">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <v-card class="mx-auto products-card" max-width="344">
            <h1 class="display-1 font-weight-thin mt-6 mb-6 text-center">
              Mes produits favoris
            </h1>
          </v-card>
        </v-col>
      </v-row>
    </v-parallax>

    <v-row align="center">
      <v-col v-for="(result, i) in results" :key="i" md="4" sm="2">
        <v-card class="mx-auto fav-products">
          <v-card-text>
            {{ result.name }}
            <v-btn class="float-right" outlined fab small color="green">
              {{ result.nutrition_grade }}
            </v-btn>
          </v-card-text>
          <v-card-actions class="mt-10">
            <v-btn
              rounded
              depressed
              dark
              color="amber accent-3"
              class="btn-edit"
              :href="result.url"
              target="_blank"
            >
              en savoir +
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";

export default {
  name: "MyProducts",
  components: {},
  data() {
    return {
      results: [],
    };
  },
  created() {
    axios.get("products/").then((response) => {
      var i;
      for (i = 0; i < response.data.results.length; i++) {
        if (response.data.results[i].favorite === true) {
          this.results.push({
            name: response.data.results[i].name,
            nutrition_grade: response.data.results[i].nutrition_grade,
            url: response.data.results[i].url,
          });
          console.log("mes produits: ", this.results);
        }
      }
    });
  },
};
</script>

<style scoped lang="sass">
.products-card
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: auto
  padding: 10px

.fav-products
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: 200px
  padding: 10px
  max-width: 344px
  @media (max-width: 600px)
    max-width: 214px

</style>
