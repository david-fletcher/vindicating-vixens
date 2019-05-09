<template>
  <v-hover>
    <v-card tile slot-scope="{ hover }"
      :class="`elevation-${hover ? 12 : 2}`"
    >
      <v-img :src="require(`@/assets/${image}`)" 
              contain
              @error="imageError"
      />
      <v-card-title secondary-title>
        <h3 class="display-1">{{ title }}</h3>
      </v-card-title>
      <v-card-text class="headline font-weight-light">
        {{ text }}
      </v-card-text>
      <v-card-actions>
        <router-link :to="`/vixens/${fetchID}`" tag="span">
          <v-btn :large="buttonSize" class="subheading" color="primary">Read More</v-btn>
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
    },
    buttonSize() {
      switch(this.$vuetify.breakpoint.name) {
        case 'xs':
        case 'sm': return false;
        default:   return true;
      }
    }
  },
  data () {
    return {
      imageError(err) {
        console.error("IMAGE LOAD ERROR", err);
      }
    }
  }
}
</script>