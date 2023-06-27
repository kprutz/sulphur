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
  const { sensors, fetchAllSensors } = useSensorsService()

  useEffect(() => {
    fetchAllSensors(SENSOR_IDS)
  }, [fetchAllSensors])
  return (
    <>
      <Container maxWidth="xs">
        {!!Object.keys(sensors).length && <Graph data={sensors[SENSOR_IDS[0]]} />}
      </Container>
    </>
  )
}
