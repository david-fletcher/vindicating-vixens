<template>
  <v-layout align-start justify-end row>
    <v-toolbar dark color="primary">
      <v-toolbar-side-icon @click="toggleNavDrawer"></v-toolbar-side-icon>
      <v-toolbar-title>Vindicating Vixens</v-toolbar-title>
      <v-spacer />
      <v-flex shrink>
        <v-toolbar-items>
          <router-link to="/">
            <v-btn flat icon><v-icon>home</v-icon></v-btn>
          </router-link>
        </v-toolbar-items>
      </v-flex>
    </v-toolbar>
    <Navigation ref="nav"/>
  </v-layout>
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