<template>
  <div>
    <div class="pa-15 signin-mobile">
      <h2 class="display-1 font-weight-thin mt-6 mb-6 text-center">
        S'enregistrer
      </h2>
      <v-card class="card-form mx-auto">
        <v-card-text>
          <validation-observer ref="observer" v-slot="{ invalid }">
            <form @submit.prevent="signin">
              <validation-provider
                v-slot="{ errors }"
                name="email"
                rules="required|email"
              >
                <v-text-field
                  v-model="email"
                  :error-messages="errors"
                  label="E-mail"
                  required
                  rounded
                  dense
                  filled
                  light
                  color="grey"
                  name="email_signin"
                ></v-text-field>
              </validation-provider>
              <validation-provider
                v-slot="{ errors }"
                name="username"
                rules="required"
              >
                <v-text-field
                  v-model="username"
                  :error-messages="errors"
                  label="Username"
                  required
                  rounded
                  dense
                  filled
                  light
                  color="grey"
                  name="username_signin"
                ></v-text-field>
              </validation-provider>
              <validation-provider name="password" rules="required|min:6">
                <v-text-field
                  type="password"
                  v-model="password"
                  label="Mot de passe"
                  required
                  rounded
                  dense
                  filled
                  light
                  color="grey"
                  name="password_signin"
                >
                </v-text-field>
              </validation-provider>
              <div class="text-center mt-6">
                <v-btn type="submit" :disabled="invalid" rounded name="submit">
                  Envoyer
                </v-btn>
              </div>
            </form>
          </validation-observer>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios.js";
// import { mapActions } from 'vuex'

import { required, email, min } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";

setInteractionMode("eager");

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});

extend("min", {
  ...min,
  message: "Veuillez fournir un mot de passe de plus de 6 caractères",
});

extend("email", {
  ...email,
  message: "L'adresse e-mail doit être valide",
});
export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    email: "",
    password: "",
    username: "",
  }),
  methods: {
    async signin() {
      const res = await axios.post("api/register/", {
        email: this.email,
        username: this.username,
        password: this.password,
      });
      this.$router.replace({
        name: "login",
      });
      console.log("res: ", res);
    },
  },
};
</script>

<style scoped lang="sass">
.signin-bg
  // background-color: #F5F5F5
  margin-top: 40px
  height: 100%
  padding: 40px
  margin-bottom: 100px

.card-form
  border-radius: 30px !important
  box-shadow: 0 2px 12px 0 rgba(195, 191, 185, 0.48), 0 2px 2px 0 rgba(221, 218, 213, 0.36)
  height: 380px
  width: 600px
  padding: 30px
  @media (max-width: 600px)
    height: auto
    padding: 15px

.signin-mobile
  @media (max-width: 600px)
    padding-left: 20px !important
    padding-right: 20px !important
</style>
