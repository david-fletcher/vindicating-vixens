<template>
  <v-container>
    <v-layout align-space-around justify-center fill-height column>
      <v-flex>
        <Hero :height="500" :image="vixen.image" :title="vixen.name" :subtitle="vixen.short_desc"/>
      </v-flex>
      <br />
      <v-divider dark />
      <v-flex v-for="(p, index) in vixen.paragraphs" :key="index">
        <br />
        <div class="paragraph">{{ p }}</div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
import Hero from './Hero';

export default {
  name: 'VixenDetail',
  components: { Hero },
  data() {
    return {
      vixen: {
        image: 'hero-image.jpg',
        name: '',
        short_desc: '',
        paragraphs: ['']
      }
    }
  },
  mounted() {
    axios.get(`${this.$base_url}/vixens/${this.$route.params.id}`)
      .then(res => {
        this.vixen = res.data;
      })
      .catch(err => {
        console.error(err.response);
      })
  }
}
</script>

<style scoped>
  .paragraph {
    font-size: 115%;
  }
</style>