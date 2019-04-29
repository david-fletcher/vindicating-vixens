<template>
  <v-parallax 
    :height="height ? height : 700"
    :src="require(`@/assets/${image}`)"
    alt="Photo by Wendy van Zyl from Pexels">
    
    <v-layout justify-center align-center column>
      <div class="display-4 font-weight-black white--text text-xs-center">{{ title }}</div>
      <div class="display-2 font-italic white--text text-xs-center mb-3">{{ subtitle ? subtitle : ""}}</div>
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
  data() {
    return {
      //
    }
  }
}
</script>