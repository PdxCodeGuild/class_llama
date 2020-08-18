// JavaScript Lab 11 - To-Do List

new Vue({
    el: '#todo-list',
    data: {
        todos: [],
        newTaskText: '',
        newTaskId: 0,
    },
    methods: {
        newTask: function (event) {
            this.todos.push({text: this.newTaskText, completed: false, id: this.newTaskId });
            this.newTaskText = '';
            this.newTaskId ++;
        },
        completeTask: function (todo) {
            todo.completed = true;
        },
        deleteTask: function (todo) {
            this.todos.splice(this.todos.indexOf(todo), 1);
        }
    },
    computed: {
        incompleteTasks: function () {
            return this.todos.filter(function(todo) {
                return todo.completed === false;
            });
        },
        completeTasks: function () {
            return this.todos.filter(function(todo) {
                return todo.completed === true;
            });
        }
    }
})