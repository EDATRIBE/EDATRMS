import axios from "axios";

const userStore = {
    state: {
        loading: false,
        users: null
    },
    getters:{
        usersInitialized(state){
            return state.users !== null
        },
        idUserDict(state) {
            if(state.users){
                let d = {}
                for (const user of state.users) {
                    d[user.id] = user
                }
                return d
            }
            return null
        }
    },
    mutations: {
        setLoading(state, b){
            state.loading=b
        },
        setUsers(state,users){
            state.users=users
        },
    },
    actions: {
        getUsers(context){
            if (context.state.users === null){
                context.commit('setLoading',true)
            }
            axios.get('api/user/list').then((response) => {
                const rd = response.data
                if (rd.code === 'success') {
                    context.commit('setUsers',rd.data.users)
                    context.commit('setLoading',false)
                }
            }).catch(function (error) {
                console.log(error)
            })
        }
    }
}

export default userStore
