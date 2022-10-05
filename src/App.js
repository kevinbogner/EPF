import Header from './components/Header';
import Main from './components/Main';
import Footer from './components/Footer';
import Blockprint from './components/Blockprint';

import './App.css';

function App() {

  return (
    // <> </> only 1 thing returnable, therefore fragement/wrapper.
    <> 
      <div className="App">
          <Header />
          <Main />
          <Footer />
          <Blockprint />
      </div>
    </>
  
  );
}

export default App;