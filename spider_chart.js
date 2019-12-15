let raw_data = d3.js('spider_chart_data.csv')
let data = raw_data.slice(0)
let features = data[0]

let svg = d3.select("body").append("svg").attr("width", 600).attr("height", 600);

let radialScale = d3.scaleLinear().domain([0,10]).range([0,250]);

let ticks = [2,4,6,8,10];

ticks.forEach(t =>
    svg.append("circle")
    .attr("cx", 300)
    .attr("cy", 300)
    .attr("fill", "none")
    .attr("stroke", "gray")
    .attr("r", radialScale(t))
);
