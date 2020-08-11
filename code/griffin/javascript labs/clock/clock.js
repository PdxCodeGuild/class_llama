let date = new Date();
let hour = date.getHours();
let minutes = date.getMinutes();
let seconds = date.getSeconds();

let time_display = document.getElementById("time");

function update() {
    date = new Date();
    hour = date.getHours();
    minutes = date.getMinutes();
    seconds = date.getSeconds();
    time = `${hour}:${minutes}:${seconds}`;
    time_display.innerText = time;
}

window.setInterval(update,1000);
