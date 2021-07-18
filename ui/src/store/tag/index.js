import axios from "axios";

const tagStore = {
  state: {
    loading: false,
    tags: null
  },
  getters:{
    tagsInitialized(state){
      return state.tags !== null
    }
  },
  mutations: {
    setLoading(state, b){
      state.loading=b
    },
    setTags(state,tags){
      state.tags=tags
    }
  },
  actions: {
    getTags(context){
      if (context.state.tags === null){
        context.commit('setLoading',true)
      }
      axios.get('api/tag/list').then((response) => {
        const rd = response.data
        if (rd.code === 'success') {
          context.commit('setTags',rd.data.tags)
          context.commit('setLoading',false)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default tagStore
