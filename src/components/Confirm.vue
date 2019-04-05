<template>
  <v-card>
    <v-card-text>
      {{ message }}
    </v-card-text>
    <v-card-actions>
      <v-spacer/>
      <v-btn color="secondary" flat @click="cancel">Cancel</v-btn>
      <v-btn color="primary" @click="confirm">Confirm</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Confirm',
  props: {
    message: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      //
    }
  },
  methods: {
    cancel() {
      this.$emit('cancel');
    },
    confirm() {
      this.$emit('confirm');
    }
  }
}
</script>