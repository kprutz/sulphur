import Container from '@mui/material/Container'
import React, { useEffect } from 'react'

import { Graph } from 'features/sensors/components/Graph'
import { useSensorsService } from 'features/sensors/hooks/useSensorsService'


const SENSOR_IDS = [145788]
// SENSOR_IDS = [
//     {index: 145800, purple_name: "Westlake", name: ""},
//     {index: 38421, purple_name: "Westlake, Louisiana", name: ""},
//     {index: 30131, purple_name: "Margaret Place, Lake Charles, Louisiana", name: ""},
//     {index: 174173, purple_name: "Beauregard Ave Sulphur", name: ""},
//     {index: 145788, purple_name: "624 W. Verdine, Sulphur", name: ""},
// ]

export const SensorsContainer = () => {
  const { sensors, cronMetadata, fetchAllSensors, runCronJob, fetchCronMetadata } = useSensorsService()

  useEffect(() => {
    fetchAllSensors(SENSOR_IDS),
    fetchCronMetadata()
  }, [fetchAllSensors, fetchCronMetadata])

  const data = sensors[SENSOR_IDS[0]] ?? []

  return (
    <>
      <Container>
        <div><h2>Purple Air - PM2.5 for the last week</h2></div>
        {!!Object.keys(sensors).length && <Graph data={data} />}
      </Container>
      <Container>
        <div><h2>Auto-complainer</h2></div>
        <button onClick={runCronJob}>Run cron job</button>
        <div><h3>Last cron job run: </h3><span>{cronMetadata.lastComplainerRun}</span></div>
      </Container>
    </>
  )
}
