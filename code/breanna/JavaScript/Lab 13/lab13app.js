// Javascript for Lab 13 - Quotes

// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.


Vue.component('a-quote', {
    props: ['quote'],
    template: '<p>"{{ quote.body }}"<br>Author: {{ quote.author }}</p>'
  })

let vm = new Vue({
    el: '#app',
    data: {
        searchType: '',
        searchTerm: '',
        quotes: []
    },
    methods: {
        listQuotes: function () {
            axios({
                headers: {
                    Authorization: `Token token="${FavQsKey}"`
                },
                method: "get",
                url: `https://favqs.com/api/quotes/?filter=${this.searchTerm}`
                // https://favqs.com/api/quotes/?filter=${this.searchTerm}&type=tag
            }).then(response => {
                this.quotes = response.data.quotes;
            });
            this.searchType = '';
            this.searchTerm = ''
        }
    }
});