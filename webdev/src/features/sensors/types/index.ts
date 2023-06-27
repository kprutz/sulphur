export type Sensor = {
  id: string
  title: string
  history: SensorData[]
}

export type SensorData = {
  timestamp: number
  pm25: number
  // TODO: can add other data types here
}
export type Sensors = {
  [id: number]: SensorData[];
}
