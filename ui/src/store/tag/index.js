import axios from "axios";

const tagStore = {
  state: {
    ready: false,
    tags: null
  },
  mutations: {
    setReady(state, b){
      state.ready=b
    },
    setTags(state,tags){
      state.tags=tags
    }
  },
  actions: {
    getTags(context){
      if (context.state.tags === null){
        context.commit('setReady',false)
      }
      axios.get('api/tag/list').then((response) => {
        const rd = response.data
        if (rd.code === 'success') {
          context.commit('setTags',rd.data.tags)
          context.commit('setReady',true)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default tagStore
