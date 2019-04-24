<template>
  <v-hover>
    <v-card tile slot-scope="{ hover }"
      :class="`elevation-${hover ? 12 : 2}`"
    >
      <v-img :src="require(`@/assets/${image}`)" 
              contain
      />
      <v-card-title primary-title>
        <h3 class="display-2">{{ title }}</h3>
      </v-card-title>
      <v-card-text>
        {{ text }}
      </v-card-text>
      <v-card-actions>
        <router-link :to="`/vixens/${fetchID}`" tag="span">
          <v-btn color="primary" flat>Read More</v-btn>
        </router-link>
      </v-card-actions>
    </v-card>
  </v-hover>
</template>

<script>
export default {
  name: 'Card',
  props: {
    title: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: false
    },
    image: {
      type: String,
      required: true
    },
    id: {
      type: Number,
      required: true
    }
  },
  computed: {
    fetchID() {
      return this.$props.id;
    }
  },
  data () {
    return {
      //
    }
  }
}
</script>