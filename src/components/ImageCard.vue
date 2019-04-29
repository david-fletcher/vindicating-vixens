<template>
  <v-hover>
    <v-card tile slot-scope="{ hover }"
      :class="`elevation-${hover ? 12 : 2}`"
    >
      <v-img :src="require(`@/assets/${image}`)" 
              contain
      />
      <v-card-title secondary-title>
        {{ image }}
      </v-card-title>
      <v-card-actions>
        <v-btn color="secondary" flat @click="deleteImage" :disabled="!isallowed">Delete</v-btn>
      </v-card-actions>
    </v-card>
  </v-hover>
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