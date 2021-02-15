<template>
  <div>
    <v-card max-width="400" height="400" class="mt-10">
      token validator here

      <div>
        <div v-if="token != null">
          {{ token }}
          Adresse email validée, connectez-vous!
        </div>
        <div v-if="error != null">
          {{ error }}
          Erreur
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";

export default {
  components: {},
  data: () => ({
    token: null,
    error: null,
  }),
  computed: {
    get_token() {
      console.log("token validation", this.$route.query.token);
      return this.$route.query.token;
    },
  },
  async mounted() {
    try {
      let query_token = this.get_token;
      this.token = await axios
        .get("api/email-verify/?token=" + query_token)
        .then((res) => res.data.email);
      console.log("this token", this.token);
      this.error = null;
    } catch (error) {
      this.token = null;
      this.error = error;
    }
  },
};
</script>

<style scoped lang="sass"></style>
