<script setup lang="ts">
import type MenuItem from "@/interfaces/MenuItemInterface";

/** Drawer menu items */
const items: MenuItem[] = [
  {
    title: "L",
    icon: "mdi mdi-cog",
    to: { name: "Home" },
  },
  {
    title: "T",
    icon: "mdi mdi-music-note",
    to: { name: "Douyin" },
  },
  {
    title: "Disabled Item",
    icon: "mdi-plus-circle",
  },
];
</script>

<template>
  <v-list v-for="item in items" :key="item.title">
    <v-list-item
      :disabled="!item.to"
      :prepend-icon="item.icon"
      :title="item.title"
      :to="item.to"
      link
    />
  </v-list>
</template>
