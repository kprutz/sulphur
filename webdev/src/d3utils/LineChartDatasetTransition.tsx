import { useState } from "react";
import { LineChart, Datapoint } from "./LineChart";

const BUTTONS_HEIGHT = 50;

type LineChartDatasetTransitionProps = {
  width: number;
  height: number;
  data: Datapoint[];
  isDate: boolean;
};

const buttonStyle = {
  border: "1px solid #9a6fb0",
  borderRadius: "3px",
  padding: "4px 8px",
  margin: "10px 2px",
  fontSize: 14,
  color: "#9a6fb0",
  opacity: 0.7,
};

export const LineChartDatasetTransition = ({
  width,
  height,
  data,
  isDate,
}: LineChartDatasetTransitionProps) => {
  // const [selectedGroup, setSelectedGroup] = useState<"melanie" | "yan">(
  //   "melanie"
  // );

  return (
    <div>
      <LineChart
        width={width}
        height={height - BUTTONS_HEIGHT}
        data={data}
        isDate={isDate}
      />
    </div>
  );
};
