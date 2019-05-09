<template>
  <v-parallax 
    :height="height ? height : 700"
    :src="require(`@/assets/${image}`)">
    
    <v-layout justify-center align-center column>
      <div :class="titleTextSize" class="font-weight-black white--text text-xs-center">{{ title }}</div>
      <div :class="subtitleTextSize" class="font-italic white--text text-xs-center mb-3">{{ subtitle ? subtitle : ""}}</div>
    </v-layout>

  </v-parallax>
</template>

<script>
export default {
  name: "Hero",
  props: {
    height: {
      type: Number,
      required: false
    },
    image: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      required: false
    }
  },
  computed: {
    titleTextSize() {
      switch(this.$vuetify.breakpoint.name) {
        case 'xs':
        case 'sm': return 'display-2'
        default:   return 'display-4'
      }
    },
    subtitleTextSize() {
      switch(this.$vuetify.breakpoint.name) {
        case 'xs':
        case 'sm': return 'display-1'
        default:   return 'display-2'
      }
    }
  },
  data() {
    return {
      //
    }
  }
}
</script>