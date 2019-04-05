<template>
  <v-card>
    <v-layout column>
      <v-flex>
        <v-card-title class="headline">Create a Vixen!</v-card-title>
      </v-flex>
      <v-flex>
        <v-card-text>
          <v-text-field :label="'Name'" v-model="name"></v-text-field>
          <v-textarea :label="'Short Description'" v-model="short_desc"></v-textarea>
          <v-textarea :label="'Long Description'" v-model="long_desc"></v-textarea>
          <v-text-field :label="'Image'" v-model="image" readonly @click="chooseImage"></v-text-field>
          <form method="POST" ref="image_form">
            <input type="file" ref="file" name="file" @change="uploadImage" hidden/>
          </form>
        </v-card-text>
      </v-flex>
      <v-divider></v-divider>
      <v-flex>
        <v-card-actions>
          <v-spacer/>
          <v-btn color="secondary" flat @click="cancelDialog">Cancel</v-btn>
          <v-btn color="primary" @click="saveVixen">Submit</v-btn>
        </v-card-actions>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
  import axios from 'axios'
  import { isEmpty } from 'lodash'

  export default {
    name: "ContentForm",
    data() {
      return {
        id: "",
        name: "",
        short_desc: "",
        long_desc: "",
        image: ""
      }
    },
    props: {
      editMode: {
        type: Boolean,
        required: true
      },
      initialData: {
        type: Object,
        required: true
      },
    },
    watch: {
      initialData(vixen) {
        if(isEmpty(vixen)) {
          this.clear();
        } else {
          this.id = vixen.id;
          this.name = vixen.name;
          this.short_desc = vixen.short_desc;
          this.long_desc = vixen.long_desc;
          this.image = vixen.image;
        }
      }
    },
    methods: {
      clear() {
        this.id = "";
        this.name = "";
        this.short_desc = "";
        this.long_desc = "";
        this.image = "";
      },

      chooseImage() {
        this.$refs.file.click();
      },

      uploadImage($event) {
        const files = $event.target.files;
        if(files.length > 0) {
          const form = new FormData(this.$refs.image_form);
          axios.post('http://localhost:5000/images', form)
            .then(res => {
              this.image = files[0].name;
            })
            .catch(err => {
              console.error('ERROR SAVING IMAGE', err.response)
            });
        }
      },

      cancelDialog() {
        this.clear();
        this.$emit('cancel');
      },

      saveVixen() {
        const args = { name: this.name, short_desc: this.short_desc, long_desc: this.long_desc, image: this.image };
        if(this.editMode) {
          axios.patch(`http://localhost:5000/vixens/${this.id}`, args)
            .then(res => {
              this.clear();
              this.$emit('save');
            })
            .catch(err => {
              console.error("ERROR PUTTING VIXEN", err.response);
            });
        } else {
          axios.post('http://localhost:5000/vixens', args)
            .then(res => {
              this.clear();
              this.$emit('save');
            })
            .catch(err => {
              console.error("ERROR POSTING VIXEN", err.response);
            });
        }
      }
    }
  }
</script>