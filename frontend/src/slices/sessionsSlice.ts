import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import api from '../utils/api';

interface Session {
  id: number;
  topic_id: number;
  start_time: string;
  end_time: string;
  duration_minutes: number;
  is_open: boolean;
}

interface SessionsState {
  items: Session[];
  loading: boolean;
  error: string | null;
}

const initialState: SessionsState = {
  items: [],
  loading: false,
  error: null,
};

export const openSession = createAsyncThunk(
  'sessions/open',
  async (data: { topicId: number; minutes?: number }) => {

    const payload = {'duration_minutes': data.minutes};
    const res = await api.post(`/topics/${data.topicId}/session`, payload);
    return res.data as Session;
  }
);

export const fetchSessions = createAsyncThunk('sessions/list', async () => {
  const res = await api.get('/sessions');
  return res.data as Session[];
});

const sessionsSlice = createSlice({
  name: 'sessions',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(openSession.fulfilled, (state, action) => {
        state.items.push(action.payload);
      })
      .addCase(fetchSessions.fulfilled, (state, action) => {
        state.items = action.payload;
      });
  },
});

export default sessionsSlice.reducer;
