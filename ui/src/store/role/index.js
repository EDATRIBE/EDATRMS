import axios from "axios";

const roleStore = {
    state: {
        loading: false,
        roles: null
    },
    getters:{
        rolesInitialized(state){
            return state.roles !== null
        },
        idRoleDict(state) {
            let d = {}
            if (state.roles) {
                for (const role of state.roles) {
                    d[role.id] = role
                }
            }
            return d
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
