import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import api from '../utils/api';

interface VoteState {
  submitting: boolean;
  error: string | null;
}

const initialState: VoteState = {
  submitting: false,
  error: null,
};

export const submitVote = createAsyncThunk(
  'votes/submit',
  async (data: { sessionId: number; value: boolean }) => {
    const res = await api.post(`/sessions/${data.sessionId}/vote`, { value: data.value });
    return res.data;
  }
);

const votesSlice = createSlice({
  name: 'votes',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(submitVote.pending, (state) => {
        state.submitting = true;
        state.error = null;
      })
      .addCase(submitVote.fulfilled, (state) => {
        state.submitting = false;
      })
      .addCase(submitVote.rejected, (state) => {
        state.submitting = false;
        state.error = 'Unable to vote';
      });
  },
});

export default votesSlice.reducer;
