import Header from './components/Header';
import Main from './components/Main';
import Footer from './components/Footer';
import Blockprint from './components/Blockprint';
import Etherscan from './components/Etherscan';
import Table from './components/Table';

import './App.css';


function App() {

  return (
    // <> </> only 1 thing returnable, therefore fragement/wrapper.
    <> 
      <div className="App">
          <Header />
          <Main />
          <Blockprint />
          <Etherscan />
          <Table />
          <Footer />
      </div>
    </>
  
  );
}

export default App;