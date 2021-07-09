<template>
  <div>
    <index-i-ps></index-i-ps>
    <index-tags></index-tags>
  </div>
</template>

<script>

import IndexIPs from "src/layout_pages/Index/IndexIPs";
import IndexTags from "src/layout_pages/Index/IndexTags";

export default {
  name: "indexIPsAndTags",
  components: {IndexTags, IndexIPs}
}
</script>

<style scoped>

</style>
