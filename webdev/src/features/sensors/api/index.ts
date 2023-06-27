import { Env } from 'config/Env'
import { Sensor } from 'features/sensors/types'
import makeApi from "libs/core/configureAxios";

const api = makeApi("http://localhost:8000");

const SENSORS_BASE_URL = `/sensors`

export const getSensorsData = (ids: number[]): Promise<Sensor[]> => {
  return api.get(SENSORS_BASE_URL, {params: {ids: ids.join(',')}})
}
