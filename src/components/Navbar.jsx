function Navbar({ pagina, setPagina }) {
  
  // liga o modo escuro / alto contraste
  function ligarContraste() {
    document.body.classList.toggle('high-contrast')
  }

  return (
    <div className="topo">
      <h1>LABIC</h1>
      <nav>
        <button onClick={() => setPagina('home')}>Home</button>
        <button onClick={() => setPagina('sobre')}>Sobre</button>
        <button onClick={() => setPagina('linhas')}>Linhas</button>
        <button onClick={() => setPagina('contato')}>Contato</button>
        <button onClick={() => setPagina('dashboard')}>Admin</button>
        <button onClick={ligarContraste}>Alto Contraste</button>
      </nav>
    </div>
  )
}

export default Navbar