<template>
  <div>
    <h1 class="display-1 font-weight-thin mt-6 mb-6 text-center">
      Notre histoire inoubliable 
    </h1>

    <v-row justify="center">
      <v-col md="4" v-for="(item, i) in items" :key="i">
        <v-card class="card-form">
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">
                {{ item.name }}
              </v-list-item-title>
              <v-list-item-content>{{ item.description }} </v-list-item-content>
            </v-list-item-content>

            <v-list-item-avatar tile size="80" color="grey">
              <v-img :src="item.img"></v-img>
            </v-list-item-avatar>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "About",
  components: {},
  data() {
    return {
      items: [
        {
          name: "Colette",
          img: require("@/assets/persona3.png"),
          description:
            "Il faut juste apprendre ou réapprendre à manger “simplement”, c’est à dire avec de bons produits et surtout, cuisinés par nous-même pour éviter le surplus de sucre et de sel.",
        },
        {
          name: "Rémy",
          img: require("@/assets/persona4.png"),
          description:
            "Prenez vous 30min en moyenne pour vous faire un bon repas, du temps qu'on passe devant la télé ou devant son téléphone mais c’est pour la bonne cause. Notre santé est en jeu !",
        },
      ],
    };
  },
};
</script>

<style scoped lang="sass">
.card-form
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: 220px
  padding: 20px
</style>
