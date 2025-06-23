import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import api from '../utils/api';

interface AuthState {
  token: string | null;
  loading: boolean;
  error: string | null;
}

const getTokenFromStorage = (): string | null => {
  try {
    return localStorage.getItem('token');
  } catch {
    return null;
  }
};

const initialState: AuthState = {
  token: getTokenFromStorage(),
  loading: false,
  error: null,
};

export const register = createAsyncThunk(
  'auth/register',
  async (data: { cpf: string; password: string, username: string }, { rejectWithValue, fulfillWithValue }) => {
    try {

      const data_payload = { ...data, name: data.username }
      const response = await api.post('/register', data_payload);

      const token = response.data.access_token;

      localStorage.setItem('token', token);
      return token

    } catch (error) {
      console.error('Registration error:', error);
      const message = error.detail[0].msg || 'Erro desconhecido';

      return rejectWithValue(message);
    }
  }
);


export const login = createAsyncThunk(
  'auth/login',
  async (credentials: { cpf: string; password: string }, { rejectWithValue, fulfillWithValue }) => {

    try {
      const params = new URLSearchParams();
      console.log('Logging in with credentials:', credentials);
      params.append('username', credentials.cpf);
      params.append('password', credentials.password);

      const response = await api.post('/login', params, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      const token = response.data.access_token;

      localStorage.setItem('token', token);
      return token

    } catch (error) {
      console.error('Login error:', error);
      const message = error.msg || 'Erro desconhecido';
      return rejectWithValue(message);
    }

  }
);

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    logout(state) {
      state.token = null;
    },
  },
  extraReducers: (builder) => {
    builder
      // Login Cases
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.loading = false;
        state.token = action.payload;
      })
      .addCase(login.rejected, (state) => {
        state.loading = false;
        state.error = 'Login failed';
      })

      // Register Cases 
      .addCase(register.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(register.fulfilled, (state, action) => {
        state.loading = false;
        state.token = action.payload;
        state.error = null;
      })
      .addCase(register.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

export const { logout } = authSlice.actions;
export default authSlice.reducer;
