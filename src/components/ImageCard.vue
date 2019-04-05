<template>
  <v-card tile>
    <v-img :src="require(`@/assets/${image}`)" 
            contain
    />
    <v-card-title primary-title>
      {{ image }}
    </v-card-title>
    <v-card-actions>
      <v-btn color="primary" flat @click="deleteImage" :disabled="!isallowed">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'ImageCard',
  props: {
    image: {
      type: String,
      required: true
    },
    isallowed: {
      type: Boolean,
      required: true
    }
  },
  data () {
    return {
      //
    }
  },
  methods: {
    deleteImage() {
      this.$emit("delete", this.$props.image);
    }
  }
}
</script>