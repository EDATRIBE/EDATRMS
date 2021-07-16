import axios from "axios";

const ipStore = {
  state: {
    ready: false,
    ips: null
  },
  mutations: {
    setReady(state, b){
      state.ready=b
    },
    setIPs(state,ips){
      state.ips=ips
    },
  },
  actions: {
    getIPs(context){
      if (context.state.ips === null){
        context.commit('setReady',false)
      }
      axios.get('api/ip/list').then((response) => {
        const rd = response.data
        if (rd.code === 'success') {
          context.commit('setIPs',rd.data.ips)
          context.commit('setReady',true)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default ipStore
