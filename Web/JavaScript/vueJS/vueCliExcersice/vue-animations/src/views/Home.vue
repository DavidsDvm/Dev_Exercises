<template>
  <div class="home">
    <button @click="animated = !animated">Animation</button>
     <section>
      <transition name="animate" enter-active-class="animate__animated animate__backInDown" leave-active-class="animate__animated animate__bounceOut">
        <img v-if="animated" alt="Vue logo" src="../assets/logo.png">
      </transition><br><hr>
      <div class="imagen2" @mouseover="hoverOver" @mouseout="hoverOut">
        <img :class="classes" alt="Vue logo" src="../assets/logo.png">
      </div>
    </section>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data () {
    return {
      animated: false,
      classes: []
    };
  },
  methods: {
    hoverOver() {
      this.classes = ['animate__animated', 'animate__backInDown'];
    },
    hoverOut() {
      setTimeout(() => {this.classes = []}, 1000);
    }
  }
}
</script>

<style>
.imagen2 {
  margin: 0 auto 0 auto;
  width: 200px;
  height: 200px;
}
</style>
