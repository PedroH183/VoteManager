import { useEffect, useState } from 'react';
import api from '../utils/api';

interface SessionResult {
  session_id: number;
  topic_id: number;
  total_sim: number;
  total_nao: number;
}

interface SessionInfo {
  id: number;
  topic_id: number;
  start_time: string;
  end_time: string;
  is_open: boolean;
}

export default function Results() {
  const [sessions, setSessions] = useState<SessionInfo[]>([]);
  const [results, setResults] = useState<Record<number, SessionResult>>({});

  useEffect(() => {
    api.get('/sessions').then((res) => setSessions(res.data));
  }, []);

  useEffect(() => {
    sessions
      .filter((s) => !s.is_open)
      .forEach((s) => {
        if (!results[s.id]) {
          api.get(`/sessions/${s.id}/result`).then((r) => {
            setResults((prev) => ({ ...prev, [s.id]: r.data }));
          });
        }
      });
  }, [sessions, results]);

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-bold">Resultados</h1>
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Sessão</th>
            <th className="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Tópico</th>
            <th className="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Sim</th>
            <th className="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Não</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {sessions
            .filter((s) => !s.is_open)
            .map((s) => {
              const r = results[s.id];
              return (
                <tr key={s.id} className="hover:bg-gray-50">
                  <td className="px-4 py-2 text-center text-sm text-gray-900">{s.id}</td>
                  <td className="px-4 py-2 text-center text-sm text-gray-900">{s.topic_id}</td>
                  <td className="px-4 py-2 text-center text-sm text-gray-900">{r ? r.total_sim : '-'}</td>
                  <td className="px-4 py-2 text-center text-sm text-gray-900">{r ? r.total_nao : '-'}</td>
                </tr>
              );
            })}
        </tbody>
      </table>
    </div>
  );
}
