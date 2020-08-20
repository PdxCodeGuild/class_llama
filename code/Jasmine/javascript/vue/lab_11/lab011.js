let vm = new Vue({
    el: '#vm',
    data: {
        current: '', 
        todos: [
        
        ],

    },

    methods: {
        create: function(current) {
            this.todos.push({text: this.current})
            this.current=''
        },

        del:function(todo) {
            this.todos.splice(this.todos.indexOf(todo))
        }
    }
    
       
})

