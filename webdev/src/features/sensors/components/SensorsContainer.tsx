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
  const { sensors, complaints, fetchAllSensors, runCronJob, listComplaints } = useSensorsService()

  useEffect(() => {
    fetchAllSensors(SENSOR_IDS),
    listComplaints()
  }, [fetchAllSensors, listComplaints])

  const sensor = sensors[SENSOR_IDS[0]] ?? []
  const {data} = sensor

  const renderComplaints = () => (
    <table>
      <tr>
        <th>Sensor index</th>
        <th>Date filed</th>
        <th>Was filed from a manual run?</th>
        <th>Submission Data</th>
      </tr>
      {complaints.map(c => (
        <tr>
          <td>{c.sensorIndex}</td>
          <td>{c.fileDate}</td>
          <td>{c.isManualRun}</td>
          <td>{c.submissionData}</td>
        </tr>
      ))}
    </table>
  )

  return (
    <>
      <Container>
        <div><h2>Purple Air - PM2.5 for the last week</h2></div>
        {!!Object.keys(sensors).length && <Graph data={data} />}
      </Container>
      <Container>
        <h2>Auto-complainer</h2>
        <h3>Last complainer run:</h3>
        {sensor.lastComplainerRun  && <div>{new Date(sensor.lastComplainerRun).toLocaleDateString()} --- {new Date(sensor.lastComplainerRun).toTimeString()}</div>}
        <button onClick={runCronJob}>Run cron job</button>
        <div>
          <h3>Complaints: </h3>
          {renderComplaints()}
        </div>
      </Container>
    </>
  )
}
