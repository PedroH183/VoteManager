import { useSelector } from 'react-redux';
import { Navigate } from 'react-router-dom';
import { RootState } from '../store';
import { ReactNode } from 'react';

interface Props {
  children: ReactNode;
}

export default function ProtectedRoute({ children }: Props) {
  const token = useSelector((state: RootState) => state.auth.token);
  
  console.log('ProtectedRoute State:', useSelector((state: RootState) => state));
  
  if (!token) return <Navigate to="/login" replace />;
  return <>{children}</>;
}
