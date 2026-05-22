import { useState } from 'react'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Home from './pages/Home'
import Sobre from './pages/Sobre'
import LinhasPesquisa from './pages/LinhasPesquisa'
import Contato from './pages/Contato'
import Dashboard from './pages/Dashboard'
import Formulario from './pages/Formulario'

function App() {
  // página sendo exibida
  const [pagina, setPagina] = useState('home')

  // exibindo página certa
  function renderizarPagina() {
    if (pagina === 'home') return <Home setPagina={setPagina} />
    if (pagina === 'sobre') return <Sobre />
    if (pagina === 'linhas') return <LinhasPesquisa />
    if (pagina === 'contato') return <Contato />
    if (pagina === 'dashboard') return <Dashboard />
    if (pagina === 'formulario') return <Formulario />
    return <Home setPagina={setPagina} />
  }

  return (
    <>
      <Navbar pagina={pagina} setPagina={setPagina} />
      <main className="container">
        {renderizarPagina()}
      </main>
      <Footer />
    </>
  )
}

export default App