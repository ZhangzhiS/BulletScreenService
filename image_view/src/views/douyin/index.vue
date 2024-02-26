<template>
  <app-bar
    :second="second"
    :tips="tips"
    :room_info="room_info_data"
    :connect_click="changeConnection"
  >
  </app-bar>
  <v-container class="fill-height" style="max-width: 100%">
    <v-row no-gutters style="height: 100%">
      <v-spacer></v-spacer>
      <!-- 当前生成信息,排队信息 -->
      <v-col cols="3">
        <image-generating-info
          :nickname="rank_list[0]?.nickname"
          :prompt="rank_list[0]?.prompt"
        ></image-generating-info>
        <br />
        <part-in-desc></part-in-desc>
      </v-col>
      <!-- <v-spacer></v-spacer> -->
      <!-- 上次生成图片预览 -->
      <v-col cols="5">
        <image-preview
          :nickname="last_generating_info.nickname"
          :image_url="last_generating_info.image_url"
          :prompt="last_generating_info.prompt"
          :image_code="last_generating_info.image_code"
          :last_image_url="placeholder_url"
          :progress="last_generating_info.progress"
        ></image-preview>
      </v-col>
      <v-spacer></v-spacer>
      <!-- 排队列表  -->
      <v-col cols="2">
        <queue-list :rank_list="rank_list"></queue-list>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
  <v-footer app height="72">
    <v-text-field
      bg-color="deep-purple-lighten-5"
      class="rounded-pill overflow-hidden text-center"
      hide-details
      variant="solo"
      :readonly="true"
    >
      提示词实例(<strong class="text-red-lighten-1">必须以 "生成-" 开始</strong>
      ): 生成- 一只酷酷的猫在阳台晒太阳
    </v-text-field>
  </v-footer>
  <v-dialog
    transition="dialog-top-transition"
    width="auto"
    v-model="alt_status"
  >
    <v-card>
      <v-toolbar color="primary" title="提示"></v-toolbar>
      <v-card-text>
        <div class="text-h2 pa-12">{{ alt_msg }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" block @click="alt_status = false"
          >关闭（3s后自动关闭）</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script setup lang="ts">
import AppBar from "@/components/AppBar.vue";
import ImageGeneratingInfo from "@/components/ImageGeneratingInfo.vue";
import QueueList from "@/components/QueueList.vue";
import ImagePreview from "@/components/ImagePreview.vue";
import PartInDesc from "@/components/PartInDesc.vue";
import { onMounted, ref } from "vue";
import { useDouyinWsStore } from "@/store/douyinws";

const room_info_data = ref({
  live_room_id: "",
  live_room_title: "",
  url_room_id: "",
  live_room_anchor_nickname: "未连接",
  connection_status: false,
  socia_count: 0,
});

const tips = ref("未开始");

const placeholder_url = ref(
  "https://cdn.discordapp.com/attachments/1136559812776308849/1144197555031379968/zhoumo99_A_cool_cat_basking_in_the_sun_on_the_balcony_f3987b76-a9c4-429c-865c-9f26478419a8.png",
);

const last_generating_info = ref({
  user_id: "",
  nickname: "",
  prompt: "",
  image_code: "",
  image_url: "",
  progress: 0,
});

const second = ref(0);

const alt_msg = ref("");
const alt_status = ref(false);
const alt_second = ref(0);

const generate_task_id = ref("none");

const task_status = ref(false);

const rank_list = ref([
  {
    user_id: "1",
    nickname: "暂无",
    rank_score: 0,
    prompt: "无",
  },
]);

function countdown(duration: any) {
  return new Promise((resolve) => {
    const startTime = Date.now();
    let timerId: string | number | NodeJS.Timeout | undefined;

    function updateCountdown() {
      const now = Date.now();
      const elapsed = now - startTime;

      second.value = Math.max(0, duration - Math.floor(elapsed / 1000));

      if (second.value > 0) {
        timerId = setTimeout(updateCountdown, 1000);
      } else {
        clearTimeout(timerId);
        resolve(true);
      }
    }

    updateCountdown();
  });
}

// 解析直播间信息数据
function parse_refresh_room_info(data: any) {
  room_info_data.value = data.data;
  if (room_info_data.value.socia_count === -1) {
    // alert("请先在抖音开始直播");
    ws_store.ws_connection?.close();
    alt_msg_handler("请先在抖音开启直播", 3000);
  } else {
    room_info_data.value.connection_status = true;
  }
}

// 处理排队信息
function parse_refresh_rank_list(data: any) {
  if (data.data.length > 0) {
    rank_list.value = data.data;
    // last_generating_info.value = data.data[0];
  }
  if (
    data.data.length == 12 &&
    task_status.value === false &&
    second.value === 0
  ) {
    // 如果排队列表等于12且现在无进行中的任务，则开启生成图片的任务
    startGenerating();
    generate_task_id.value = "start";
  }
}

async function parse_refresh_last_generating_info(data: any) {
  last_generating_info.value = data.data;
  // console
  if (data.data.image_url != null && data.data.image_url != placeholder_url.value) {
    placeholder_url.value = data.data.image_url;
  }
  // if (data.data.progress && data.data.progress!)
  if (data.data.task_id) {
    generate_task_id.value = data.data.task_id;
  }
  if (data.data.status === 1) {
    placeholder_url.value = data.data.image_url;
    task_status.value = false;
    await countdown(60);
    second.value = 0;
    // task_status.value = false;
  }
}

function alt_msg_handler(msg: any, timeout: number) {
  alt_msg.value = msg;
  alt_status.value = true;
  alt_second.value = 3;
  setTimeout(() => {
    alt_status.value = false;
  }, timeout); // 3秒后自动关闭
}

// function loadUserInfo(user_id: string) {}

async function onMessage(e: any) {
  const data = JSON.parse(e.data);
  if (data.msg_type == "refresh_room_info") {
    parse_refresh_room_info(data);
  } else if (data.msg_type == "refresh_rank_list") {
    parse_refresh_rank_list(data);
  } else if (data.msg_type == "refresh_last_generating_info") {
    await parse_refresh_last_generating_info(data);
  } else if (data.msg_type == "start_task") {
    task_status.value = true;
    tips.value = "生成中";
  } else if (data.msg_type == "alt_msg") {
    alt_msg_handler(data.data.msg, 3000);
    tips.value = data.data.tips;
  }
}

const timer = ref<NodeJS.Timeout | null>(null);

const ws_store = useDouyinWsStore();

function onWsOpened() {
  timer.value = setInterval(() => {
    if (
      generate_task_id.value != "none" &&
      generate_task_id.value != "start" &&
      task_status.value == true
    ) {
      const data = {
        task_id: generate_task_id.value,
        nickname: last_generating_info.value.nickname,
        user_id: last_generating_info.value.user_id,
        prompt: last_generating_info.value.prompt,
        type: "1",
      };
      ws_store.ws_connection?.send(JSON.stringify(data));
    }
  }, 5000);
}

function onWsError(e: any) {
  console.log(e);
}

function changeConnection() {
  if (room_info_data.value.connection_status === true) {
    ws_store.ws_connection?.close();
    if (timer.value) {
      clearInterval(timer.value);
      ws_store.timer = null;
    }
    room_info_data.value.connection_status = false;
    second.value = 0;
    tips.value = "断开链接";
  } else {
    tips.value = "未开始"
    connectWS();
    room_info_data.value.connection_status = true;
  }
}

function startGenerating() {
  const data = {
    type: "2",
    nickname: rank_list.value[0].nickname,
    prompt: rank_list.value[0].prompt,
    user_id: rank_list.value[0].user_id,
    sys_user_id: 0,
    room_id: room_info_data.value.live_room_id,
  };
  last_generating_info.value = {
    user_id: rank_list.value[0].user_id,
    nickname: rank_list.value[0].nickname,
    prompt: rank_list.value[0].prompt,
    image_code: "",
    image_url: "",
    progress: 0,
  };

  ws_store.ws_connection?.send(JSON.stringify(data));
}

function connectWS() {
  const web_socket_url = "ws://hello.zzs7.top/douyin/"+ws_store.dy_url_id+"/ws";
  ws_store.ws_connection = new WebSocket(web_socket_url);
  ws_store.ws_connection.onmessage = onMessage;
  ws_store.ws_connection.onopen = onWsOpened;
  ws_store.ws_connection.onerror = onWsError;
}

onMounted(() => {
  console.log(ws_store.dy_url_id)
});
</script>
