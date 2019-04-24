<template>
  <v-container fluid grid-list-md>
    <h3 v-if="images.length < 1">No images to display.</h3>
    <v-layout row wrap>
      <v-flex
              xs12
              md6
              lg3
              v-for="item in images"
              :key="item.image"
            >
              <ImageCard v-bind:image="item.image" v-bind:isallowed="item.allowed" v-on:delete="deleteImage"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ImageCard from './ImageCard';
import axios from 'axios';

export default {
  name: 'ManageImages',
  components: {
    ImageCard
  },
  data() {
    return {
      images: []
    }
  },
  methods: {
    refreshImages() {
      axios.get(`${this.$base_url}/images`)
        .then(res => {
          this.images = res.data;
        })
        .catch(err => {
          console.log("ERROR RETRIEVING IMAGES", err.response);
        });
    },

    deleteImage(image) {
      axios.delete(`${this.$base_url}/images/${image}`)
        .then(() => {
          this.refreshImages();
        })      
        .catch(err => {
          console.error("ERROR DELETING IMAGE", err.response);
        })
    }
  },
  mounted() {
    this.refreshImages();
  }
}
</script>