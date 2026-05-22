function Dashboard() {
  return (
    <div className="pagina">
      <h2>Dashboard de Gestão</h2>
      
      {/* botões de ação */}
      <div style={{ display: 'flex', gap: '1rem', marginBottom: '2rem' }}>
        <button>+ Pesquisador</button>
        <button>+ Projeto</button>
        <button>+ Artigo</button>
      </div>

      {/* lista de pesquisadores */}
      <div className="grid">
        <div className="card">
          <h3>Ana Paula Silva</h3>
          <p>Área: Inteligência Artificial</p>
          <p>Email: ana@labic.com</p>
          <button style={{ background: '#EF4444' }}>Excluir</button>
        </div>
        
        <div className="card">
          <h3>Carlos Mendes</h3>
          <p>Área: Internet das Coisas</p>
          <p>Email: carlos@labic.com</p>
          <button style={{ background: '#EF4444' }}>Excluir</button>
        </div>
      </div>
      
      <p style={{ textAlign: 'center', fontSize: '0.8rem', color: '#666' }}>
        Versão estática. Integração com API em 30/06.
      </p>
    </div>
  )
}

export default Dashboard