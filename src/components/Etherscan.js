import { useState } from 'react';
import Axios from 'axios';

function Etherscan() {

    const [etherscan, setEtherscan] = useState("")

    const getEtherscan = () => {
      Axios.get("https://api.etherscan.io/api?module=block&action=getblockreward&blockno=187&apikey=J89B32DSNTZ4WZN8WVGHFFJHFIXEPP4VTQ").then((response)=> {
        //console.log(response)
        setEtherscan(
            " BlockNumber: " + response.data.result.blockNumber +
            " Timestamp: " + response.data.result.timeStamp +
            " BlockReward: " + response.data.result.blockReward)
      })
    }

    return (
    <div>
        <button onClick={getEtherscan}>
          getblockreward 2165403
        </button>
        {etherscan}
    </div>
    )
}

export default Etherscan;