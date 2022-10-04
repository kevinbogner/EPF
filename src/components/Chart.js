import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine,
  ResponsiveContainer,
} from 'recharts';

const Chart = () => {

    const data = [
        {
          name: 'Epoch 151175',
          Prysm: 13,
          Lighthouse: 13,
          Teku: 4,
          Nimbus: 1,
          Lodestar: 0,
        },
        {
          name: 'Epoch 151176',
          Prysm: 19,
          Lighthouse: 9,
          Teku: 4,
          Nimbus: 0,
          Lodestar: 0,
        },
        {
          name: 'Epoch 151177',
          Prysm: 11,
          Lighthouse: 13,
          Teku: 7,
          Nimbus: 1,
          Lodestar: 0,
        },
        {
          name: 'Epoch 151178',
          Prysm: 11,
          Lighthouse: 11,
          Teku: 8,
          Nimbus: 2,
          Lodestar: 0,
        },
        {
          name: 'Epoch 151179',
          Prysm: 8,
          Lighthouse: 17,
          Teku: 6,
          Nimbus: 0,
          Lodestar: 0,
        },
        {
          name: 'Epoche 151180',
          Prysm: 15,
          Lighthouse: 5,
          Teku: 9,
          Nimbus: 2,
          Lodestar: 0,
        },
        {
          name: 'Epoche 151181',
          Prysm: 13,
          Lighthouse: 11,
          Teku: 7,
          Nimbus: 1,
          Lodestar: 0,
        },
      ];

    return (
        <ResponsiveContainer width={'99%'} height={500}>
        <LineChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 20,
            right: 50,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <ReferenceLine x="Epoche 151180" stroke="red" label="Event" />
          <Line type="monotone" dataKey="Prysm" stroke="#72FBFD" />
          <Line type="monotone" dataKey="Lighthouse" stroke="#262626" />
          <Line type="monotone" dataKey="Teku" stroke="#2C56DD" />
          <Line type="monotone" dataKey="Nimbus" stroke="#FF9C00" />
          <Line type="monotone" dataKey="Lodestar" stroke="#6873D1" />
        </LineChart>
        </ResponsiveContainer>
    )
}

export default Chart;