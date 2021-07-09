import axios from "axios";

const tagStore = {
  state: {
    tags: null
  },
  mutations: {
    setTags(state,tags){
      state.tags=tags
    }
  },
  actions: {
    getTags(context){
      axios.get('api/tag/list').then((response) => {
        const rd = response.data
        if (rd.code === 'success') {
          context.commit('setTags',rd.data.tags)
        }
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}

export default tagStore
