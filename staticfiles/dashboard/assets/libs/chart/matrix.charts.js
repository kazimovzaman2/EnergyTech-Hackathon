$(function () {
  
   fetch('http://127.0.0.1:8000/api/ml-date/')
  .then(response => response.json())
  .then(data => {

      let ctx = document.getElementById("bars");
 
      let usedData = data[0]["used_data"];
      let usedDate = data[0]["used_date"];
      let usedDatas = [];
      for(let i=0;i<7;i++){
        usedDatas.push(usedData[i]);
      }
      
      let usedDatev = [];
      let month = [];
      for(let i=0;i<7;i++){
        let temp = parseInt(usedDate[i][5]+usedDate[i][6]);
        month.push(temp);
      }
      for(let i=0;i<7;i++){
        let temp = usedDate[i][8]+usedDate[i][9];
        usedDatev.push(temp);
      }

      let months = ["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
    
      console.log(month[4]);  
    
    
    
      var d1 = [];
      
      for(let i = 0; i<7; i++)
      {
        let a = [];
        a.push(usedDatev[i] + " " +months[month[i]]);
        d1.push(a);
      }
      
      console.log(d1);

      let chart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: d1,
          datasets:[
            {
              label:"Istifade olunan enerji",
              data:usedDatas
            }
          ]
        }
      }
      )

      
    
    maruti = {
      // === Tooltip for flot charts === //
      flot_tooltip: function (x, y, contents) {
        $('<div id="tooltip">' + contents + "</div>")
          .css({
            top: y + 5,
            left: x + 5,
          })
          .appendTo("body")
          .fadeIn(200);
      },
    };
  })
  .catch(error => console.error(error));

//   console.log(usedData);  



//   var d1 = [];
  
//   for(let i = 0; i<=7; i++)
//   {
//     let a = [];
//     a.push(usedData[i], usedDate[i]);
//     d1.push(a);
//   }

  

//   var data = new Array();
//   data.push({
//     data: d1,
//     bars: {
//       show: true,
//       barWidth: 0.6,
//       order: 1,
//     },
//   });

//   //Display graph
//   var bar = $.plot($(".bars"), data, {
//     legend: true,
//     color: "#2b2b2b",
//   });
});

// maruti = {
//   // === Tooltip for flot charts === //
//   flot_tooltip: function (x, y, contents) {
//     $('<div id="tooltip">' + contents + "</div>")
//       .css({
//         top: y + 5,
//         left: x + 5,
//       })
//       .appendTo("body")
//       .fadeIn(200);
//   },
//};
