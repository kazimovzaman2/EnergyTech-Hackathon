$(function () {
  fetch('https://energy-tech.azurewebsites.net/api/ml-adnsu/')
  .then(response => response.json())
  .then(data => {
let cts = document.getElementById('real-time');

let usedData = data[0]["used_data"];
console.log(usedData);
let usedDate = data[0]["used_date"];
let usedDatas = [];
let usedDatass = [];

usedDatas.push(usedData[0]);

for(let i=1;i<120;i++){
  usedDatass.push(usedData[i]);
}
let usedDatev = [];
let hour = [];


let temp = parseInt(usedDate[0][11]+usedDate[0][12]);
hour.push(temp);


for(let i=1;i<120;i++){
  let temp = parseInt(usedDate[i][11]+usedDate[i][12]);
  usedDatev.push(temp);
}
  
  

  let chart = new Chart(cts, {
    type: "line",
    data :{
      labels: hour,
    datasets: [
      {
        label: "Woltage",
        data: usedDatas
      }
    ]}
  })
  
  function sleep(ms){
    let start = new Date().getTime(), expire = start + ms;
    while(new Date().getTime() < expire){}
    return;
  }
  function add_data(chart, data, label){
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
      dataset.data.push(data)
    });
      chart.update();
  } 
    function remove_data(chart){
      chart.data.labels.shift();
      chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
      });
      chart.update();
    }

  let i = 0;
  function coni(){
    add_data(chart, usedDatass[i], usedDatev[i]);
    if(i>=24){
      remove_data(chart);
    }
    i += 1;
  }
  setInterval(coni, 2000);

})});