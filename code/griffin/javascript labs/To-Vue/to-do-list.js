let vm = new VTTCue({
    el: '#app',
    data: {
        items: [
            {text: "gramd camyom", completed: false, id: 1}

        ],
        newItem: "",
        newItemId: 2
    },

    methods: {
        addItem: function (event) {
            this.items.push({ text: this.newItem, completed: false, id: this.newItemId });
            this.newItem = "";
            this.newItemId += 1;
        },
        completeItem: function (item) {
            item.completed = true;
        },
        removeItem: function (item) {
            //I don't understand the example code here
        }


    },
    computed: {
        incompleteItems: function() {
            return this.items.filter(function(item) {
                return item.completed === false;
            });     
        },
        completeItems: function() {
            return this.items.filter(function(item) {
                return item.completed === true;
            });     
        },
    }



})