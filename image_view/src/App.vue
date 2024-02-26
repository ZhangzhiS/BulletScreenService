<template>
  <v-app id="inspire">
    <v-navigation-drawer color="grey-lighten-3" rail>
      <!-- 个人头像 -->
      <home-avatar />

      <!-- 分割线 -->
      <v-divider class="mx-3 my-5"></v-divider>

      <!-- 菜单 -->
      <menu-component />
    </v-navigation-drawer>

    <v-main>
      <router-view v-slot="{ Component, route }">
        <component :is="Component" :key="route.name" />
      </router-view>
    </v-main>

  </v-app>
</template>

<script setup lang="ts">
import HomeAvatar from "@/components/HomeAvatar.vue";
import MenuComponent from "@/components/MenuComponent.vue";

</script>

<style scoped>
</style>
