import axios from "axios";

const roleStore = {
    state: {
        loading: false,
        roles: null
    },
    getters:{
        rolesInitialized(state){
            return state.roles !== null
        }
    },
    mutations: {
        setLoading(state, b){
            state.loading=b
        },
        setRoles(state,roles){
            state.roles=roles
        },
    },
    actions: {
        getRoles(context){
            if (context.state.roles === null){
                context.commit('setLoading',true)
            }
            axios.get('api/role/list').then((response) => {
                const rd = response.data
                if (rd.code === 'success') {
                    console.log(rd.data.roles)
                    context.commit('setRoles',rd.data.roles)
                    context.commit('setLoading',false)
                }
            }).catch(function (error) {
                console.log(error)
            })
        }
    }
}

export default roleStore
