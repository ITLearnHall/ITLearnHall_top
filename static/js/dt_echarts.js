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
    //将此封装成一个方法
    // $.post("/top",function (data) {
    //     option.xAxis.data=data.x;
    //     option.series[0].data=data.y;
    //     myChart.setOption(option, true);
    //
    // });
    dt_test();
    function dt_test() {
        $.post("/dt/top",function (data) {
        option.xAxis.data=data.x;
        option.series[0].data=data.y;
        myChart.setOption(option, true);
        //1000一秒刷新
        setTimeout(dt_test,1000)
    });
    }



    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    };

}

