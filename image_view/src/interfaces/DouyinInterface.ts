export interface RoomInfo {
  room_id: string;
  room_title: string;
  url_room_id: string;
  live_anchor_nickname: string;
  connection_state: boolean;
  socia_count: number;
}


export interface LastGeneratingInfo {
  user_id?: string;
  nickname?: string;
  rank_score?: number;
  prompt?: string;
  image_code?: string;
  inage_url?: string;
}
