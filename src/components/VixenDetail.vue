<template>
  <v-container>
    <v-layout align-center justify-center fill-height column>
      <v-flex>
        <h2>{{ vixen.name }}</h2>
      </v-flex>
      <v-flex>
        <p class="font-weight-light font-italic">{{ vixen.short_desc }}</p>
      </v-flex>
      <v-flex align-self-start>
        <p class="">{{ vixen.long_desc }}</p>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'VixenDetail',
  data() {
    return {
      vixen: {}
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