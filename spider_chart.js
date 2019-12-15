let data = {
    'Computer Vision ND': [7,5,0,6,0],
    'Deep Reinforcement Learning ND': [8,0,0,6,7],
    'Deep Learning ND': [8,0,4,6,0]
}
let features = ['PyTorch', 'OpenCV', 'AWS', 'LSTM', 'Deep Q-Network'];

let svg = d3.selectAll(".spider_chart").append("svg").attr("width", 600).attr("height", 600);

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

function angleToCoordinate(angle, value){
    let x = Math.cos(angle) * radialScale(value);
    let y = Math.sin(angle) * radialScale(value);
    return {"x": 300 + x, "y": 300 - y};
}

for (let i = 0; i < features.length; i++) {
    let ft_name = features[i];
    let angle = (Math.PI / 2) + (2 * Math.PI * i / features.length);
    let line_coordinate = angleToCoordinate(angle, 10);
    let label_coordinate = angleToCoordinate(angle, 10.5);

    //draw axis line
    svg.append("line")
    .attr("x1", 300)
    .attr("y1", 300)
    .attr("x2", line_coordinate.x)
    .attr("y2", line_coordinate.y)
    .attr("stroke","black");

    //draw axis label
    svg.append("text")
    .attr("x", label_coordinate.x)
    .attr("y", label_coordinate.y)
    .text(ft_name);
}

let line = d3.line()
    .x(d => d.x)
    .y(d => d.y);
let colors = ["darkorange", "gray", "navy"];


function getPathCoordinates(data_point){
    let coordinates = [];
    for (let i = 0; i < features.length; i++){
        let ft_name = features[i];
        let angle = (Math.PI / 2) + (2 * Math.PI * i / features.length);
        coordinates.push(angleToCoordinate(angle, data_point[ft_name]));
    }
    return coordinates;
}


for (let i = 0; i < data.length; i ++){
    let d = data[i];
    let color = colors[i];
    let coordinates = getPathCoordinates(d);

    //draw the path element
    svg.append("path")
    .datum(coordinates)
    .attr("d",line)
    .attr("stroke-width", 3)
    .attr("stroke", color)
    .attr("fill", color)
    .attr("stroke-opacity", 1)
    .attr("opacity", 0.5);
}

