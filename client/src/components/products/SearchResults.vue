<template>
  <div>
    <v-parallax dark src="@/assets/photo-food-3.jpg" height="300">
      <v-row align="center" justify="center">
        <v-col class="text-center" cols="12">
          <v-card class="mx-auto searched-prod mt-10" max-width="344">
            <v-card-text>
              <h1 class="display-1 font-weight-thin mb-4">
                {{ searched_prod }}
              </h1>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-parallax>

    <v-row align="center" class="row-search">
      <v-col v-for="(result, i) in results" :key="i" md="4">
        <v-card class="mx-auto results-card">
          <v-card-text>
            {{ result.name }}
            <v-btn class="float-right" outlined fab small color="green">
              {{ result.nutrition_grade }}
            </v-btn>
          </v-card-text>
          <v-card-actions class="mt-10">
            <v-row justify="space-around">
            <v-btn
              rounded
              depressed
              dark
              color="amber accent-3"
              class="btn-edit"
              @click="learnMore(result.id)"
              name="learn_more"
            >
              en savoir +
            </v-btn>
            <v-btn
              rounded
              depressed
              color="orange darken-2"
              class="btn-edit"
              dark
              @click="
                dialog = true;
                getId(result.id);
              "
            >
              modifier
            </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-dialog v-model="dialog" max-width="405px">
        <v-card>
          <v-card-title>Sélectionner un produit de substitution </v-card-title>
          <v-divider></v-divider>
          <v-card-text v-for="(result, i) in results" :key="i">
            <v-checkbox
              color="orange darken-3"
              value="orange darken-3"
              :label="result.name"
            >
            </v-checkbox>
            <div class="pl-9">nutriscore : {{ result.nutrition_grade }}</div>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>

            <v-btn color="orange accent-3" text @click="dialog = false">
              Fermer
            </v-btn>
            <v-btn color="orange accent-3" text @click="editSub(sub_id)">
              Enregistrer
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";

export default {
  name: "SearchResults",
  components: {},
  data() {
    return {
      results: [],
      dialogm1: "",
      dialog: false,
      prod_id: null,
      sub_id: null,
      searched_prod: "",
      nutrition_grade: "",
    };
  },
  created() {
    this.results = this.$route.params.data;
    this.searched_prod = this.$route.params.search;
    var i;
    for (i = 0; i < this.results.length; i++) {
      this.sub_id = this.results[i].id;
      this.nutrition_grade = this.results[i].nutrition_grade;
      console.log("created id ", this.sub_id);
    }
    // this.sub_id = this.$route.params.data.results[0].id
  },
  methods: {
    async learnMore(id) {
      const res = await axios.get("products/" + id);
      this.results = res.data;
      this.$router.push({
        name: "singleProduct",
        params: { data: this.results, id: id },
      });
      console.log(res);
    },
    async editSub(id) {
      // let old_id = this.getId();
      this.prod_id = this.getId();
      console.log("edit sub id 2 ", id);
      console.log("edit sub id ", this.prod_id);

      var i;
      for (i = 0; i < this.results.length; i++) {
        this.sub_id = this.results[i].id;
        console.log("created id ", this.sub_id);
      }

      const res = await axios.patch("products/" + id, {
        substitut: this.sub_id,
      });
      console.log(res);
    },
    getId(id) {
      this.prod_id = id;
      //   console.log("get id ", id);
      //   axios.put("products/" + id, {
      //     substitut: this.sub_id,
      //   });
    },
  },
};
</script>

<style scoped lang="sass">
.searched-prod
  border-radius: 50px !important

.results-card
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: 170px
  width: 344px
  padding: 10px
  @media (max-width: 600px)
    width: 250px
    height: auto

.btn-edit
  width: 150px
  @media (max-width: 600px)
    margin: 10px

.test
  // height: 50px

.row-search
  margin-bottom: 150px
  margin-top: 50px

</style>
