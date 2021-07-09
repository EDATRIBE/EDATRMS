import axios from "axios";

const accountStore = {
  state: {
    user: null
  },
  mutations: {
    setUser(state,user){
      state.user=user
    }
  },
  actions: {
    getUser(context){
      axios.get('api/account/info').then((response) => {
        const rd = response.data
        console.log('return data:')
        console.log(rd)
        if (rd.code === 'success') {
          context.commit('setUser',rd.data.user)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default accountStore
