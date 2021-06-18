<template>
  <q-page  class="row justify-center">
    <div class="col-7 bg-pink-2 column items-center content-center myborder">
      <p>一个宽度为7col的列，主轴从上往下，元素剧中</p>
      <div style="width: 100%;background-color: rebeccapurple" class="myborder">
        一个宽度为100%的div
      </div>
      <div class="row myborder" style="width: 100%;background-color: rebeccapurple">
        <div class="col-3 myborder">在宽度为100的row</div>
        <div class="col-3 myborder">内的宽度为3col的div</div>
        <div class="q-ml-auto myborder">左边距auto</div>
      </div>
      <q-btn style="width: 100px">自动剧中</q-btn>
      <q-btn style="width: 100px" class="q-ml-auto">左边距auto</q-btn>
      <div style="width: 100%;background-color: rebeccapurple" class="myborder row">
        <a href="baidu.com" class="text-accent"> heksdkfsdafdsafasfdsadsadjkldfhasdlsaj</a>
        <a href="baidu.com" class="text-primary"> heksdkfsdafdsldfhasdlsaj</a>
      </div>
      <router-link to="/#an3">00000</router-link>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'flexboxlab',
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
