import Header from './components/Header';
import Main from './components/Main';
import Footer from './components/Footer';
import Blockprint from './components/Blockprint';
import Etherscan from './components/Etherscan';
import TableClientReward from './components/TableClientReward';

import './App.css';
import TableRelayer7d from './components/TableRelayer7d';
import TableRelayer30d from './components/TableRelayer30d';
import TableSkippedSlots from './components/TableSkippedSlots';



function App() {

  return (
    // <> </> only 1 thing returnable, therefore fragement/wrapper.
    <> 
      <div className="App">
          <Header />
          <Main />
          <Blockprint />
          <Etherscan />
          <TableClientReward />
          <TableRelayer7d />
          <TableRelayer30d />
          <TableSkippedSlots />
          <Footer />
      </div>
    </>
  
  );
}

export default App;