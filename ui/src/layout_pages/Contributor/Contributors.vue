<template>
  <q-page class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
    <div class="q-mx-auto" style="width: 95%">
      <div
        class="row q-mb-md q-px-lg q-py-md bg-dark-light" :class="{'no-wrap': $q.screen.gt.sm}"
        v-for="j in 10" :key="j"
      >
        <div>
          <q-avatar size="130px"  v-ripple class="cursor-pointer q-mr-md q-mt-md" v-if="user !== null">
            <img contain :src="require('assets/3333.png')">
          </q-avatar>
        </div>
        <div style="width: 100%">
          <div class="q-pt-md  items-center  text-white text-h5 text-weight-medium">
            二仙桥野猪佩奇
          </div>
          <q-separator class="q-mt-sm" color="white"></q-separator>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div ><q-icon size="1.2em" class="q-mr-sm"  name="email"></q-icon> </div>
            <div class="text-justify">
              amaindex@outlook.com
            </div>
          </div>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div><q-icon size="1.2em" class="q-mr-sm"  name="phone"></q-icon> </div>
            <div class="text-justify">
              17685472365
            </div>
          </div>
          <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
            <div><q-icon size="1.2em" class="q-mr-sm"  name="fas fa-info"></q-icon> </div>
            <div class="text-justify">
              春江潮水连海平，海上明月共潮生。
              滟滟随波千万里，何处春江无月明！
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "Contributors"
}
</script>

<style lang="sass" scoped>
.bd-gold
  border: solid deeppink 1px

</style>
