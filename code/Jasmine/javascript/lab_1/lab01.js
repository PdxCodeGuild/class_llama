
const units = {
    ft : 0.3048,
    mi : 1609.34, 
    m : 1, 
    km: 1000, 
    yd: .9144, 
    inch: .0254
}


let number = prompt("please enter a number:");
alert("you have chosen " + number)
console.log(number)
let measurement = prompt("what is the measurement:")
alert("You want to convert " + number + measurement)
let convert = prompt("what would you like to convert to:")
alert("You would like to  convert to " + convert)
console.log(convert)
console.log(measurement)
console.log(units[measurement])

number = number/units[measurement]
console.log(number, 'this a number')
alert("The conversion is " + number*units[convert])

