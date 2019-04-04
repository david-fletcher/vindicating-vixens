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
      <!-- <v-flex xs12 md6 lg3>
        <Card v-bind:title="'Martha'" v-bind:text="'Martha was a sweet woman who did not want to harm anyone.'"/>
        <Card v-bind:title="'Martha'" v-bind:text="'Martha was a sweet woman who did not want to harm anyone.'"/>
        <Card v-bind:title="'Martha'" v-bind:text="'Martha was a sweet woman who did not want to harm anyone.'"/>
      </v-flex> -->
      <v-flex
              xs12
              md6
              lg3
              v-for="n in 12"
              :key="n"
            >
              <Card v-bind:title="'Martha'" v-bind:text="'Martha was a sweet woman who did not want to harm anyone.'"/>
            </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Card from './Card';

export default {
  name: 'Home',
  components: {
    Card
  },
  data () {
    return {
      //
    }
  }
}
</script>