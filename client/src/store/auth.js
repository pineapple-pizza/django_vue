import axios from "@/plugins/axios.js";

export default {
  namespaced: true,
  state: {
    token: null,
    user: null,
    email: null
  },

  getters: {
    authenticated(state) {
      return state.token && state.user;
    },

    user(state) {
      return state.user;
    },

    email(state) {
      return state.email;
    }
  },

  mutations: {
    SET_TOKEN(state, token) {
      state.token = token;
    },

    SET_USER(state, data) {
      state.user = data;
    },

    SET_EMAIL(state, data) {
      state.email = data
    }
  },

  actions: {
    async login({ dispatch, commit }, credentials) {
      let res = await axios.post("api/login/", credentials);
      let json_token = JSON.parse(res.data.tokens);
      console.log("res: ", res);
      
      // commit("email", res.data.email)

      let res_test = res.data.username;
      commit("SET_USER", res_test);

      let res_email = res.data.email;
      commit("SET_EMAIL", res_email)

      return dispatch("attempt", json_token);
    },

    async attempt({ commit, state }, token) {
      if (token) {
        commit("SET_TOKEN", token.access);
      }

      if (!state.token) {
          return
      }
    },
    signOut({ commit }) {
        commit("SET_TOKEN", null);
        commit("SET_USER", null);
    }
  },
};
