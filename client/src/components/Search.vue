<template>
  <div>

    <v-row align="center" justify="center" no-gutters>
      <v-col>
        <v-text-field
          label="Nom du produit ou de la catégorie"
          rounded
          dense
          filled
          v-model="search"
          light
          class="input-field"
          name="search_bar"
        ></v-text-field>
      </v-col>

      <v-col md="3">
          <div class="pb-md-7 pb-sm-3">
          <v-btn
            depressed
            rounded
            color="amber lighten-1"
            dark
            type="submit"
            @click="getProd()"
            name="search_submit"
            >Chercher</v-btn>
          </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      results: [],
      search: null,
      categories: [],
      randomProd: ''
    };
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  },
  methods: {
    async getProd() {
      const res = await axios.get("products/?search=" + this.search);
      this.results = res.data.results;
    //   var randomProd = Math.floor(Math.random() * this.results.length);
    //   this.randomProd = this.results[randomProd]
      this.$router.push({
        name: "searchResults",
        params: { data: this.results, search: this.search.replace(/ /g, "-") },
      });
      console.log(res);
    },
  },
};
</script>

<style scoped lang="sass">
.input-field
  width: 380px !important
</style>
