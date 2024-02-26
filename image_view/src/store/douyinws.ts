// Utilities
import { defineStore } from 'pinia'

export const useDouyinWsStore = defineStore('douyinWS', {
  state: () => ({
      connection_status: false,
      ws_connection: null as WebSocket | null,
      timer: null,
      dy_url_id: "",
  }),
  // getters: {
  //   open_connection:() => {
  //     state.ws_connection = new WebSocket("")
  //   }
  // }
})
