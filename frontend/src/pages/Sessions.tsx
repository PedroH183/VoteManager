import { FormEvent, useEffect, useState } from 'react';
import { useAppDispatch, useAppSelector } from '../hooks';
import { openSession, fetchSessions } from '../slices/sessionsSlice';
import { submitVote } from '../slices/votesSlice';

export default function Sessions() {
  const dispatch = useAppDispatch();
  const { items } = useAppSelector((s) => s.sessions);
  const { items: topics } = useAppSelector((s) => s.topics);
  const [topicId, setTopicId] = useState<number>(0);
  const [minutes, setMinutes] = useState<number>(1);

  useEffect(() => {
    dispatch(fetchSessions());
  }, [dispatch]);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    dispatch(openSession({ topicId, minutes }));
  };

  const handleVote = (sessionId: number, topicId: number, option: string) => {
    dispatch(submitVote({ sessionId, topicId, option }));
  };

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-bold">Sessão</h1>
      <form onSubmit={handleSubmit} className="space-y-2">
        <select value={topicId} onChange={(e) => setTopicId(Number(e.target.value))} className="border p-2">
          <option value={0}>Selecione um tópico</option>
          {topics.map((t) => (
            <option key={t.id} value={t.id}>{t.title}</option>
          ))}
        </select>
        <input type="number" value={minutes} onChange={(e) => setMinutes(Number(e.target.value))} className="border p-2" />
        <button type="submit" className="bg-blue-500 text-white px-3 py-2 rounded">Abrir Sessão</button>
      </form>

      <table className="min-w-full divide-y divide-gray-200">
        <thead>
          <tr>
            <th className="px-4 py-2text-center text-xs font-medium text-gray-900 uppercase tracking-wider">ID</th>
            <th className="px-4 py-2text-center text-xs font-medium text-gray-900 uppercase tracking-wider">Tópico</th>
            <th className="px-4 py-2text-center text-xs font-medium text-gray-900 uppercase tracking-wider">Início</th>
            <th className="px-4 py-2text-center text-xs font-medium text-gray-900 uppercase tracking-wider">Fim</th>
            <th className="px-4 py-2text-center text-xs font-medium text-gray-900 uppercase tracking-wider">Ações</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200">
          {items.map((s) => (
            <tr key={s.id}>
              <td className="px-4 py-2 text-center text-xs font-medium text-gray-900 uppercase tracking-wider">{s.id}</td>
              <td className="px-4 py-2 text-center text-xs font-medium text-gray-900 uppercase tracking-wider">{s.topic_id}</td>
              <td className="px-4 py-2 text-center text-xs font-medium text-gray-900 uppercase tracking-wider">{s.start_time}</td>
              <td className="px-4 py-2 text-center text-xs font-medium text-gray-900 uppercase tracking-wider">{s.end_time}</td>
              <td className="px-4 py-2 space-x-2">
                {s.is_open ? (
                  <>
                    <button
                      onClick={() => handleVote(s.id, s.topic_id, 'Sim')}
                      className="bg-green-500 text-white px-2 py-1 rounded hover:bg-green-600"
                    >
                      Sim
                    </button>
                    <button
                      onClick={() => handleVote(s.id, s.topic_id, 'Não')}
                      className="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
                    >
                      Não
                    </button>
                  </>
                ) : (
                  <span className="text-gray-500">Sessão fechada</span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
