const data = [
  {
   "Client": "Prysm",
   "NumberOfSlots": 78206,
   "TotalRewardsInEther": 4666.813660000005,
   "AverageReward": 0.05967334552336145
  },
  {
   "Client": "Lighthouse",
   "NumberOfSlots": 67408,
   "TotalRewardsInEther": 5402.2103300000435,
   "AverageReward": 0.08014197617493538
  },
  {
   "Client": "Teku",
   "NumberOfSlots": 33644,
   "TotalRewardsInEther": 2316.0970999999986,
   "AverageReward": 0.06884131197241702
  },
  {
   "Client": "Nimbus",
   "NumberOfSlots": 7054,
   "TotalRewardsInEther": 496.91897000000034,
   "AverageReward": 0.07044499149418774
  },
  {
   "Client": "Lodestar",
   "NumberOfSlots": 258,
   "TotalRewardsInEther": 18.269150000000003,
   "AverageReward": 0.0708106589147287
  },
  {
   "Client": "Total",
   "NumberOfSlots": 186570,
   "TotalRewardsInEther": 12900.309210000049,
   "AverageReward": 0.06914460636758347
  }
 ]

function TableClientReward() {
  return (
    <div>
      <h2>Data by Blockprint</h2>
      <table>
        <tr>
          <th>Client</th>
          <th>Number of Slots</th>
          <th>Total Rewards in Ether</th>
          <th>Average Reward/Slot</th>
        </tr>
        {data.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.Client}</td>
              <td>{val.NumberOfSlots}</td>
              <td>{val.TotalRewardsInEther}</td>
              <td>{val.AverageReward}</td>
            </tr>
          )
        })}
      </table>
      </div>
  );
}
  
export default TableClientReward;