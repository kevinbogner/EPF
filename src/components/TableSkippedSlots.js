const data = [
    {
     "Slots": 204809,
     "ProposedSlots": 203328,
     "SkippedSlots": 1481,

    }
   ]
  
  function TableSkippedSlots() {
    return (
      <div>
        <h2>Data by https://beaconcha.in/</h2>
        <table>
          <tr>
            <th>Slots</th>
            <th>Proposed Slots</th>
            <th>Skipped Slots</th>
          </tr>
          {data.map((val, key) => {
            return (
              <tr key={key}>
                <td>{val.Slots}</td>
                <td>{val.ProposedSlots}</td>
                <td>{val.SkippedSlots}</td>
              </tr>
            )
          })}
        </table>
        </div>
    );
  }
    
  export default TableSkippedSlots;