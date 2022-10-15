const data = [
  {
   "Name": "Flashbots (Relay)",
   "BlockCount": "20715 (41.10%)",
   "UniqueBuilder": 27,
   "AverageReward": "0.12284278 ETH",
   "HighestReward": "81.00241977 ETH (Slot 4903350)",
   "OverallRewards": "2,544.68820111 ETH",
   "Uncensored": "No",
   "Unfiltered": "Yes"
  },
  {
   "Name": "BloXroute [Max-Profit] (Relay)",
   "BlockCount": "1625 (3.22%)",
   "UniqueBuilder": 3,
   "AverageReward": "0.08211211 ETH",
   "HighestReward": "13.52927684 ETH (Slot 4903353)",
   "OverallRewards": "133.43217647 ETH",
   "Uncensored": "Yes",
   "Unfiltered": "Yes"
  },
  {
   "Name": "Blocknative (Relay)",
   "BlockCount": "1295 (2.57%)",
   "UniqueBuilder": 1,
   "AverageReward": "0.08038891 ETH",
   "HighestReward": "16.52316402 ETH (Slot 4905606)",
   "OverallRewards": "104.10363284 ETH",
   "Uncensored": "No",
   "Unfiltered": "???"
  },
  {
   "Name": "Eden Network (Relay)",
   "BlockCount": "1087 (2.16%)",
   "UniqueBuilder": 2,
   "AverageReward": "0.38496164 ETH",
   "HighestReward": "278.29152063 ETH (Slot 4867314)",
   "OverallRewards": "418.45330459 ETH",
   "Uncensored": "No",
   "Unfiltered": "???"
  },
  {
   "Name": "BloXroute [Ethical] (Relay)",
   "BlockCount": "1056 (2.10%)",
   "UniqueBuilder": 2,
   "AverageReward": "0.05564702 ETH",
   "HighestReward": "1.45552517 ETH (Slot 4904798)",
   "OverallRewards": "58.76325639 ETH",
   "Uncensored": "Yes",
   "Unfiltered": "No"
  },
  {
   "Name": "Manifold (Relay)",
   "BlockCount": "1046 (2.08%)",
   "UniqueBuilder": 2,
   "AverageReward": "0.06730583 ETH",
   "HighestReward": "6.39205779 ETH (Slot 4904444)",
   "OverallRewards": "70.40189766 ETH",
   "Uncensored": "Yes",
   "Unfiltered": "Yes"
  },
  {
   "Name": "BloXroute [Regulated] (Relay)",
   "BlockCount": "456 (0.90%)",
   "UniqueBuilder": 3,
   "AverageReward": "0.08393644 ETH",
   "HighestReward": "4.8364185 ETH (Slot 4905241)",
   "OverallRewards": "38.27501748 ETH",
   "Uncensored": "No",
   "Unfiltered": "Yes"
  }
 ]
  
  function TableRelayer7d() {
    return (
      <div>
        <h2>Data by https://beaconcha.in/</h2>
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
                <td>{val.Name}</td>
                <td>{val.BlockCount}</td>
                <td>{val.AverageReward}</td>
                <td>{val.OverallRewards}</td>
              </tr>
            )
          })}
        </table>
        </div>
    );
  }
    
  export default TableRelayer7d;