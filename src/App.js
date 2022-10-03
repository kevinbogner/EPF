import './App.css';

function App() {
  return (
    // <> </> only 1 thing returnable, therefore fragement/wrapper.
    <> 
      <div className="App">
        <h1>🍴 Forkchoice</h1>
        <a href="https://github.com/kevinbogner/forkchoice-epf">GitHub</a>
      </div>
      <p>
      Forkchoice aggregates Data of the Consensus Clients and tracks Block Proposals to identify network splits across clients.
      This helps to statistically identify peering issues in the Consensus Client landscape.
      </p>
      <p>
      These data points might help to further improve equality among Consensus Clients.
      </p>
    </>
    
  );
}

export default App;

