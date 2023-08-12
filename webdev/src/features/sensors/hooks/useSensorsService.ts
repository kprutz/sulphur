import { useCallback } from 'react'

import { sensorsActions, selectSensors, selectComplaints } from 'features/sensors/store'
import { Sensors, Complaint } from 'features/sensors/types'
import { useAppDispatch, useAppSelector } from 'store/hooks'

export type SensorsServiceOperators = {
  sensors: Sensors
  complaints: Complaint[]
  fetchAllSensors: (ids: number[]) => void
  runCronJob: () => void
  listComplaints: () => void
}


export const useSensorsService = (): Readonly<SensorsServiceOperators> => {
  const dispatch = useAppDispatch()

  return {
    sensors: useAppSelector(selectSensors),
    complaints: useAppSelector(selectComplaints),

    fetchAllSensors: useCallback((ids) => {
      dispatch(sensorsActions.fetchAll(ids))
    }, [dispatch]),

    runCronJob: useCallback(() => {
      dispatch(sensorsActions.runCronJob())
    }, [dispatch]),


    listComplaints: useCallback(() => {
      dispatch(sensorsActions.listComplaints())
    }, [dispatch]),
  }
}

export default useSensorsService
