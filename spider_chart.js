let data = {
    'Computer Vision ND': [7,5,0,6,0],
    'Deep Reinforcement Learning ND': [8,0,0,6,7],
    'Deep Learning ND': [8,0,4,6,0]
}
let features = ['PyTorch', 'OpenCV', 'AWS', 'LSTM', 'Deep Q-Network'];

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

function angleToCoordinate(angle, value){
    let x = Math.cos(angle) * radialScale(value);
    let y = Math.sin(angle) * radialScale(value);
    return {"x": 300 + x, "y": 300 - y};
}
