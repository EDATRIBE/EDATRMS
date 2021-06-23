<!--<template>-->
<!--  <q-page  class="column">-->
<!--    <div style="width: 100%" >-->
<!--      <div class="col-3">1</div>-->
<!--      <div class="col-9 bg-dark">2</div>-->
<!--    </div>-->
<!--  </q-page>-->
<!--</template>-->

<!--<script>-->
<!--export default {-->
<!--  name: 'flexboxlab',-->
<!--  data: () => ({-->
<!--    tab: 'Animations',-->
<!--    LD: true,-->
<!--    expanded: false,-->
<!--    lorem: 'Kazuto "Kirito" Kirigaya enters a virtual-reality, massively multiplayer online role playing game called Sword Art Online. There is no escape from this world unless the player clears the game; however getting a "game over" results in the death of the player.'-->
<!--  }),-->
<!--  created() {-->
<!--  },-->
<!--  mounted() {-->
<!--    this.$axios.get('api/ip/list').then((response) => {-->
<!--      const rd = response.data-->
<!--      console.log('return data:')-->
<!--      console.log(rd)-->
<!--      if (rd.code === 'success') {-->
<!--        this.ips = rd.data.ips-->
<!--        console.log('ips:')-->
<!--        console.log(this.ips)-->
<!--        for(let i=0; i< this.ips.length;i++){-->
<!--          const reservedNames = []-->
<!--          for(let key in this.ips[i].reservedNames){-->
<!--            // console.log(key+":"+this.ips[i].reservedNames[key])-->
<!--            reservedNames.push({'label':key+": "+this.ips[i].reservedNames[key]})-->
<!--          }-->
<!--          this.ips[i].reservedNames= [{-->
<!--            'label': 'reservedNames',-->
<!--            'children': reservedNames-->
<!--          }]-->
<!--          console.log(this.ips[i].reservedNames)-->
<!--          const intros = []-->
<!--          for(let key in this.ips[i].intros){-->
<!--            // console.log(key+":"+this.ips[i].reservedNames[key])-->
<!--            intros.push({'label':key+": "+this.ips[i].intros[key]})-->
<!--          }-->
<!--          this.ips[i].intros= [{-->
<!--            'label': 'intros',-->
<!--            'children': intros-->
<!--          }]-->
<!--          console.log(this.ips[i].intros)-->
<!--        }-->
<!--        // for(var key in this.ips[0].tags){-->
<!--        //   console.log(key+":"+this.ips.tags[key])-->
<!--        // }-->
<!--      }-->
<!--      this.LD=false-->
<!--      this.$forceUpdate()-->

<!--    }).catch(function (error) {-->
<!--      console.log(error)-->
<!--    }).then(()=> {-->
<!--      // document.querySelector("#an4").scrollIntoView(-->
<!--      //   {behavior: "smooth", block: "start"}-->
<!--      // );-->
<!--      this.$nextTick(-->
<!--        document.querySelector("#anm5").scrollIntoView(-->
<!--          {behavior: "smooth", block: "start"}-->
<!--        ))-->
<!--    })-->
<!--  }-->
<!--}-->
<!--</script>-->
