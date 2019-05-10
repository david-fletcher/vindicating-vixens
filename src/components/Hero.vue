<template>
  <v-img 
    :height="height ? height : 700"
    :src="fetchImage">
    
    <v-layout justify-center align-center fill-height column>
      <div :class="titleTextSize" class="font-weight-black white--text text-xs-center">{{ title }}</div>
      <div :class="subtitleTextSize" class="font-italic white--text text-xs-center mb-3">{{ subtitle ? subtitle : ""}}</div>
    </v-layout>

  </v-img>
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
    },
    fetchImage() {
      return `${this.$base_url}/images/${this.image}`
    }
  },
  data() {
    return {
      //
    }
  }
}
</script>