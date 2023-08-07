// DUCKS pattern
import { createAction, createSlice, nanoid, PayloadAction } from '@reduxjs/toolkit'

import { CronMetadata, Sensors } from 'features/sensors/types'
import type { RootState } from 'store/store'

export interface SensorsState {
  sensors: Sensors
  cronMetadata: CronMetadata
}

const initialState: SensorsState = {
  sensors: [],
  cronMetadata: {lastComplainerRun: ''}
}

// slice
export const sensorsSlice = createSlice({
  name: 'sensors',
  initialState,
  reducers: {
    fetchAllSucceeded(state, action: PayloadAction<Sensors>) {
      state.sensors = action.payload
    },
    fetchCronMetadataSucceeded(state, action: PayloadAction<CronMetadata>) {
      state.cronMetadata = action.payload
    },
  },
})

// Actions
export const sensorsActions = {
  fetchAll: createAction<number[]>(`${sensorsSlice.name}/fetchAll`),
  fetchAllSucceeded: sensorsSlice.actions.fetchAllSucceeded,
  runCronJob: createAction(`${sensorsSlice.name}/runcron`),
  fetchCronMetadata: createAction(`${sensorsSlice.name}/cronmetadata`),
  fetchCronMetadataSucceeded: sensorsSlice.actions.fetchCronMetadataSucceeded,
}

// Selectors
export const selectSensors = (state: RootState) => state.sensors.sensors

export const selectCronMetadata = (state: RootState) => state.sensors.cronMetadata

// Reducer
export default sensorsSlice.reducer
