<template>
  <q-dialog v-model="show">
    <div class="bg-dark column q-pa-lg " style="width: 60vw; max-width: 60vw;">
      <q-btn @click="show=false">hello</q-btn>
    </div>
  </q-dialog>
</template>

<script>
export default {
  name: "IPDeleteDialog",
  props: {
    isDeleting: Boolean,
  },
  data() {
    return {
      show: false
    }
  },
  methods: {
  },
  watch: {
    isDeleting(){
      this.show=this.isDeleting
    },
    show(){
      this.$emit('update:isDeleting',this.show)
    }
  },
  computed: {

  }
}
</script>

<style scoped>

</style>
