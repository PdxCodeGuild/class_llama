let vm = new Vue({
    el: '#app',
    data: {
        quote_array: []
    },
    methods: {
        
        
    },
    mounted: function () {
        for (let i = 0; i< 25; i++) {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd"
            }).then(response => {
                this.quote_array.push(response.data.quote.body);
            })
        }
    }
})