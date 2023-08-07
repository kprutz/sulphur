import { useCallback } from 'react'

import { sensorsActions, selectSensors, selectCronMetadata } from 'features/sensors/store'
import { Sensors, CronMetadata } from 'features/sensors/types'
import { useAppDispatch, useAppSelector } from 'store/hooks'

export type SensorsServiceOperators = {
  sensors: Sensors
  cronMetadata: CronMetadata
  fetchAllSensors: (ids: number[]) => void
  runCronJob: () => void
  fetchCronMetadata: () => void
}


export const useSensorsService = (): Readonly<SensorsServiceOperators> => {
  const dispatch = useAppDispatch()

  return {
    sensors: useAppSelector(selectSensors),
    cronMetadata: useAppSelector(selectCronMetadata),

    fetchAllSensors: useCallback((ids) => {
      dispatch(sensorsActions.fetchAll(ids))
    }, [dispatch]),

    runCronJob: useCallback(() => {
      dispatch(sensorsActions.runCronJob())
    }, [dispatch]),


    fetchCronMetadata: useCallback(() => {
      dispatch(sensorsActions.fetchCronMetadata())
    }, [dispatch]),
  }
}

export default useSensorsService
