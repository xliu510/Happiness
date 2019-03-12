    
function createBarplot(route, divider, outerColor){


        // d3.csv(route, function (data) {
        d3.json(route, function (error, data) {


            // set the dimensions and margins of the graph
            var margin = { top: 50, right: 0, bottom: 0, left: 0 },
            width = 800 - margin.left - margin.right,
            height = 800 - margin.top - margin.bottom,
            innerRadius = 150,
            outerRadius = (Math.min(width, height)-200) / 2;   // the outerRadius goes from the middle of the SVG area to the border


            //Remove whatever chart with the same id/class was present before
            d3.select("#my_dataviz").select("svg").remove();

            // append the svg object
            var svg = d3.select("#my_dataviz")
                    .append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                    .append("g")
                    .attr("transform", "translate(" + (width / 2 + margin.left) + "," + (height / 2 + margin.top) + ")");

            // data = data_load[0]
            //find max avg_happiness for y
            console.log(d3.max(data, function(d) { return d.Happiness_Score_2015}))
            console.log(d3.max(data, function(d) { return d.Second_Feature/divider}))
            console.log(route)
            console.log(data)
            console.log(d3.extent(data, function(d) { return d.Second_Feature; }))

            max_happiness = d3.max(data, function(d) { return d.Happiness_Score_2015})
            max_feature = d3.max(data, function(d) { return d.Second_Feature/divider})
            

            // X scale: common for 2 data series
            var x = d3.scaleBand()
                .range([0, 2 * Math.PI])    // X axis goes from 0 to 2pi = all around the circle. If I stop at 1Pi, it will be around a half circle
                .align(0)                  // This does nothing
                .domain(data.map(function (d) { return d.Country; })); // The domain of the X axis is the list of states.

            // Y scale outer variable
            var y = d3.scaleRadial()
                .range([innerRadius, outerRadius])   // Domain will be define later.
                .domain([0, max_feature]); // Domain of Y is from 0 to the max seen in the data

            // Second barplot Scales
            var ybis = d3.scaleRadial()
                .range([innerRadius, 5])   // Domain will be defined later.
                .domain([0, max_happiness]); 
                // .domain([0, max_happiness]);

            // Add the bars
            svg.append("g")
                .selectAll("path")
                .data(data)
                .enter()
                .append("path")
                .attr("fill", outerColor)
                .attr("class", "yo")
                .attr("d", d3.arc()     // imagine your doing a part of a donut plot
                    .innerRadius(innerRadius)
                    .outerRadius(function (d) { return y(d.Second_Feature/divider); })
                    .startAngle(function (d) { return x(d.Country); })
                    .endAngle(function (d) { return x(d.Country) + x.bandwidth(); })
                    .padAngle(0.01)
                    .padRadius(innerRadius))

            // Add the labels
            svg.append("g")
                .selectAll("g")
                .data(data)
                .enter()
                .append("g")
                .attr("text-anchor", function (d) { return (x(d.Country) + x.bandwidth()/2 + Math.PI) % (2 * Math.PI) < Math.PI ? "end" : "start"; })
                .attr("transform", function (d) { return "rotate(" + ((x(d.Country) + x.bandwidth() / 2) * 180 / Math.PI - 90) + ")" + "translate(" + (y(d.Second_Feature/divider) + 10) + ",0)"; })
                .append("text")
                .text(function (d) { return (d.Country) })
                .attr("transform", function (d) { return (x(d.Country) + x.bandwidth()/2 + Math.PI) % (2 * Math.PI) < Math.PI ? "rotate(180)" : "rotate(0)"; })
                .style("font-size", "11px")
                .attr("alignment-baseline", "middle")

            // Add the second serie
            svg.append("g")
                .selectAll("path")
                .data(data)
                .enter()
                .append("path")
                .attr("fill", "#FFCF50")
                .attr("d", d3.arc()     // imagine your doing a part of a donut plot
                    .innerRadius(function (d) { return ybis(0) })
                    .outerRadius(function (d) { return ybis(d.Happiness_Score_2015); })
                    .startAngle(function (d) { return x(d.Country); })
                    .endAngle(function (d) { return x(d.Country) + x.bandwidth(); })
                    .padAngle(0.01)
                    .padRadius(innerRadius))

        })
    }

    function updateBarplot(){

        update_feature = this.value
        
        console.log("this updates: "+ update_feature)
        update_route = `/barplot/${update_feature}`
        divider = 1
        color = ""
        
        if (update_feature == 'adultmortality') {
            divider = 10
            color = "#ABCAE0"
        } else if (update_feature == 'lifeexpectancy') {
            divder = 14
            color = "#99D7C0"
        } else if (update_feature == 'gdp') {
            divider = 0.5
            color = "#E3B2C3"
        } else if (update_feature == 'family'){
            divider = 0.5
            color = "#B2E3DB"
        } else if (update_feature == 'health'){
            divider = 0.7
            color = "#E3B2B2"
        } else if (update_feature == 'freedom'){
            divider = 0.2
            color = "#B2BBE3"
        } else if (update_feature == 'income') {
            divider = 0.2
            color = "#AEBFC8"
        }

        createBarplot(update_route, divider, color)
    }

    function init(){
        
        console.log("this is init()")
        temp = this.value
        flask_route = "/barplot/adultmortality"

        createBarplot(flask_route, 12, "#ABCAE0")
    }

    init()


    d3.select('#feature_selection').on('change', updateBarplot)