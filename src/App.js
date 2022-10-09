import Header from './components/Header';
import Main from './components/Main';
import Footer from './components/Footer';
import Blockprint from './components/Blockprint';

import './App.css';
import Etherscan from './components/Etherscan';

function App() {

  return (
    // <> </> only 1 thing returnable, therefore fragement/wrapper.
    <> 
      <div className="App">
          <Header />
          <Main />
          <Footer />
          <Blockprint />
          <Etherscan />
      </div>
    </>
  
  );
}

export default App;