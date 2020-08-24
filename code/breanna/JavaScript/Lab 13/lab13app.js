// Javascript for Lab 13 - Quotes

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
        page: 1,
        activeTerm: '',
        activeType: '',
        loadMoreButton: false
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
            this.activeType = this.searchType;
            this.activeTerm = this.searchTerm;
            this.page = 1;
            this.loadMoreButton = true;
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
            this.page ++
            axios({
                headers: {
                    Authorization: `Token token="${FavQsKey}"`
                },
                method: "get",
                url: `https://favqs.com/api/quotes/?filter=${this.activeTerm}&type=${this.activeType}&page=${this.page}/`
            }).then(response => {
                console.log(response.data);
                this.quotes = response.data.quotes;
            });
        }
    }
});