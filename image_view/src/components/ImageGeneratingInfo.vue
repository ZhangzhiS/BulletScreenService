<template>
  <v-card style="height: 30%" max-width="344" variant="outlined">
    <v-card-text>
      <div class="text-h6 mb-1 text-center">下次生成</div>
      <p class="text-h7 text--primary">
        用户: {{props.nickname}}
      </p>
      <v-divider></v-divider>
      <p>提示词</p>
      <v-divider></v-divider>
      <div class="text--primary">
        {{props.prompt}}
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">

interface generateInfo  {
  nickname: string;
  prompt: string
}
const props = defineProps<generateInfo>()
</script>
