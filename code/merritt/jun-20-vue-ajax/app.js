let vm = new Vue({
    el: '#app',
    data: {
        quote: {}
    },
    methods: {
        loadQuote: function () {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd"
            }).then(response => {
                this.quote = response.data.quote;
            });
        }
    }
});