import { all, fork } from 'redux-saga/effects'

import { postsWatcherSaga } from 'features/posts/store/posts.sagas'
import { sensorsWatcherSaga } from 'features/sensors/store/sensors.sagas'

export function* rootSaga() {
  yield all([fork(postsWatcherSaga)])
  yield all([fork(sensorsWatcherSaga)])
}

export default rootSaga
