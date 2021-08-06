import axios from "axios";

const accountStore = {
  state: {
    user: null
  },
  mutations: {
    setCurrentUser(state,user){
      state.user=user
    }
  },
  actions: {
    getCurrentUser(context){
      axios.get('api/account/info').then((response) => {
        const rd = response.data
        if (rd.code === 'success') {
          context.commit('setCurrentUser',rd.data.user)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default accountStore
