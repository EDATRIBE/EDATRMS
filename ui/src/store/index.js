import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import accountStore from "src/store/account";
import tagStore from "src/store/tag";
import ipStore from "src/store/ip";
import announcementStore from "src/store/announcement";
import userStore from "src/store/user";
import roleStore from "src/store/role";

export default new Vuex.Store({
    modules: {
        account: accountStore,
        announcement: announcementStore,
        tag: tagStore,
        ip: ipStore,
        user: userStore,
        role: roleStore
    }
})
