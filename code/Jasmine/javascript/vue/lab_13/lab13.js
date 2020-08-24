let vm = new Vue ({
    el: '#app', 
    data: {
        quotes: {},
        page: 0,
        last_page: true,
        filter: '',
    }, 


    methods: {
        loadQuote: function () {
            axios({
                method: "get", 
                url: "https://favqs.com/api/quotes/", 
                headers: {Authorization: 'Token token="013ae52a79f2b1a99bc3084e9dc1ebc6"'}
            }).then(response => {
                this.quotes = response.data.quotes;
                this.page = response.data.page;
                this.last_page = response.data.last_page;
            })                 
        }, 

        loadMore: function () {
            axios({
                method: "get", 
                url: `https://favqs.com/api/quotes/?filter=${this.filter}&page=${this.page+1}`, 
                headers: {Authorization: 'Token token="013ae52a79f2b1a99bc3084e9dc1ebc6"'}
            }).then(response => {
                this.quotes = this.quotes.concat(response.data.quotes)
                this.page = response.data.page;
                this.last_page = response.data.last_page;
            })                 
        },

        searchQuote: function () {
            axios({
                method: "get", 
                url: `https://favqs.com/api/quotes/?filter=${this.filter}`, 
                headers: {Authorization: 'Token token="013ae52a79f2b1a99bc3084e9dc1ebc6"'}
            }).then(response => {
                this.quotes = response.data.quotes
                this.page = response.data.page;
                this.last_page = response.data.last_page;
            })                 
        },
     
    },

    mounted: function () {
        this.loadQuote()
    }

})


