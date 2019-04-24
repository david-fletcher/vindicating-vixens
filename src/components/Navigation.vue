<template>
  <v-navigation-drawer
        v-model="show"
        absolute
      >
    <v-list>
      <v-list-tile 
        v-for="item in items"
        :key="item.title"
        dense
        @click="loadLink(item.path)"
      >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>
              {{ item.title }}
            </v-list-tile-title>
          </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Navigation',
  methods: {
    toggle() {
      this.show = !this.show;
    },
    loadLink(path) {
      this.$router.push(path);
    }
  },
  data() {
    return {
      show: false,
      items: [
        { 
          icon: 'home',
          title: 'Home',
          path: '/',
        },
        {
          icon: 'people',
          title: 'Manage Vixens',
          path: '/vixens'
        },
        {
          icon: 'image',
          title: 'Manage Images',
          path: '/images'
        }
      ]
    }
  }
}
</script>