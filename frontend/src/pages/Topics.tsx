import { FormEvent, useEffect, useState } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { fetchTopics, createTopic } from '../slices/topicsSlice';

export default function Topics() {
  const dispatch = useAppDispatch();
  const { items, loading } = useAppSelector((s) => s.topics);
  const [title, setTitle] = useState('');

  useEffect(() => {
    dispatch(fetchTopics());
  }, [dispatch]);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (title) {
      dispatch(createTopic({ title }));
      setTitle('');
    }
  };

  return (
    <div className="space-y-6">
      <h1 className="text-xl font-bold">Tópicos</h1>
      <div className="p-6 bg-white rounded shadow">
        <form onSubmit={handleSubmit} className="flex space-x-2">
          <input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="border p-2 flex-grow rounded"
            placeholder="Título do tópico"
          />
          <button
            type="submit"
            className="bg-green-500 text-white px-3 py-2 rounded hover:bg-green-600"
          >
            Adicionar
          </button>
        </form>
      </div>

      {loading && <p>Carregando...</p>}

      <table className="min-w-full divide-y divide-gray-200 bg-white rounded shadow">
        <thead>
          <tr>
            <th className="px-4 py-2 text-center text-xs font-medium text-gray-900 uppercase tracking-wider">ID</th>
            <th className="px-4 py-2 text-center text-xs font-medium text-gray-900 uppercase tracking-wider">Título</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200">
          {items.map((t) => (
            <tr key={t.id}>
              <td className="px-4 py-2 text-center">{t.id}</td>
              <td className="px-4 py-2 text-center">{t.title}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
