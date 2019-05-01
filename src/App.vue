<template>
  <v-app dark>
    <Toolbar />
    <v-content>
      <router-view/>
    </v-content>
    <Footer />
  </v-app>
</template>

<script>
import Toolbar from './components/Toolbar';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: { Footer, Toolbar },
  data () {
    return {
      //
    }
  }
}
</script>
