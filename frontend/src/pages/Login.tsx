import { FormEvent, useState } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { login } from '../slices/authSlice';
import { Link, Navigate } from 'react-router-dom';

export default function Login() {
  
  const dispatch = useAppDispatch();
  const { token, loading } = useAppSelector((s) => s.auth);

  const [cpf, setCpf] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    dispatch(login({ cpf, password }));
  };

  if (token) return <Navigate to="/" replace />;

  return (
    <div className="flex items-center justify-center h-screen">
      <form onSubmit={handleSubmit} className="space-y-4 p-6 bg-white rounded shadow">
        <div>
          <label className="block text-sm font-medium">CPF</label>
          <input value={cpf} onChange={(e) => setCpf(e.target.value)} className="border p-2 w-64" />
        </div>
        <div>
          <label className="block text-sm font-medium">Senha</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="border p-2 w-64" />
        </div>
        <button type="submit" disabled={loading} className="bg-blue-500 text-white px-4 py-2 w-full rounded">
          {loading ? 'Entrando...' : 'Entrar'}
        </button>
        <p className="text-sm">
            Não possui conta? <Link to="/register" className="text-blue-500 underline">Cadastre-se</Link>
        </p>
      </form>
    </div>
  );
}
