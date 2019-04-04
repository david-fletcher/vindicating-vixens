<template>
  <v-card tile>
    <v-img src="https://www.futurity.org/wp/wp-content/uploads/2018/04/pink-flowers-against-green_1600.jpg" />
    <v-card-title primary-title>
      <h3 class="display-2">{{ title }}</h3>
    </v-card-title>
    <v-card-text>
      {{ text }}
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" flat>Read More</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Card',
  props: {
    title: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      //
    }
  }
}
</script>