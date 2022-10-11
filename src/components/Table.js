const data = [
  { block: 15723955, slot: 4888021, client: "Lighthouse", reward: 34922932213389509},
  { block: 15723956, slot: 4888022, client: "Lighthouse", reward: 44425782600333138},
  { block: 15723957, slot: 4888023, client: "Teku", reward: 200115147873261992},
  { block: 15723958, slot: 4888024, client: "Lighthouse", reward: 47648568203180921},
  { block: 15723959, slot: 4888025, client: "Prysm", reward: 35169293955722269},
  { block: 15723960, slot: 4888026, client: "Teku", reward: 46196070826817724},
  { block: 15723961, slot: 4888027, client: "Lighthouse", reward: 36506787448140888},
  { block: 15723962, slot: 4888028, client: "Prysm", reward: 2107057631307192},
  { block: 15723963, slot: 4888029, client: "Lighthouse", reward: 88185520424235151},
  { block: 15723964, slot: 4888030, client: "Lighthouse", reward: 98253366250614227},
  { block: 15723965, slot: 4888031, client: "Prysm", reward: 33710061124560808},
]

function Table() {
  return (
    <div className="App">
      <table>
        <tr>
          <th>Block</th>
          <th>Slot</th>
          <th>Client</th>
          <th>Reward</th>
        </tr>
        {data.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.block}</td>
              <td>{val.slot}</td>
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