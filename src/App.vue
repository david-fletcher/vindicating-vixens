<template>
  <v-app dark>
    <Toolbar />
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Toolbar from './components/Toolbar';
import Hero from './components/Hero';

export default {
  name: 'App',
  components: { Hero, Toolbar },
  data () {
    return {
      //
    }
  }
}
</script>
