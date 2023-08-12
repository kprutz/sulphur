/** connect dispatched action IDs to action methods */
import { SagaIterator } from '@redux-saga/core'
import { call, put, takeEvery } from 'redux-saga/effects'

import { listComplaints, getSensorsData, runCronJob } from 'features/sensors/api'
import { sensorsActions } from 'features/sensors/store/sensors.slice'
import { Complaint, Sensors } from 'features/sensors/types'

type AnyAction = {type: string, [key: string]: any}


// Worker Sagas
export function* onGetSensorsData(action: AnyAction): SagaIterator {
  const sensors: Sensors = yield call(getSensorsData, action.payload)
  yield put(sensorsActions.fetchAllSucceeded(sensors))
}

export function* onListComplaints(action: AnyAction): SagaIterator {
  const complaints: Complaint[] = yield call(listComplaints)
  yield put(sensorsActions.listComplaintsSucceeded(complaints))
}

export function* onRunCronJob(): SagaIterator {
  yield call(runCronJob)
}

// Watcher Saga
export function* sensorsWatcherSaga(): SagaIterator {
  yield takeEvery(sensorsActions.fetchAll.type, onGetSensorsData)
  yield takeEvery(sensorsActions.listComplaints.type, onListComplaints)
  yield takeEvery(sensorsActions.runCronJob.type, onRunCronJob)
}

export default sensorsWatcherSaga
