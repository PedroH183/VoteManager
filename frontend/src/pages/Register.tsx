import { FormEvent, useState } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { register } from '../slices/authSlice';
import { Navigate, Link } from 'react-router-dom';


export default function Register() {

    const dispatch = useAppDispatch();
    const { token, loading, error} = useAppSelector((s) => s.auth);
    const [cpf, setCpf] = useState('');
    const [password, setPassword] = useState('');
    const [username, setUsername] = useState('');

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        dispatch(register({ cpf, password, username}));
    };

    if (token) return <Navigate to="/" replace />;

    return (
        <div className="flex items-center justify-center h-screen">
            <form onSubmit={handleSubmit} className="space-y-4 p-6 bg-white rounded shadow">
                { error && (
                    <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
                        {error}
                    </div>
                )}
                <div>
                    <label className="block text-sm font-medium">CPF</label>
                    <input value={cpf} onChange={(e) => setCpf(e.target.value)} className="border p-2 w-64" />
                </div>
                <div>
                    <label className="block text-sm font-medium">Username</label>
                    <input value={username} onChange={(e) => setUsername(e.target.value)} className="border p-2 w-64" />
                </div>
                <div>
                    <label className="block text-sm font-medium">Senha</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="border p-2 w-64" />
                </div>
                <button type="submit" disabled={loading} className="bg-green-500 text-white px-4 py-2 w-full rounded">
                    {loading ? 'Registrando...' : 'Registrar'}
                </button>
                <p className="text-sm">
                    Já possui conta? <Link to="/login" className="text-blue-500 underline">Entrar</Link>
                </p>
            </form>
        </div>
    );
}