//Build Chart
function buildCharts() {

    // @TODO: Use `d3.json` to fetch the sample happiness for the plots
    var url = '/region/happiness';
    console.log("Url", url);
      // @TODO: Build a Bubble Chart using the sample happiness
      d3.json(url).then(function(happiness) { 
      console.log("happiness", happiness);
        
        var trace = [{
        x: happiness.work,
        y: happiness.life,
        text: happiness.region,
        mode: 'markers',
        marker: {
          size: happiness.happiness,
          color: happiness.work,
        }
        }];

        //var happiness = [trace];
        var layout2 = {
          title: "Life vs Happiness",
          showlegend: false
        };
        Plotly.newPlot("bubble", trace, layout2);
      })
  }
buildCharts();


