import Container from '@mui/material/Container'
import React, { useEffect } from 'react'

import { SensorData } from 'features/sensors/types'
import { LineChartDatasetTransition } from "d3utils/LineChartDatasetTransition";
import { Datapoint } from "d3utils/LineChart";


export type GraphProps = {
  data: SensorData[]
}

export const Graph = (props: GraphProps) => {
  return (
    <>
      <LineChartDatasetTransition
        width={800}
        height={300}
        data={props.data.map(d => ({x: d.timestamp, y: d.pm25_aqi}) as Datapoint)}
        isDate={true} />
    </>
  )
}
