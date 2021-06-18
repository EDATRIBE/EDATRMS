<template>
  <q-page padding class="row justify-center" v-if="!LD">
    <div class="col-md-7 col-xs-10 column items-center content-center" v-for="i in 5" :key="i">
      <q-card class="ip-card rounded-borders q-my-lg" flat bordered :id="'anm'+i">
        <q-img width="100%" :src="require('../assets/0334.jpg')">
<!--          <div class="absolute-bottom text-h5 text-center">-->
<!--            {{ips[0].name}}-->
<!--          </div>-->
        </q-img>
        <q-card-section class="q-pb-sm">
<!--          <div class="text-overline text-accent q-pl-xs">-->
<!--            <q-icon name="far fa-folder-open"></q-icon>-->
<!--            series-->
<!--          </div>-->
          <div class="text-h5 text-dark  q-mb-xs">{{ips[0].name}}</div>
          <q-tree
            class="text-caption"
            text-color="grey"
            :nodes="ips[0].reservedNames"
            node-key="label"
            :expanded.sync="expanded"
            :duration="100"
          />
          <q-tree
            class="text-caption"
            text-color="grey"
            :nodes="ips[0].intros"
            node-key="label"
            :expanded.sync="expanded"
            :duration="100"
          />
        </q-card-section>
        <q-separator/>

        <q-card-actions>
          <q-chip dense outline square clickable color="primary" text-color="white" icon-right="tag" v-for="(tag,i) in ips[0].tags" :key="i">
            {{tag.name}}
          </q-chip>
        </q-card-actions>
        <q-separator/>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="dark"
          indicator-color="accent"
          align="justify"
          inline-label
        >
          <q-tab ripple name="Animations" label="Animations" icon="movie"/>
          <q-tab ripple name="Novels" label="Novels" icon="import_contacts"/>
        </q-tabs>

        <q-separator />

        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="Animations" class="q-pa-sm">
            <q-markup-table flat dense>
              <thead>
              <tr>
                <th class="text-left">NAME</th>
                <th class="text-center">TYPE</th>
                <th class="text-center">PRODUCEBY</th>
                <th class="text-center">EPNUM</th>
                <th class="text-right">RELEASEDAT</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(animation,i) in ips[0].animations" :key="i">
                <td class="text-left"><a class="text-primary" href="baodu.com">{{animation.name}}</a></td>
                <td class="text-center">{{animation.type}}</td>
                <td class="text-center">{{animation.producedBy}}</td>
                <td class="text-center">{{animation.episodesNum}}</td>
                <td class="text-right">{{animation.releasedAt}}</td>
              </tr>
              </tbody>
            </q-markup-table>
          </q-tab-panel>

          <q-tab-panel name="Novels" class="q-pa-sm">
            <q-markup-table flat dense>
              <thead>
              <tr>
                <th class="text-left">NAME</th>
                <th class="text-right">TYPE</th>
                <th class="text-right">PRODUCEBY</th>
                <th class="text-right">EPNUM</th>
                <th class="text-right">RELEASEDAT</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(animation,i) in ips[0].animations" :key="i">
                <td class="text-left"><a class="text-primary" href="baodu.com">{{animation.name}}</a></td>
                <td class="text-right">{{animation.type}}</td>
                <td class="text-right">{{animation.producedBy}}</td>
                <td class="text-right">{{animation.episodesNum}}</td>
                <td class="text-right">{{animation.releasedAt}}</td>
              </tr>
              </tbody>
            </q-markup-table>
          </q-tab-panel>

        </q-tab-panels>
      </q-card>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "index.vue",
  data: () => ({
    tab: 'Animations',
    LD: true,
    expanded: false,
    lorem: 'Kazuto "Kirito" Kirigaya enters a virtual-reality, massively multiplayer online role playing game called Sword Art Online. There is no escape from this world unless the player clears the game; however getting a "game over" results in the death of the player.'
  }),
  created() {
  },
  mounted() {
    this.$axios.get('api/ip/list').then((response) => {
      const rd = response.data
      console.log('return data:')
      console.log(rd)
      if (rd.code === 'success') {
        this.ips = rd.data.ips
        console.log('ips:')
        console.log(this.ips)
        for(let i=0; i< this.ips.length;i++){
          const reservedNames = []
          for(let key in this.ips[i].reservedNames){
            // console.log(key+":"+this.ips[i].reservedNames[key])
            reservedNames.push({'label':key+": "+this.ips[i].reservedNames[key]})
          }
          this.ips[i].reservedNames= [{
            'label': 'reservedNames',
            'children': reservedNames
          }]
          console.log(this.ips[i].reservedNames)
          const intros = []
          for(let key in this.ips[i].intros){
            // console.log(key+":"+this.ips[i].reservedNames[key])
            intros.push({'label':key+": "+this.ips[i].intros[key]})
          }
          this.ips[i].intros= [{
            'label': 'intros',
            'children': intros
          }]
          console.log(this.ips[i].intros)
        }
        // for(var key in this.ips[0].tags){
        //   console.log(key+":"+this.ips.tags[key])
        // }
      }
      this.LD=false
      this.$forceUpdate()

    }).catch(function (error) {
      console.log(error)
    }).then(()=> {
      // document.querySelector("#an4").scrollIntoView(
      //   {behavior: "smooth", block: "start"}
      // );
      this.$nextTick(
        document.querySelector("#anm5").scrollIntoView(
        {behavior: "smooth", block: "start"}
      ))
    })
  }
}
</script>

<style lang="sass" scoped>
.ip-card
  width: 100%
  margin-top: 10px
a
  text-decoration: none
</style>
