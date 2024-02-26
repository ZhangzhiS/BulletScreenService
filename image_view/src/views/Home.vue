<template>

  <v-container class="fill-height" style="max-width: 100%">
   <v-sheet width="300" class="mx-auto">
    <v-form @submit.prevent>
      <v-text-field
        v-model="ws_store.dy_url_id"
        label="直播间ID"
      ></v-text-field>
      <!-- <v-btn type="submit" -->
      <!--     @click="submit" -->
      <!--     block class="mt-2" color="indigo-darken-3">确认</v-btn> -->
    </v-form>
  </v-sheet>
  </v-container>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
import { useDouyinWsStore } from "@/store/douyinws";

const ws_store = useDouyinWsStore();
// const dy_url_id = ref("")

// function submit() {
//   // ws_store.dy_url_id = dy_url_id.value
// }

</script>
