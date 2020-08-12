let date = new Date();
let stopdate = new Date();
let hour = date.getHours();
let minutes = date.getMinutes();
let seconds = date.getSeconds();
let stopseconds = 0;
let stopwatch_running = false;

let lap_array = document.getElementById("lap-array");
let container = document.getElementById("container");
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

//Makes things happen when you push the start stopwatch button
startstop.addEventListener("click", function() {
    if (stopwatch_running == false) {
        stopwatch_running = true;
        stopdate = new Date();
        stopdate.setHours(0,0,0,0);
        let stopwatch_interval = window.setInterval(update_stopwatch,1000);
        
        //add stop button
        let stop_button = document.createElement("button");
        stop_button.innerText = "stop";
        container.append(stop_button);
        stop_button.addEventListener("click", function() {
            clearInterval(stopwatch_interval);
            container.removeChild(stop_button);
            container.removeChild(lap_button);
            lap_array.innerText = "";
            stopwatch_running = false;
        })

        //add lap button
        let lap_button = document.createElement("button");
        lap_button.innerText = "lap";
        container.append(lap_button);
        lap_button.addEventListener("click", function() {
            let lap_item = document.createElement("li");
            lap_item.innerText = `${stopdate.getHours()}:${stopdate.getMinutes()}:${stopdate.getSeconds()}`;
            lap_array.append(lap_item);
        })
    }
})