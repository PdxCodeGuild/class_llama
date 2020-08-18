// JavaScript Lab 04 - To-Do List

let newTask = document.getElementById("new-task-s")
newTask.addEventListener("click", function(){
    let li = document.createElement("li")
    let completeButton = document.createElement("button")
    let deleteButton = document.createElement("button")
    li.innerText = document.getElementById("new-task").value
    let list = document.getElementById("to-do-list")
    completeButton.innerText = "Mark task as complete"
    deleteButton.innerText = "Delete task from list"
    li.append(completeButton)
    li.append(deleteButton)
    list.append(li)
    document.getElementById("new-task").value = "";

    completeButton.addEventListener("click", function() {
        this.parentNode.style.textDecoration = "line-through"
    })

    deleteButton.addEventListener("click", function() {
        this.parentNode.remove();
    })
})