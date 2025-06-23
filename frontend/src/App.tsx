import { Route, Routes, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Topics from './pages/Topics';
import Sessions from './pages/Sessions';
import Results from './pages/Results';
import ProtectedRoute from './components/ProtectedRoute';
import Layout from './components/Layout';
import Register from './pages/Register';

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Layout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Dashboard />} />
        <Route path="topics" element={<Topics />} />
        <Route path="sessions" element={<Sessions />} />
        <Route path="results" element={<Results />} />
      </Route>
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}

export default App;
