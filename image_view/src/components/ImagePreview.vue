<template>
  <v-card class="w-100 h-100">
    <v-img class="align-end text-white" style="width: 100%" :src="props.last_image_url"
    >
      <v-card-title>{{
        props.nickname ? "用户: " + props.nickname : ""
      }}</v-card-title>
    </v-img>
    <v-progress-linear :model-value="props.progress" :height="18" color="green"></v-progress-linear>
    <v-card-text>
      <div class="text-overline mb-1">{{ props.prompt }}</div>
      <div class="text-overline mb-1">
        {{ props.image_code ? "CODE" + props.image_code : "" }}
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
interface PrevireItem {
  nickname: string;
  image_url: string;
  image_code: string;
  prompt: string;
  last_image_url: string;
  progress: number;
}
const props = defineProps<PrevireItem>();
</script>
