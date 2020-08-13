let width = document.getElementById("canvas").width;
let height = document.getElementById("canvas").height;
let ctx = document.getElementById("canvas").getContext("2d");
let cnv = document.getElementById("canvas");


let ball = {
    radius: 4,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};



function main_loop() {
    ball.px += ball.vx;
    ball.py += ball.vy;
    if (ball.px <= 1) {
        ball.px = 1;
        ball.vx *= -1;
    }
    if (ball.py <= 1) {
        ball.py = 1;
        ball.vy *= -1;
    }
    if (ball.px >= 499) {
        ball.px = 499;
        ball.vx *= -1;
    }
    if (ball.py >= 499) {
        ball.py = 499;
        ball.vy *= -1;
    }
    ctx.clearRect(0,0,width,height);
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'green';
    ctx.fill();
    
    
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);