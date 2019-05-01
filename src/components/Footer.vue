<template>
  <v-footer
    dark
    height="auto"
  >
    <v-layout justify-space-around align-space-around row fill-height>
      <v-flex>
        <v-card
          flat
          tile
          color="primary"
          class="darken-2 white--text text-xs-center"
        >

          <v-card-text class="white--text">
            All content on this site is summarized from the book, <i>Vindicating the Vixens</i>, edited by Sandra Glahn (&copy; 2017).
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>

export default {
  name: 'Footer',
  data() {
    return {
      //
    }
  }
}
</script>