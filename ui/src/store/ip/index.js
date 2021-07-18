import axios from "axios";

const ipStore = {
  state: {
    loading: false,
    ips: null
  },
  getters:{
    ipsInitialized(state){
      return state.ips !== null
    }
  },
  mutations: {
    setLoading(state, b){
      state.loading=b
    },
    setIPs(state,ips){
      state.ips=ips
    },
  },
  actions: {
    getIPs(context){
      if (context.state.ips === null){
        context.commit('setLoading',true)
      }
      axios.get('api/ip/list').then((response) => {
        const rd = response.data
        if (rd.code === 'success') {
          context.commit('setIPs',rd.data.ips)
          context.commit('setLoading',false)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default ipStore
