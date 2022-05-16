const CHART_OPTIONS = {
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position:'left',
            labels:{
                font: {
                    size: 10
                },
                color:'rgba(255, 255, 255, 0.8)',
                boxWidth:10,
                boxHeight:10,
                padding:5,
            }
        }
    },
    scales: {
        y: {
            grid: {
              color: 'rgba(255, 255, 255, 0.4)',
            },
            ticks: {
                color:'white'
            }
        },
        x: {
            grid: {
                color: 'rgba(255, 255, 255, 0.4)',
            },
            ticks: {

                maxTicksLimit: 5,
                color:'rgba(255, 255, 255, 0.8)',
                maxRotation: 0,
                minRotation: 0
            }
        },
    },
}

window.onload = function(){

    updateAll();

    setInterval(() => {
        updateAll();
    },30000)

};

function updateAll(){
    updateDerivativeStatusesTable();
    updateLongShortRatioChart();
    updateIndexPriceKairiChart();
    updateMarkPriceKairiChart();
    updateFundingRateChart();
    updateUpdateTime();
    updatePriceChart();
}

function updateUpdateTime(){
    $('#UpdateTime').html("Last updated: " + getNowDateStr());
}

function updateDerivativeStatusesTable(){
    $.ajax({
        type: 'GET',
        url: '/derivative_statuses_table',
    }).done(function (data) {
        $('#DerivativesSheetTable').html(data);
    })
};

function updatePriceChart(){
    $.ajax({
        type: 'GET',
        url: '/get_price',
    }).done(function (data) {
        console.log(data)
        if (typeof PChart !== 'undefined') {
            PChart.destroy();
        }

        let ctx = document.getElementById('PriceChart').getContext('2d');

        window.PChart = new Chart(ctx, {
            type: 'line',
            data: data,
            options: CHART_OPTIONS
        });
    })
};


function updateFundingRateChart(){
    $.ajax({
        type: 'GET',
        url: '/funding_rate_history',
    }).done(function (data) {

        if (typeof FRChart !== 'undefined') {
            FRChart.destroy();
        }

        let ctx = document.getElementById('FundingRateChart').getContext('2d');

        window.FRChart = new Chart(ctx, {
            type: 'bar',
            data: data,
            options: CHART_OPTIONS
        });

    })
};

function updateIndexPriceKairiChart(){
    $.ajax({
        type: 'GET',
        url: '/index_price_kairi',
    }).done(function (data) {

        if (typeof IPKChart !== 'undefined') {
            IPKChart.destroy();
        }

        let ctx = document.getElementById('IndexPriceKairiChart').getContext('2d');

        window.IPKChart = new Chart(ctx, {
            type: 'bar',
            data:{
                labels:data[0]['indexes'],
                datasets: [
                {
                    label:'Binance BTC/USD',
                    data:data[0]['values'],
                    borderColor: '#ff3737',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Binance BTC/USDT',
                    data:data[1]['values'],
                    borderColor: '#ff8337',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Bybit BTC/USD',
                    data:data[2]['values'],
                    borderColor: '#de6fff',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Bybit BTC/USDT',
                    data:data[3]['values'],
                    borderColor: '#ff74bc',
                    borderWidth: 1,
                    pointRadius: 0,
                }]
            },
            options: CHART_OPTIONS
        });

    })
};

function updateMarkPriceKairiChart(){
    $.ajax({
        type: 'GET',
        url: '/mark_price_kairi',
    }).done(function (data) {

        if (typeof MPKChart !== 'undefined') {
            MPKChart.destroy();
        }

        let ctx = document.getElementById('MarkPriceKairiChart').getContext('2d');

        window.MPKChart = new Chart(ctx, {
            type: 'bar',
            data:{
                labels:data[0]['indexes'],
                datasets: [
                {
                    label:'Binance BTC/USD',
                    data:data[0]['values'],
                    borderColor: '#ff3737',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Binance BTC/USDT',
                    data:data[1]['values'],
                    borderColor: '#ff8337',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Bybit BTC/USD',
                    data:data[2]['values'],
                    borderColor: '#de6fff',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Bybit BTC/USDT',
                    data:data[3]['values'],
                    borderColor: '#ff74bc',
                    borderWidth: 1,
                    pointRadius: 0,
                }]
            },
            options: CHART_OPTIONS
        });

    })
};

function updateLongShortRatioChart() {
    $.ajax({
        type: 'GET',
        url: '/long_short_ratio',
    }).done(function (data) {

        if (typeof LSRChart !== 'undefined') {
            LSRChart.destroy();
        }

        let ctx = document.getElementById('LongShortRatioChart').getContext('2d');
        window.LSRChart = new Chart(ctx, {
            type: 'line',
            data:{
                labels:data[0]['indexes'],
                datasets: [
                {
                    label:'BTC/USD Top Acc',
                    data:data[0]['top_long_account_ratios'],
                    borderColor: '#ff3737',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'BTC/USD Top Pos',
                    data:data[0]['top_long_position_ratios'],
                    borderColor: '#ff8337',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'BTC/USD Glb Acc',
                    data:data[0]['global_long_account_ratios'],
                    borderColor: '#ffe272',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'BTC/USDT Top Acc',
                    data:data[1]['top_long_account_ratios'],
                    borderColor: '#9de16f',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'BTC/USDT Top Pos',
                    data:data[1]['top_long_position_ratios'],
                    borderColor: '#36d8b7',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'BTC/USDT Glb Acc',
                    data:data[1]['global_long_account_ratios'],
                    borderColor: '#53afff',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Bybit BTC/USD Glb Acc',
                    data:data[2]['global_long_account_ratios'],
                    borderColor: '#de6fff',
                    borderWidth: 1,
                    pointRadius: 0,
                },
                {
                    label:'Bybit BTC/USDT Glb Acc',
                    data:data[3]['global_long_account_ratios'],
                    borderColor: '#ff74bc',
                    borderWidth: 1,
                    pointRadius: 0,
                }
                ]
            },
            options: CHART_OPTIONS
        });

        $('#LongShortRatioChartUpdateTime').html("<最終更新日時> " + getNowDateStr());

    })
};

function getNowDateStr(){
    let nowDate = new Date();
    let year = nowDate.getFullYear();
    let month = nowDate.getMonth();
    let day = nowDate.getDate();
    let hour = nowDate.getHours();
    let min = nowDate.getMinutes();
    let second = nowDate.getSeconds();
    return year + "/" + month + "/" + day + " " + hour + ":" + min + ":" + second
};