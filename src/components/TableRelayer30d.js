const data = [
  {
   "Name": "Flashbots (Relay)",
   "BlockCount": "70207 (31.45%)",
   "UniqueBuilder": 30,
   "AverageReward": "0.14562849 ETH",
   "HighestReward": "81.00241977 ETH (Slot 4903350)",
   "OverallRewards": "10,224.139708 ETH",
   "Uncensored": "No",
   "Unfiltered": "Yes"
  },
  {
   "Name": "BloXroute [Max-Profit] (Relay)",
   "BlockCount": "6648 (2.98%)",
   "UniqueBuilder": 4,
   "AverageReward": "0.10346615 ETH",
   "HighestReward": "13.52927684 ETH (Slot 4903353)",
   "OverallRewards": "687.84293725 ETH",
   "Uncensored": "Yes",
   "Unfiltered": "Yes"
  },
  {
   "Name": "BloXroute [Ethical] (Relay)",
   "BlockCount": "2354 (1.05%)",
   "UniqueBuilder": 3,
   "AverageReward": "0.08434942 ETH",
   "HighestReward": "10.32511803 ETH (Slot 4791729)",
   "OverallRewards": "198.55854547 ETH",
   "Uncensored": "Yes",
   "Unfiltered": "No"
  },
  {
   "Name": "Blocknative (Relay)",
   "BlockCount": "2140 (0.96%)",
   "UniqueBuilder": 2,
   "AverageReward": "0.08150232 ETH",
   "HighestReward": "16.52316402 ETH (Slot 4905606)",
   "OverallRewards": "174.41495783 ETH",
   "Uncensored": "No",
   "Unfiltered": "???"
  },
  {
   "Name": "Manifold (Relay)",
   "BlockCount": "1771 (0.79%)",
   "UniqueBuilder": 2,
   "AverageReward": "0.09246619 ETH",
   "HighestReward": "31.9242307 ETH (Slot 4738717)",
   "OverallRewards": "163.75762499 ETH",
   "Uncensored": "Yes",
   "Unfiltered": "Yes"
  },
  {
   "Name": "Eden Network (Relay)",
   "BlockCount": "1569 (0.70%)",
   "UniqueBuilder": 3,
   "AverageReward": "0.31571037 ETH",
   "HighestReward": "278.29152063 ETH (Slot 4867314)",
   "OverallRewards": "495.34957287 ETH",
   "Uncensored": "No",
   "Unfiltered": "???"
  },
  {
   "Name": "BloXroute [Regulated] (Relay)",
   "BlockCount": "1502 (0.67%)",
   "UniqueBuilder": 4,
   "AverageReward": "0.12036883 ETH",
   "HighestReward": "13.6623918 ETH (Slot 4792331)",
   "OverallRewards": "180.79398273 ETH",
   "Uncensored": "No",
   "Unfiltered": "Yes"
  }
 ]
  
  function TableRelayer30d() {
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
    
  export default TableRelayer30d;