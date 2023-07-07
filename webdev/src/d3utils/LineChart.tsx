import { useEffect, useMemo, useRef } from "react";
import * as d3 from "d3";
import { useSpring, animated } from "@react-spring/web";

const MARGIN = { top: 30, right: 30, bottom: 50, left: 50 };

export type Datapoint = { x: number; y: number };

type LineChartProps = {
  width: number;
  height: number;
  data: Datapoint[];
  isDate: boolean;
};

export const LineChart = ({
  width,
  height,
  data,
  isDate,
}: LineChartProps) => {
  const axesRef = useRef(null);
  const boundsWidth = width - MARGIN.right - MARGIN.left;
  const boundsHeight = height - MARGIN.top - MARGIN.bottom;

  const yScale = useMemo(() => {
    return d3.scaleLinear().domain([0, 100]).range([boundsHeight, 0]);
  }, [data, height]);

  const xScale = useMemo(() => {
    if(isDate) {
      return d3.scaleTime()  
        .domain([
          new Date(data[0].x * 1000),
          new Date(data[data.length-1].x * 1000)])
        .range([ 0, boundsWidth ]);
    }
    return d3.scaleLinear()
      .domain([data[0].x, data[data.length-1].x])
      .range([0, boundsWidth]);
  }, [data, width]);

  // Render the X and Y axis using d3.js, not react
  useEffect(() => {
    const svgElement = d3.select(axesRef.current);
    svgElement.selectAll("*").remove();

    let xAxisGenerator = d3.axisBottom(xScale);
    svgElement
      .append("g")
      .attr("transform", "translate(0," + boundsHeight + ")")
      .call(xAxisGenerator);

    const yAxisGenerator = d3.axisLeft(yScale);
    svgElement.append("g").call(yAxisGenerator);
  }, [xScale, yScale, boundsHeight]);

  const lineBuilder = d3
    .line<Datapoint>()
    .x((d) => isDate ? xScale(new Date(d.x * 1000)) : xScale(d.x))
    .y((d) => yScale(d.y));
  const linePath = lineBuilder(data);

  if (!linePath) {
    return null;
  }

  return (
    <div>
      <svg width={width} height={height}>
        {/* first group is lines */}
        <g
          width={boundsWidth}
          height={boundsHeight}
          transform={`translate(${[MARGIN.left, MARGIN.top].join(",")})`}
        >
          <LineItem
            path={linePath}
            color={"#69b3a2"}
          />
        </g>
        {/* Second is for the axes */}
        <g
          width={boundsWidth}
          height={boundsHeight}
          ref={axesRef}
          transform={`translate(${[MARGIN.left, MARGIN.top].join(",")})`}
        />
      </svg>
    </div>
  );
};

type LineItemProps = {
  path: string;
  color: string;
};

const LineItem = ({ path, color }: LineItemProps) => {
  const springProps = useSpring({
    to: {
      path,
      color,
    },
    config: {
      friction: 100,
    },
  });

  return (
    <animated.path
      d={springProps.path}
      fill={"none"}
      stroke={color}
      strokeWidth={2}
    />
  );
};
