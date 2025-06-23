import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';
import topicsReducer from './slices/topicsSlice';
import sessionsReducer from './slices/sessionsSlice';
import votesReducer from './slices/votesSlice';
import { setTokenGetter } from './utils/api';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    topics: topicsReducer,
    sessions: sessionsReducer,
    votes: votesReducer,
  },
});

setTokenGetter(() => store.getState().auth.token);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
