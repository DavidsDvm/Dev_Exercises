<template>
  <div class="about">
    <h1>{{grettig}}</h1>
    <input @keypress.enter="salute" v-model="grettig">
  </div>
</template>

<script>

export default({
  data () {
    return {
      grettig: "asda"
    };
  },
  methods: {
    salute() {
      console.log(this.grettig);
    }
  }
})
</script>
