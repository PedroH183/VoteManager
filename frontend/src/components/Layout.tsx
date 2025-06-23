import { Link, Outlet, useNavigate } from 'react-router-dom';
import { useAppDispatch } from '../hooks';
import { logout } from '../slices/authSlice';

export default function Layout() {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logout());
    navigate('/login');
  };

  return (
    <div className="flex min-h-screen">
      <aside className="w-48 bg-gray-800 text-white p-4 space-y-2">
        <h2 className="text-lg font-bold mb-4">Dashboard</h2>
        <nav className="flex flex-col space-y-1">
          <Link to="/" className="hover:underline">Home</Link>
          <Link to="/topics" className="hover:underline">Tópicos</Link>
          <Link to="/sessions" className="hover:underline">Sessões</Link>
          <Link to="/results" className="hover:underline">Resultados</Link>
        </nav>
        <button
          onClick={handleLogout}
          className="w-full bg-red-600 hover:bg-red-700 text-white px-3 py-2 rounded"
        >
          Sair
        </button>
      </aside>
      <main className="flex-1 p-6 bg-gray-50">
        <Outlet />
      </main>
    </div>
  );
}
