import { useCallback } from 'react'

import { sensorsActions, selectSensors } from 'features/sensors/store'
import { Sensors } from 'features/sensors/types'
import { useAppDispatch, useAppSelector } from 'store/hooks'

export type SensorsServiceOperators = {
  sensors: Sensors
  fetchAllSensors: (ids: number[]) => void
}


export const useSensorsService = (): Readonly<SensorsServiceOperators> => {
  const dispatch = useAppDispatch()

  return {
    sensors: useAppSelector(selectSensors),

    fetchAllSensors: useCallback((ids) => {
      dispatch(sensorsActions.fetchAll(ids))
    }, [dispatch]),
  }
}

export default useSensorsService
