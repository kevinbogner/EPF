import { useState } from 'react';
import Axios from 'axios';

function Blockprint() {

    const [joke, setJoke] = useState("")

    const getJoke = () => {
      Axios.get("https://official-joke-api.appspot.com/random_joke").then((response)=> {
        //console.log(response)
        setJoke(response.data.setup + " ... " + response.data.punchline)
      })
    }

    return (
    <div>
        <button onClick={getJoke}>
          Get Joke Now
        </button>
        {joke}
    </div>
    )
}

export default Blockprint;