import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import api from '../utils/api';

interface Session {
  id: number;
  topicId: number;
  active: boolean;
  yes: number;
  no: number;
}

interface SessionsState {
  current: Session | null;
  loading: boolean;
  error: string | null;
}

const initialState: SessionsState = {
  current: null,
  loading: false,
  error: null,
};

export const openSession = createAsyncThunk(
  'sessions/open',
  async (data: { topicId: number; minutes?: number }) => {
    const res = await api.post('/sessions', data);
    return res.data as Session;
  }
);

export const fetchCurrentSession = createAsyncThunk('sessions/current', async () => {
  const res = await api.get('/sessions/current');
  return res.data as Session;
});

const sessionsSlice = createSlice({
  name: 'sessions',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(openSession.fulfilled, (state, action) => {
        state.current = action.payload;
      })
      .addCase(fetchCurrentSession.fulfilled, (state, action) => {
        state.current = action.payload;
      });
  },
});

export default sessionsSlice.reducer;
