import { Env } from 'config/Env'
import { CronMetadata, Sensor } from 'features/sensors/types'
import makeApi from "libs/core/configureAxios";

const api = makeApi("http://localhost:8000");

const SENSORS_BASE_URL = `/sensors`
const CRON_METADATA_URL = `/sensors/cronmetadata`

export const getSensorsData = (ids: number[]): Promise<Sensor[]> => {
  return api.get(SENSORS_BASE_URL, {params: {ids: ids.join(',')}})
}

export const getCronMetadata = (): Promise<CronMetadata> => {
  return api.get(CRON_METADATA_URL)
}

export const runCronJob = (): Promise<void> => {
  return api.post(`/runcron`)
}