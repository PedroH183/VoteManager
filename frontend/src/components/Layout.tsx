import { Link, Outlet } from 'react-router-dom';

export default function Layout() {
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
      </aside>
      <main className="flex-1 p-6 bg-gray-50">
        <Outlet />
      </main>
    </div>
  );
}
