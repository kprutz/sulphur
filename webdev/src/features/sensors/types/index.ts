export type Sensor = {
  id: string
  data: SensorData[]
  lastComplainerRun: string  // datetime, e.g. "2023-07-28T19:54:22Z"
}

export type SensorData = {
  timestamp: number
  pm25: number
  pm25_aqi: number
}

export type Sensors = {
  [id: number]: Sensor;
}

export type Complaint = {
  sensorIndex: number
  submissionData: string  // JSON
  fileDate: string
  isManualRun: boolean
}