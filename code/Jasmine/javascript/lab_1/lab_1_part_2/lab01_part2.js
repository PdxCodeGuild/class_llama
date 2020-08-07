const units = {
    ft : 0.3048,
    mi : 1609.34, 
    m : 1, 
    km: 1000, 
    yd: .9144, 
    inch: .0254
}

let btn = document.getElementById('convert'); 
let results = document.getElementById('results')
let num = document.getElementById('num');
let measure1 = document.getElementById('measure1');
let measure2 = document.getElementById('measure2');


function convert (){
    let number = parseFloat(num.value)*units[measure1.value]
    number = number/units[measure2.value]
        results.innerText = number
}

    btn.addEventListener('click', convert)