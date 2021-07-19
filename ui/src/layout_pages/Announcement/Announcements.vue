<template>
    <q-page padding class=" bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto" style="width: 95%">
            <div class="row q-col-gutter-x-lg"><!--do not set margin-->
                <!--LEFT-->
                <div class="col-md-3 col-xs-12 q-pb-md"><!--do not set margin-->
                    <div class="bg-dark-light text-grey-6" style="border-radius: 5px">
                        <q-list bordered separator v-if="!LD">
                            <q-item
                                clickable v-ripple
                                v-for="(ann,i) in announcements" :key="'ann'+i"
                                class="q-mb-none text-body1 text-weight-medium"
                                @click="$router.push({path:'/ann',query:{title:ann.title}})"
                                active-class="acann"
                                :active="i===currentId"
                            >
                                <q-item-section>
                                    <div class="row no-wrap items-center">
                                        <q-icon size="1.5em" class="q-mr-md" name="article"></q-icon>
                                        {{ ann.title }}
                                    </div>

                                </q-item-section>
                            </q-item>
                        </q-list>
                    </div>
                </div>

                <!--RIGHT-->
                <div class="col-md-9 col-xs-12 q-pb-md "><!--do not set margin-->
                    <div style="width: 100%; border-radius: 5px" class="q-py-md q-px-lg bg-dark-light " v-if="!LD">
                        <q-markdown
                            content-class="text-white" :src="currentText"
                            no-heading-anchor-links
                            no-linkify
                        />
                    </div>
                </div>
            </div>
        </div>
    </q-page>
</template>

<script>


export default {
    name: 'Announcements',
    components: {},
    beforeRouteUpdate(to,from,next){
        this.selectAnnouncement(to.query.title)
        next()
    },
    created() {
        if (this.readyToInitialize) this.selectAnnouncement(this.$route.query.title)
    },
    data() {
        return {
            LD: true,
            currentText: '',
            currentId: 0
        }
    },
    methods: {
        selectAnnouncement(title) {
            this.currentId =0
            for (const i in this.announcements) {
                if (this.announcements[i].title===title){
                    this.currentId=Number(i)
                }
            }
            const uri = this.announcements[this.currentId].uri
            this.$axios.get('api/' + uri).then((response) => {
                this.currentText = response.data
                this.LD = false
            }).catch(function (error) {
                console.log(error)
            })
        }
    },
    computed: {
        announcements() {
            return this.$store.state.announcement.announcements
        },
        readyToInitialize() {
            return this.$store.getters.announcementsInitialized
        }
    },
    watch: {
        readyToInitialize() {
            if (this.readyToInitialize) {
                if (this.readyToInitialize) this.selectAnnouncement(this.$route.query.title)
            }
        }
    }
}
</script>

<style lang="sass" scoped>
.bl
    border-left: solid
    border-left-color: white
    border-width: 2px

.acann
    color: $dark
    background-color: white

//border-right: solid
//border-color: white
//border-width: 2px

</style>
