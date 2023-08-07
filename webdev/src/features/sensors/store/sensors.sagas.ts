/** connect dispatched action IDs to action methods */
import { SagaIterator } from '@redux-saga/core'
import { call, put, takeEvery } from 'redux-saga/effects'

import { getCronMetadata, getSensorsData, runCronJob } from 'features/sensors/api'
import { sensorsActions } from 'features/sensors/store/sensors.slice'
import { CronMetadata, Sensors } from 'features/sensors/types'

type AnyAction = {type: string, [key: string]: any}


// Worker Sagas
export function* onGetSensorsData(action: AnyAction): SagaIterator {
  const sensors: Sensors = yield call(getSensorsData, action.payload)
  yield put(sensorsActions.fetchAllSucceeded(sensors))
}

export function* onGetCronMetadata(action: AnyAction): SagaIterator {
  const metadata: CronMetadata = yield call(getCronMetadata)
  yield put(sensorsActions.fetchCronMetadataSucceeded(metadata))
}

export function* onRunCronJob(): SagaIterator {
  yield call(runCronJob)
}

// Watcher Saga
export function* sensorsWatcherSaga(): SagaIterator {
  yield takeEvery(sensorsActions.fetchAll.type, onGetSensorsData)
  yield takeEvery(sensorsActions.fetchCronMetadata.type, onGetCronMetadata)
  yield takeEvery(sensorsActions.runCronJob.type, onRunCronJob)
}

export default sensorsWatcherSaga
