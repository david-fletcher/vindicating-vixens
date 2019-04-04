<template>
  <v-card tile>
    <v-img :src="require(`@/assets/${image}`)" 
            contain
    />
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
    },
    image: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      //
    }
  }
}
</script>