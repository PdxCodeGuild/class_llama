
let additem = document.getElementById('newitem') 
let btn = document.getElementById('submit_item')
let todo_list = document.getElementById('todolist')
let completed_btn = document.getElementById('complete')
let remove_btn = document.getElementById('remove')

function list() {
    item = additem.value;
    let li = document.createElement('li');
    li.innerText = item;
    todo_list.append(li);
}

btn.addEventListener('click' , list)

completed_btn.addEventListener('click', function() {
    
}


