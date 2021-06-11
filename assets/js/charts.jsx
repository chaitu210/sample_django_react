import React from 'react';
import {Bar} from 'react-chartjs-2';

const state = {

  labels: ['January', 'February', 'March',
           'April', 'May'],
  datasets: [
    {
      label: 'Rainfall',
      fill: false,
      borderColor: 'red',
      borderWidth: 2,
      data: [65, 59, 80, 81, 56]
    }
  ]
}

export default class App extends React.Component {
  render() {
    return (
      <div className="chart">
        <Bar
          data={{

            labels: ['January', 'February', 'March',
                     'April', 'May'],
            datasets: [
              {
                label: 'Rainfall',
                fill: false,
                borderColor: 'red',
                borderWidth: 2,
                data: [65, 59, 80, 81, 56]
              }
            ]
          }}
          type={'Bar'}
          height={400}
          width={400}
          options={{
            title:{
              display:true,
              text:'Average Rainfall per month',
              fontSize:20
            },
            legend:{
              display:true,
              position:'right'
            }
          }}
        />
      </div>
    );
  }
}