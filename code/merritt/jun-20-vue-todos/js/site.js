let vm = new Vue({
    el: '#app',
    data: {
        todos: [
            { text: "Walk the dog", completed: false, id: 1 },
            { text: "Groceries", completed: true, id: 2 },
            { text: "Laundry", completed: false, id: 3 }
        ],
        newTodo: "",
        newTodoId: 4 
    },
    methods: {
        addTodo: function (event) {
            this.todos.push({ text: this.newTodo, completed: false, id: this.newTodoId });
            this.newTodo = "";
            this.newTodoId++;
        },
        completeTodo: function (todo) {
            todo.completed = true;
        },
        removeTodo: function (todo) {
            this.todos.splice(this.todos.indexOf(todo), 1);
        }
    },
    computed: {
        incompleteTodos: function () {
            return this.todos.filter(function(todo) {
                return todo.completed === false;
            });
        },
        completeTodos: function () {
            return this.todos.filter(function(todo) {
                return todo.completed === true;
            });
        }
    }
})