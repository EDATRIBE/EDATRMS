import axios from "axios";

const announcementStore = {
    state: {
        loading: false,
        announcements: null
    },
    getters:{
        announcementsInitialized(state){
            return state.announcements !== null
        }
    },
    mutations: {
        setLoading(state, b){
            state.loading=b
        },
        setAnnouncements(state,announcements){
            state.announcements=announcements
        },
    },
    actions: {
        getAnnouncements(context){
            context.commit('setLoading',true)
            axios.get('api/semi_static/announcements').then((response) => {
                const rd = response.data
                if (rd.code === 'success') {
                    context.commit('setAnnouncements',rd.data.announcements)
                    context.commit('setLoading',false)
                }
            }).catch(function (error) {
                console.log(error)
            })
        }
    }
}

export default announcementStore
