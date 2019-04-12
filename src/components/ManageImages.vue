<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
      <router-link to="/" tag="span">
        <v-btn color="primary" outline><v-icon small>arrow_back_ios</v-icon>Home</v-btn>
      </router-link>
      <h3 v-if="images.length < 1">No images to display.</h3>
      <v-hover>
        <v-flex
                xs12
                md6
                lg3
                v-for="item in images"
                :key="item.image"
              >
                <ImageCard v-bind:image="item.image" v-bind:isallowed="item.allowed" v-on:delete="deleteImage"/>
        </v-flex>
      </v-hover>
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
          console.log(res.data);
        })
        .catch(err => {
          console.log("ERROR RETRIEVING IMAGES", err.response);
        });
    },

    deleteImage(image) {
      axios.delete(`${this.$base_url}/images/${image}`)
        .then(res => {
          console.log("IMAGE DELETED");
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