test();
function test() {
    var myChart = echarts.init(document.getElementById("container"));
    option = {
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [],
            type: 'line',
            areaStyle: {}
        }]
    };
    $.post("/top",function (data) {
        option.xAxis.data=data.x;
        option.series[0].data=data.y;
        myChart.setOption(option, true);

    });


    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    };

}

