<template>
  <div>
    <router-link to="/ping">
      <v-btn color="primary">{{ msg }}</v-btn>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Pong',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/pong';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>