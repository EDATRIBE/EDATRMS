import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import accountStore from "src/store/account";
import tagStore from "src/store/tag";
import ipStore from "src/store/ip";

export default new Vuex.Store({
  modules:{
    account: accountStore,
    tag: tagStore,
    ip: ipStore
  }
})
