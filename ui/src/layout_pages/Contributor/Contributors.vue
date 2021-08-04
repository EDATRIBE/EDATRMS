<template>
  <q-page class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
    <div class="q-mx-auto" style="width: 97%">
      <div
        class="row q-mb-md q-px-lg q-py-md bg-dark-light" style="border-radius: 0px; position: relative"
        :class="{'no-wrap': $q.screen.gt.sm}"
        v-for="j in 10" :key="j"
      >
          <q-chip
              dense
              class="absolute q-ma-none text-weight-medium cursor-pointer" color="white" text-color="dark"
              style="right: -3px; top:-3px;  opacity: 1; border-radius: 4px 0px 4px 0px;">
              TA 参与的作品
              <q-icon size=".5em" class="q-mx-sm" name="fas fa-link"/>
          </q-chip>
        <div>
          <q-avatar size="130px" v-ripple class="cursor-pointer q-mr-md q-mt-md">
            <img contain :src="require('assets/3333.png')">
          </q-avatar>
        </div>
        <div style="width: 100%">
          <div class="row items-center q-pt-md  ">
            <div class="text-white text-h5 text-weight-medium q-mr-sm">二仙桥野猪佩奇</div>
            <div class="row text-weight-medium">
              <!--              <q-chip size="0.7em" icon="edit" color="dark" text-color="primary" square class="q-mr-sm q-ml-none">CAPTION EDITOR</q-chip>-->
              <!--              <q-chip size="0.7em" icon="person" color="dark" text-color="accent" square class="q-mr-sm q-ml-none">SYSTEM STAFF</q-chip>-->
              <!--              <q-chip size="0.7em" icon="attach_money" color="dark" text-color="orange-9" square class="q-mr-sm q-ml-none">TOP SPONSOR</q-chip>-->
              <!--              <q-chip size="0.7em" icon="settings" color="dark" text-color="secondary" square class="q-mr-sm q-ml-none">TECHNICAL SUPPORT</q-chip>-->
              <!--              <q-chip size="0.7em" icon="settings" color="dark" text-color="red-7" square class="q-mr-sm q-ml-none">TECHNICAL SUPPORT</q-chip>-->
              <!--              <q-chip size="0.7em" icon="settings" color="dark" text-color="purple-14" square class="q-mr-sm q-ml-none">TECHNICAL SUPPORT</q-chip>-->
              <q-chip size="0.7em" icon="edit" color="dark" text-color="white" square class="q-mr-sm q-ml-none">CAPTION
                EDITOR
              </q-chip>
              <q-chip size="0.7em" icon="person" color="dark" text-color="white" square class="q-mr-sm q-ml-none">SYSTEM
                STAFF
              </q-chip>
              <q-chip size="0.7em" icon="attach_money" color="dark" text-color="white" square class="q-mr-sm q-ml-none">
                TOP SPONSOR
              </q-chip>
              <q-chip size="0.7em" icon="settings" color="dark" text-color="white" square class="q-mr-sm q-ml-none">
                TECHNICAL SUPPORT
              </q-chip>
              <q-chip size="0.7em" icon="settings" color="dark" text-color="white" square class="q-mr-sm q-ml-none">
                TECHNICAL SUPPORT
              </q-chip>
              <q-chip size="0.7em" icon="settings" color="dark" text-color="white" square class="q-mr-sm q-ml-none">
                TECHNICAL SUPPORT
              </q-chip>
            </div>
          </div>
          <q-separator class="q-mt-sm" color="grey-7"></q-separator>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div>
              <q-icon size="1em" class="q-mr-sm" name="fas fa-envelope"></q-icon>
            </div>
            <div class="text-justify">
              amaindex@outlook.com
            </div>
          </div>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div>
              <q-icon size="1em" class="q-mr-sm" name="fab fa-qq"></q-icon>
            </div>
            <div class="text-justify">
              1136342931
            </div>
          </div>
          <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
            <div class="q-pa-none">
              <q-icon size="1em" class="q-mr-sm" name="fas fa-info"></q-icon>
            </div>
            <div class="text-justify">
              以中有足乐者，不知口体之奉不若人也
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "Contributors",
  data() {
    return {
      x: 'edit'
    }
  },
}
</script>

<style lang="sass" scoped>
.bd-gold
  border: solid deeppink 1px

.bl
  border-left: solid
  border-left-color: $primary
  border-width: 2px

</style>
