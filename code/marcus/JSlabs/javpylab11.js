alert("Welcome to the calculator!")

var operators = ['+', '-', 'x', '/', '=', 'C'];
var buffer = '';
var currentResult = 0;
var currentOperation = '';






function createKeys()
{
    for(let i = 0; i < 10; i++)
    {
        let key = document.createElement('div');
        key.innerHTML = i;
        key.dataset.value = i;
        key.className = 'key';

        document.getElementById('numpad').appendChild(key);
    }

    operators.forEach(function(item)
    {

        let key = document.createElement('div');
        key.innerHTML = item;
        key.dataset.operation = item;
        key.className = 'key';

        document.getElementById('operators').appendChild(key);
    }



    window.addEventListener('load',createKeys);
}

operators.forEach(function(item){

    let key = document.createElement('div');
        key.className = 'key';
    key.innerHTML = item;
        key.dataset.operation = item;
        key.addEventListener('click', function(e){
            if (this.dataset.operation == 'cl')
            {
                buffer = '';
                currentResult = 0;
                currentOperation = '';
                document.getElementById('screen').innerHTML = '0';
                document.getElementById('screentotal').innerHTML = '0';
            }
            else
            {
                calculate();
                currentOperation = this.dataset.operation;
                buffer = '';
                document.getElementById('screen').innerHTML = 0;
            }

                });
                document.getElementById('operators').appendChild(key);
            });

     }

}

function calculate()
{
    switch(currentOperation) {

        case "+":
            currentResult += parseInt(buffer);
            break;

        case "-":
            currentResult -= parseInt(buffer);
            break;

        case "/":
            currentResult /= parseInt(buffer);
            break;

        case "x":
            currentResult *= parseInt(buffer);
            break;

        case "=":
            break;
        default:
            currentResult = parseInt(buffer);
    }

    document.getElementById('screentotal').innerHTML = currentResult;


}





    }














}



