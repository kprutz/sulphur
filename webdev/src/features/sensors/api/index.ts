import { Env } from 'config/Env'
import { Complaint, Sensor } from 'features/sensors/types'
import makeApi from "libs/core/configureAxios";

const prod_address = "" // "http://50.17.131.74"
const api = makeApi(prod_address || "http://localhost:8000");

const SENSORS_BASE_URL = `/sensors/purple`
const COMPLAINTS_URL = `/api/complaints`

export const getSensorsData = (ids: number[]): Promise<Sensor[]> => {
  return api.get(SENSORS_BASE_URL, {params: {ids: ids.join(',')}})
}

export const listComplaints = (): Promise<Complaint[]> => {
  return api.get(COMPLAINTS_URL)
}

export const runCronJob = (): Promise<void> => {
  return api.post(`/runcron`)
}