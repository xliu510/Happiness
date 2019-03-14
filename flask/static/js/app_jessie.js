//Build Chart
function buildCharts() {

    // @TODO: Use `d3.json` to fetch the sample happiness for the plots
    var url = '/region/happiness';
    console.log("Url", url);
      // @TODO: Build a Bubble Chart using the sample happiness
      d3.json(url).then(function(happiness) { 
        console.log("happiness", happiness);
        //let happinessArray = happiness.happiness.map( each => 10 * each);
        let happinessRegionColor = happiness.region.map( (each, index) => index)

        // var trace = [{
        // x: happiness.work,
        // y: happiness.life,
        // text: happiness.region,
        // hovertext: happiness.happiness,
        // name:happiness.region,
        // mode: 'markers',
        // marker: {
        //   size: happinessArray,
        //   color: happinessRegionColor,
        // }
        // }];


        let happinessScale = d3.scaleLinear()
          .domain(happiness.happiness)
          .range([115,50]);

        let traces = [];
        happiness.work.forEach( (each, index) => {

          traces.push({
            x: [happiness.work[index]],
            y: [happiness.life[index]],
            text:happiness.region[index],
            name:happiness.region[index],
            mode: 'markers',
            marker: {
              size: happinessScale(happiness.happiness[index]),
              color: happinessRegionColor[index]
            },
          });
        });
        console.log(traces);
        //var happiness = [trace];
        var layout2 = {
          title: "Life Expectancy&Work Hour vs Happiness",
          showlegend: true,
          xaxis: {
            title: {
              text: 'Work Hour',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            },
          },
          yaxis: {
            title: {
              text: 'Life Expectancy',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          }
        };
        Plotly.newPlot("bubble", traces, layout2);
      })
  }
buildCharts();


