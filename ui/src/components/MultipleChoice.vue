<template>
  <div class="row">
    <q-btn
      size="0.75em" flat class="no-border-radius"
      v-for="(opt,i) in options" :key="'opt'+i"
      @click="choice(i)"
      :class="[
        opt.value===value?activeBGClass:BGClass,
        opt.value===value?activeTextClass:textClass
      ]"
    >
      {{ opt.label }}
    </q-btn>
  </div>
</template>

<script>
export default {
  name: "MultipleChoice",
  model: {
    prop: 'value',
    event: 'choice'
  },
  props: {
    value: String,
    options: Array,
    textClass: String,
    activeTextClass: String,
    BGClass: String,
    activeBGClass: String
  },
  methods: {
    choice(i) {
      this.$emit('choice', this.options[i].value)
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>
