// DUCKS pattern
import { createAction, createSlice, nanoid, PayloadAction } from '@reduxjs/toolkit'

import { Sensors } from 'features/sensors/types'
import type { RootState } from 'store/store'

export interface SensorsState {
  sensors: Sensors
}

const initialState: SensorsState = {
  sensors: [],
}

// slice
export const sensorsSlice = createSlice({
  name: 'sensors',
  initialState,
  reducers: {
    fetchAllSucceeded(state, action: PayloadAction<Sensors>) {
      state.sensors = action.payload
    },
  },
})

// Actions
export const sensorsActions = {
  fetchAll: createAction<number[]>(`${sensorsSlice.name}/fetchAll`),
  fetchAllSucceeded: sensorsSlice.actions.fetchAllSucceeded,
}

// Selectors
export const selectSensors = (state: RootState) => state.sensors.sensors

// Reducer
export default sensorsSlice.reducer
