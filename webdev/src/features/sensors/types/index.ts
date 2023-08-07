export type Sensor = {
  id: string
  title: string
  history: SensorData[]
}

export type SensorData = {
  timestamp: number
  pm25: number
  pm25_aqi: number
  // TODO: can add other data types here
}

export type Sensors = {
  [id: number]: SensorData[];
}

export type CronMetadata = {
  lastComplainerRun: string  // datetime, e.g. "2023-07-28T19:54:22Z"
  // submissions - date, time, description
}