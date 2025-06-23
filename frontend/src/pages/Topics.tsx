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
    <div className="space-y-4">
      <h1 className="text-xl font-bold">Tópicos</h1>
      <form onSubmit={handleSubmit} className="space-x-2">
        <input value={title} onChange={(e) => setTitle(e.target.value)} className="border p-2" />
        <button type="submit" className="bg-green-500 text-white px-3 py-2 rounded">Adicionar</button>
      </form>
      {loading && <p>Carregando...</p>}
      <ul className="list-disc pl-5 space-y-1">
        {items.map((t) => (
          <li key={t.id}>{t.title}</li>
        ))}
      </ul>
    </div>
  );
}
