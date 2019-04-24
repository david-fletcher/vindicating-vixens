<template>
  <div>
    <v-toolbar dark color="primary" @click="toggleNavDrawer">
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-toolbar-title>Vindicating Vixens</v-toolbar-title>
    </v-toolbar>
    <Navigation ref="nav"/>
  </div>
</template>

<script>
import Navigation from './Navigation'

export default {
  name: 'Toolbar',
  components: { Navigation },
  methods: {
    toggleNavDrawer() {
      this.$refs.nav.toggle();
    }
  },
  data() {
    return {
      //
    }
  }
}
</script>