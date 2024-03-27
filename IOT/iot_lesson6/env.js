var php1
var data_dht22
data_dht22 = new Array(7);
function Monitor(){
ajax_function();
operation();
}
function ajax_function(){
$.ajax({
type: "POST",
url: "env.php",
async:false,
data: {data1:'1'},// Dummy
}).done(function(datasql){
data_arr=JSON.parse(datasql);
php1 = data_arr;
});
}
function operation() { // Website data update on HTML Track(id) that be re-arrange from Ajax
    data_dht22 = php1;
    document.getElementById('id').innerHTML = 'Sensor_ID : '+ data_dht22[0];
    document.getElementById('temp').innerHTML = 'Temperature : '+ data_dht22[3] +' deg';
    document.getElementById('hum').innerHTML = 'Humidity : '+ data_dht22[4] +' %';
    if(data_dht22[3] <= 27){document.getElementById('templ').style.backgroundColor = 'lightgreen';}
    else if(data_dht22[3] <= 30){document.getElementById('templ').style.backgroundColor = 'orange';}
    else{document.getElementById('templ').style.backgroundColor = 'red';}

    if(data_dht22[4] <= 60){document.getElementById('huml').style.backgroundColor = 'lightgreen';}
    else if(data_dht22[4] <= 80){document.getElementById('huml').style.backgroundColor = 'orange';}
    else{document.getElementById('huml').style.backgroundColor = 'red';}
    }
    
    function Start(){ // Main function that be run all javascript action
    setInterval('Monitor()',500); // Time interval of running as cycle
    }