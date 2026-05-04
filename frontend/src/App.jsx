import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import { LangProvider } from './context/LangContext'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Pathology from './pages/Pathology'
import Login from './pages/Login'
import Register from './pages/Register'
import Settings from './pages/Settings'
import Differentials from './pages/Differentials'
import DifferentialCase from './pages/DifferentialCase'
import Dashboard from './pages/Dashboard'
import Algorithms from './pages/Algorithms'
import AlgorithmCase from './pages/AlgorithmCase'
import ClinicalImages from './pages/ClinicalImages'
import ClinicalImageCase from './pages/ClinicalImageCase'
import AnatomyMap from './pages/AnatomyMap'
import Quizzes from './pages/Quizzes'
import QuizSession from './pages/QuizSession'
import Community from './pages/Community'
import CommunityCreate from './pages/CommunityCreate'
import CommunityCasePlay from './pages/CommunityCasePlay'
import CommunityModerate from './pages/CommunityModerate'

function ProtectedRoute({ children }) {
  const { user } = useAuth()
  if (!user) return <Navigate to="/login" replace />
  return children
}

function AuthRoute({ children }) {
  const { user } = useAuth()
  if (user) return <Navigate to="/" replace />
  return children
}

function AppRoutes() {
  const { user } = useAuth()
  return (
    <>
      {user && <Navbar />}
      <Routes>
        <Route path="/login"    element={<AuthRoute><Login /></AuthRoute>} />
        <Route path="/register" element={<AuthRoute><Register /></AuthRoute>} />
        <Route path="/"              element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        <Route path="/cases"         element={<ProtectedRoute><Home /></ProtectedRoute>} />
        <Route path="/pathology/:id" element={<ProtectedRoute><Pathology /></ProtectedRoute>} />
        <Route path="/settings"           element={<ProtectedRoute><Settings /></ProtectedRoute>} />
        <Route path="/differentials"      element={<ProtectedRoute><Differentials /></ProtectedRoute>} />
        <Route path="/differential/:id"   element={<ProtectedRoute><DifferentialCase /></ProtectedRoute>} />
        <Route path="/algorithms"            element={<ProtectedRoute><Algorithms /></ProtectedRoute>} />
        <Route path="/algorithm/:id"         element={<ProtectedRoute><AlgorithmCase /></ProtectedRoute>} />
        <Route path="/clinical-images"       element={<ProtectedRoute><ClinicalImages /></ProtectedRoute>} />
        <Route path="/clinical-image/:id"    element={<ProtectedRoute><ClinicalImageCase /></ProtectedRoute>} />
        <Route path="/anatomy"               element={<ProtectedRoute><AnatomyMap /></ProtectedRoute>} />
        <Route path="/quizzes"               element={<ProtectedRoute><Quizzes /></ProtectedRoute>} />
        <Route path="/quiz/:id"              element={<ProtectedRoute><QuizSession /></ProtectedRoute>} />
        <Route path="/community"             element={<ProtectedRoute><Community /></ProtectedRoute>} />
        <Route path="/community/create"      element={<ProtectedRoute><CommunityCreate /></ProtectedRoute>} />
        <Route path="/community/case/:id"    element={<ProtectedRoute><CommunityCasePlay /></ProtectedRoute>} />
        <Route path="/community/moderate"    element={<ProtectedRoute><CommunityModerate /></ProtectedRoute>} />
      </Routes>
    </>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <LangProvider>
          <AppRoutes />
        </LangProvider>
      </AuthProvider>
    </BrowserRouter>
  )
}
