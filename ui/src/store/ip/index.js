import axios from "axios";

const ipStore = {
    state: {
        loading: false,
        ips: null,
        searchResults: null,
    },
    getters: {
        ipsInitialized(state) {
            return state.ips !== null && state.searchResults !== null
        }
    },
    mutations: {
        setLoading(state, b) {
            state.loading = b
        },
        setIPs(state, ips) {
            state.ips = ips
        },
        setSearchResults(state, searchResults) {
            state.searchResults = searchResults
        },
    },
    actions: {
        getIPs(context) {
            if (context.state.ips === null) {
                context.commit('setLoading', true)
            }
            axios.get('api/ip/list').then((response) => {
                const rd = response.data
                if (rd.code === 'success') {
                    context.commit('setIPs', rd.data.ips)
                    context.commit('setLoading', false)
                }
            }).catch(function (error) {
                console.log(error)
            })
        },
        searchKeywords(context,keywordsString) {
            context.commit('setLoading', true)
            if (keywordsString === '') {
                context.commit('setSearchResults', context.state.ips)
                context.commit('setLoading', false)
            }else {
                const data = {
                    keywordsString: keywordsString
                }
                axios.post('api/search/keywords',data).then((response) => {
                    const rd = response.data
                    if (rd.code === 'success') {
                        context.commit('setSearchResults', rd.data.ips)
                        context.commit('setLoading', false)
                    }
                }).catch(function (error) {
                    console.log(error)
                })
            }
        }
    }
}

export default ipStore
