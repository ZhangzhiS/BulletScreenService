<template>
  <v-app-bar class="px-3" color="grey-lighten-4" flat height="72">
    <v-chip class="ma-2" color="primary" variant="outlined">
      主播:{{props.room_info.live_room_anchor_nickname}}
      <v-avatar end icon="mdi-account-outline"></v-avatar>
    </v-chip>
    {{props.room_info.live_room_title}}
    <v-spacer></v-spacer>
    <v-chip class="ma-2" color="primary" variant="outlined">
      预览倒计时:{{props.second === 0?props.tips:props.second}}
    </v-chip>
    <v-spacer></v-spacer>
    <v-chip class="ma-2" :color="props.room_info.connection_status?'green':'red'" variant="outlined"
      @click="props.connect_click"
    >
      {{props.room_info.connection_status?"已连接":"未连接"}}
      <v-avatar end icon="mdi-play" class="green"></v-avatar>
    </v-chip>
    <!-- <v-spacer></v-spacer> -->
    <v-chip class="ma-2" color="primary" variant="outlined">
      直播间人数:{{props.room_info.socia_count}}
      <v-icon end icon="mdi-account-outline"></v-icon>
    </v-chip>
  </v-app-bar>
</template>

<script setup lang="ts">


interface RoomInfoItem {
  live_room_anchor_nickname: string;
  connection_status: boolean;
  socia_count: number;
  live_room_title: string
}

interface RoomInfo {
  room_info: RoomInfoItem;
  connect_click:() => void;
  tips: string;
  second: number;
}


const props = defineProps<RoomInfo>()
</script>
