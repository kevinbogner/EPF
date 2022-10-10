const data = [
  { block: 3217737, client: "Prysm", reward: 5000000000000000000},
  { block: 3217738, client: "Prysm", reward: 5000000000000000000},
  { block: 3217739, client: "Teku", reward: 5017525613000000000},
  { block: 3217740, client: "Prysm", reward: 5002730000000000000},
  { block: 3217741, client: "Prysm", reward: 5001317280000000000},
  { block: 3217742, client: "Prysm", reward: 5007656480000000000},
  { block: 3217743, client: "Prysm", reward: 5000000000000000000},
  { block: 3217744, client: "Lighthouse", reward: 5034142620000000000},
  { block: 3217745, client: "Prysm", reward: 5000000000000000000},
  { block: 3217746, client: "Prysm", reward: 5000000000000000000},
  { block: 3217747, client: "Prysm", reward: 5006022800000000000},
]

function Table() {
  return (
    <div className="App">
      <table>
        <tr>
          <th>Block</th>
          <th>Client</th>
          <th>Reward</th>
        </tr>
        {data.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.block}</td>
              <td>{val.client}</td>
              <td>{val.reward}</td>
            </tr>
          )
        })}
      </table>
    </div>
  );
}
  
export default Table;

//highest https://api.blockprint.sigp.io/blocks/4882248/4882249