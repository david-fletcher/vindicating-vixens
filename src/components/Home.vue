<template>
  <v-container fluid grid-list-md>
    <Hero :height="getHeight" :image="'hero-image.jpg'" :title="title" :subtitle="subtitle"/>
    <v-layout row wrap>
      <v-flex
              xs12
              sm6
              lg3
              v-for="item in vixens"
              :key="item.id"
            >
              <Card v-bind:title="item.name" 
                    v-bind:text="item.short_desc"
                    v-bind:image="item.image"
                    v-bind:id="item.id"
              />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Card from './Card';
import Hero from './Hero';
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    Card, Hero
  },
  computed: {
    getHeight() {
      switch(this.$vuetify.breakpoint.name) {
        case 'xs':
        case 'sm': return 400;
        default: return 600;
      }
    }
  },
  data() {
    return {
      vixens: [],
      title: 'VINDICATING VIXENS',
      subtitle: 'taking a second look at biblical women'
    }
  },
  mounted() {
    axios.get(`${this.$base_url}/vixens`)
      .then(res => {
        this.vixens = res.data;
      })
      .catch(err => {
        console.log("ERROR RETRIEVING VIXENS", err.response);
      });
  }
}
</script>