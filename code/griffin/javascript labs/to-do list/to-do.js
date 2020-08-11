let undone_list = document.getElementById("undone");
let done_list = document.getElementById("done");
let new_item = document.getElementById("new-task-submit");

new_item.addEventListener("click", function() {
    let entered_task = document.getElementById("new-task");    
    let list_item = document.createElement("li");
    
    list_item.innerText = entered_task.value;
    undone_list.appendChild(list_item);
    
    let complete_button = document.createElement("button");
    complete_button.innerText = "complete task";
    complete_button.setAttribute("value", list_item.innerText);
    complete_button.setAttribute("id", "undone_item");
    list_item.appendChild(complete_button);

    complete_button.addEventListener("click", function() {
        undone_list.removeChild(list_item);
        done_list.appendChild(list_item);
        list_item.removeChild(complete_button);
        list_item.setAttribute("class", "task-done");

        let delete_button = document.createElement("button");
        delete_button.innerText = "delete task";
        list_item.appendChild(delete_button);

        delete_button.addEventListener("click", function() {
            done_list.removeChild(list_item);
        });
    });
});