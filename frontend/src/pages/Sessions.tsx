import { FormEvent, useEffect, useState } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { openSession, fetchCurrentSession } from '../slices/sessionsSlice';

export default function Sessions() {
  const dispatch = useAppDispatch();
  const { current } = useAppSelector((s) => s.sessions);
  const { items } = useAppSelector((s) => s.topics);
  const [topicId, setTopicId] = useState<number>(0);
  const [minutes, setMinutes] = useState<number>(1);

  useEffect(() => {
    dispatch(fetchCurrentSession());
  }, [dispatch]);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    dispatch(openSession({ topicId, minutes }));
  };

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-bold">Sessão</h1>
      {current ? (
        <div>
          <p>Sessão ativa para o tópico {current.topicId}</p>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="space-y-2">
          <select value={topicId} onChange={(e) => setTopicId(Number(e.target.value))} className="border p-2">
            <option value={0}>Selecione um tópico</option>
            {items.map((t) => (
              <option key={t.id} value={t.id}>{t.title}</option>
            ))}
          </select>
          <input type="number" value={minutes} onChange={(e) => setMinutes(Number(e.target.value))} className="border p-2" />
          <button type="submit" className="bg-blue-500 text-white px-3 py-2 rounded">Abrir Sessão</button>
        </form>
      )}
    </div>
  );
}
