let undone_list = document.getElementById("undone");
let done_list = document.getElementById("done");



// function complete_item(item) {
//     undone_list.removeChild(item)
// }

function add_new_item() {
    let entered_task = document.getElementById("new-task");    
    let list_item = document.createElement("li");

    list_item.innerText = entered_task.value;
    undone_list.appendChild(list_item);

    let button = document.createElement("button");
    button.innerText = "complete task";
    // button.addEventListener("click", complete_item(list_item));
    
    list_item.appendChild(button);
}


let new_item = document.getElementById("new-task-submit");
new_item.addEventListener("click", add_new_item);