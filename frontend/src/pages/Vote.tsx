import { useAppDispatch, useAppSelector } from '../hooks';
import { submitVote } from '../slices/votesSlice';

export default function Vote() {
  const dispatch = useAppDispatch();
  const { current } = useAppSelector((s) => s.sessions);
  const { submitting, error } = useAppSelector((s) => s.votes);

  if (!current) {
    return <p>Nenhuma sessão ativa.</p>;
  }

  const handleVote = (value: boolean) => {
    dispatch(submitVote({ sessionId: current.id, value }));
  };

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-bold">Votação</h1>
      {error && <p className="text-red-500">{error}</p>}
      <div className="space-x-4">
        <button onClick={() => handleVote(true)} disabled={submitting} className="bg-green-500 text-white px-3 py-2 rounded">
          Sim
        </button>
        <button onClick={() => handleVote(false)} disabled={submitting} className="bg-red-500 text-white px-3 py-2 rounded">
          Não
        </button>
      </div>
    </div>
  );
}
