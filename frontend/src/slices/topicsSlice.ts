import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import api from '../utils/api';

interface Topic {
  id: number;
  title: string;
}

interface TopicsState {
  items: Topic[];
  loading: boolean;
  error: string | null;
}

const initialState: TopicsState = {
  items: [],
  loading: false,
  error: null,
};

export const fetchTopics = createAsyncThunk('topics/fetch', async () => {
  const res = await api.get('/topics');
  return res.data as Topic[];
});

export const createTopic = createAsyncThunk(
  'topics/create',
  async (data: { title: string }) => {
    const res = await api.post('/topics', data);
    return res.data as Topic;
  }
);

const topicsSlice = createSlice({
  name: 'topics',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchTopics.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchTopics.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchTopics.rejected, (state) => {
        state.loading = false;
        state.error = 'Failed to fetch';
      })
      .addCase(createTopic.fulfilled, (state, action) => {
        state.items.push(action.payload);
      });
  },
});

export default topicsSlice.reducer;
