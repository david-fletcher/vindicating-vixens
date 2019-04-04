<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
      <v-jumbotron color="primary" dark>
        <v-container fill-height>
          <v-layout align-center>
            <v-flex text-xs-center>
              <h3 class="display-4">Vindicating Vixens</h3>
              <p class="display-1">A second-look at some controversial women in the Bible.</p>
            </v-flex>
          </v-layout>
        </v-container>
      </v-jumbotron>
      <v-flex
              xs12
              md6
              lg3
              v-for="item in vixens"
              :key="item.id"
            >
              <Card v-bind:title="item.name" 
                    v-bind:text="item.short_desc"
                    v-bind:image="item.image"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Card from './Card';
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    Card
  },
  data() {
    return {
      vixens: []
    }
  },
  mounted() {
    axios.get('http://localhost:5000/vixens')
      .then(res => {
        this.vixens = res.data;
        console.log(this.vixens);
      })
      .catch(err => {
        console.log("ERROR RETRIEVING VIXENS", err.response);
      });
  }
}
</script>