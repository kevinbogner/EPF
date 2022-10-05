import { useState } from 'react';
import Axios from 'axios';

function Blockprint() {

    const [blockprint, setBlockprint] = useState("")

    const getBlockprint = () => {
      Axios.get("https://cryptic-bayou-25710.herokuapp.com/https://api.blockprint.sigp.io/blocks_per_client/96000").then((response)=> {
        //console.log(response)
        setBlockprint(
        " Uncertain: " + response.data.Uncertain +
        " Lighthouse: " + response.data.Lighthouse +
        " Lodestar: " + response.data.Lodestar +
        " Nimbus: " + response.data.Nimbus +
        " Other: " + response.data.Other +
        " Prysm: " + response.data.Prysm +
        " Teku: " + response.data.Teku)
      })
    }

    return (
    <div>
        <button onClick={getBlockprint}>
          Get Blockprint Data for Epoche 96000
        </button>
        {blockprint}
    </div>
    )
}

export default Blockprint;