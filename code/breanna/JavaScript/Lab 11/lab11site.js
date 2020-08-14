// JavaScript Lab 11 - To-Do List

new Vue({
    el: '#to-do-list',
    data: {
        todos: [
            { text: 'Learn JavaScript' },
            { text: 'Learn Vue' },
            { text: 'Build something awesome' }
        ],
        newTaskText: ''
    },
    methods: {
        newTask: function () {
            this.todos.push({text: this.newTaskText })
            this.newTaskText = ''
        },
        // completeTask: function () {
            // ?
        // },
        // deleteTask: function () {
            // this.todos.
        // }
    }
})