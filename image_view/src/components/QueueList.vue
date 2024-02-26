<template>
  <v-card class="h-100" variant="outlined">
    <v-table>
      <thead>
        <tr>
          <th class="text-left">用户</th>
          <th class="text-left">积分</th>
          <th class="text-left">提示</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in props.rank_list"
          :key="item.user_id">
          <td>{{ item.nickname }}</td>
          <td>{{ item.rank_score }}</td>
          <td>{{ item.prompt?"有":"无" }}</td>
        </tr>
      </tbody>
    </v-table>
  </v-card>
</template>

<script setup lang="ts">

interface RankItem {
  user_id: string,
  nickname: string,
  prompt: string,
  rank_score: number,
}

interface RankList {
  rank_list: RankItem[]
}

const props = defineProps<RankList>()
</script>
