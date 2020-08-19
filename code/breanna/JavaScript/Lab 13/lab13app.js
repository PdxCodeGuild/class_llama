// Javascript for Lab 13 - Quotes


// Implement pagination buttons when the search returns more than 25 quotes.

Vue.component('initial-quote', {
    props: ['quote'],
    template: '<p>"{{ quote.body }}"<br>Author: {{ quote.author }}</p>'
  })

Vue.component('a-quote', {
    props: ['quote'],
    template: '<p>"{{ quote.body }}"<br>Author: {{ quote.author }}</p>'
  })

let vm = new Vue({
    el: '#app',
    data: {
        searchType: 'initial',
        searchTerm: '',
        quotes: [],
        page: 1
    },
    created: function () {
        axios({
            headers: {
                Authorization: `Token token="${FavQsKey}"`
            },
            method: "get",
            url: `https://favqs.com/api/quotes/`
        }).then(response => {
            console.log(response.data);
            this.quotes = response.data.quotes;
        })
    },
    methods: {
        listQuotes: function () {
            axios({
                headers: {
                    Authorization: `Token token="${FavQsKey}"`
                },
                method: "get",
                url: `https://favqs.com/api/quotes/?filter=${this.searchTerm}&type=${this.searchType}/`
            }).then(response => {
                console.log(response.data);
                this.quotes = response.data.quotes;
            });
            this.searchType = 'initial';
            this.searchTerm = ''
        },
        nextPage: function () {
            page ++
            axios({
                headers: {
                    Authorization: `Token token="${FavQsKey}"`
                },
                method: "get",
                url: `https://favqs.com/api/quotes/?filter=${this.searchTerm}&type=${this.searchType}/?page=${page}`
            }).then(response => {
                console.log(response.data);
                this.quotes = response.data.quotes;
            });
        }
    }
});