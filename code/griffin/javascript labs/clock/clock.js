let date = new Date();
let stopdate = new Date();
let hour = date.getHours();
let minutes = date.getMinutes();
let seconds = date.getSeconds();
let stopseconds = 0;

let time_display = document.getElementById("time");
let startstop = document.getElementById("startstop");
let stopwatch = document.getElementById("stopwatch");

function update_time() {
    date = new Date();
    hour = date.getHours();
    minutes = date.getMinutes();
    seconds = date.getSeconds();
    time = `${hour}:${minutes}:${seconds}`;
    time_display.innerText = time;
}

window.setInterval(update_time,1000);

function update_stopwatch() {
    stopseconds = stopdate.getSeconds();
    stopseconds += 1;
    stopdate.setSeconds(stopseconds);
    
    stopwatch.innerText = `${stopdate.getHours()}:${stopdate.getMinutes()}:${stopdate.getSeconds()}`;
}

startstop.addEventListener("click", function() {
    stopdate = new Date();
    stopdate.setHours(0,0,0,0);
    window.setInterval(update_stopwatch,1000);

})