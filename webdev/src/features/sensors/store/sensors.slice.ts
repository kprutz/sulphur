// DUCKS pattern
import { createAction, createSlice, nanoid, PayloadAction } from '@reduxjs/toolkit'

import { Complaint, Sensors } from 'features/sensors/types'
import type { RootState } from 'store/store'

export interface SensorsState {
  sensors: Sensors
  complaints: Complaint[]
}

const initialState: SensorsState = {
  sensors: [],
  complaints: []
}

// slice
export const sensorsSlice = createSlice({
  name: 'sensors',
  initialState,
  reducers: {
    fetchAllSucceeded(state, action: PayloadAction<Sensors>) {
      state.sensors = action.payload
    },
    listComplaintsSucceeded(state, action: PayloadAction<Complaint[]>) {
      state.complaints = action.payload
    },
  },
})

// Actions
export const sensorsActions = {
  fetchAll: createAction<number[]>(`${sensorsSlice.name}/fetchAll`),
  fetchAllSucceeded: sensorsSlice.actions.fetchAllSucceeded,
  runCronJob: createAction(`${sensorsSlice.name}/runcron`),
  listComplaints: createAction(`${sensorsSlice.name}/complaints`),
  listComplaintsSucceeded: sensorsSlice.actions.listComplaintsSucceeded,
}

// Selectors
export const selectSensors = (state: RootState) => state.sensors.sensors

export const selectComplaints = (state: RootState) => state.sensors.complaints

// Reducer
export default sensorsSlice.reducer
