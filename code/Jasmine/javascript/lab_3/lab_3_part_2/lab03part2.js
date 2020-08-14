
let add = document.getElementById('add_more')
let average = document.getElementById('average')

add.addEventListener ('click' , function() {
    let newnumber = document.createElement('input');
    newnumber.type = 'number';
    newnumber.classList.add('number');
    document.getElementById('numberlist').append(newnumber)

})

average.addEventListener('click', function() {
    let numbers = document.getElementsByClassName('number');
    let sum = 0 
    for (let i=0; i<numbers.length; i++) {
        sum += parseFloat(numbers[i].value)
    }    
    document.getElementById('results').innerText = sum / numbers.length
})