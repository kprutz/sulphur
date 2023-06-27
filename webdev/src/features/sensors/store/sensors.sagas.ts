/** connect dispatched action IDs to action methods */
import { SagaIterator } from '@redux-saga/core'
import { call, put, takeEvery } from 'redux-saga/effects'

import { getSensorsData } from 'features/sensors/api'
import { sensorsActions } from 'features/sensors/store/sensors.slice'
import { Sensors } from 'features/sensors/types'

type AnyAction = {type: string, [key: string]: any}


// Worker Sagas
export function* onGetSensorsData(action: AnyAction): SagaIterator {
  const sensors: Sensors = yield call(getSensorsData, action.payload)
  yield put(sensorsActions.fetchAllSucceeded(sensors))
}

// Watcher Saga
export function* sensorsWatcherSaga(): SagaIterator {
  yield takeEvery(sensorsActions.fetchAll.type, onGetSensorsData)
}

export default sensorsWatcherSaga
