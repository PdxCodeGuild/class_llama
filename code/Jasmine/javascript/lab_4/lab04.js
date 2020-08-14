
let additem = document.getElementById('newitem') 
let btn = document.getElementById('submit_item')
let todo_list = document.getElementById('todolist')
let complete_list = document.getElementById('completelist')

function list() {
    let item = additem.value;
    let li = document.createElement('li');
    li.innerText = item;
    let complete_btn = document.createElement('button')
    complete_btn.innerText = 'complete'
    complete_btn.setAttribute('id', 'completed')
    li.append(complete_btn)
    let remove_btn = document.createElement('button')
    remove_btn.innerText = 'remove'
    remove_btn.setAttribute('id' , 'remove')
    li.append(remove_btn)
    todo_list.append(li);

    complete_btn.addEventListener('click', function() {
        let comp_item = complete_btn.parentElement
        todo_list.removeChild(comp_item)
        complete_list.append(comp_item)
        complete_btn.remove()

        
        })

    remove_btn.addEventListener('click', function() {
        let removeitem = remove_btn.parentElement
        console.log(removeitem)
        li.remove()

    })
}

btn.addEventListener('click' , list)
 






