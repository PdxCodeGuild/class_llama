let vm = new Vue({
    el: '#app',
    data: {
        quote_array: [],
        searchItem: "",
        searchType: "",
        search: false,
        searchResults: null,
        current_page: 1,
        finalPage: false,
        
    },
    methods: {
            searchQuotes: function() {
                
                axios({
                    method: "get",
                    url: "https://favqs.com/api/quotes/",
                    headers: {
                        Authorization: 'Token token="aeabe25320319442cf558f5212f93a87"',
                    },
                    params: {
                        filter: this.searchItem,
                        type: this.searchType,
                        page: this.current_page
                    },
                })
                .then(response=>{
                    if (response.data.last_page) {
                        console.log("final page");
                        this.finalPage = true;
                    } else {
                        this.finalPage = false;
                    }
                    
                    this.search = true;
                    console.log(response.data);
                    this.searchResults = response.data.quotes;
                    
                    
                    
                    // response.data.qotes is an array of objects
                    // .map takes in a array and looks at each object and you can parse from there
                    // ie element is just one of the objects and it has a body inside
                    // response.data.quotes.map(element => console.log(element.body))
                })  
                
            },
            previousPage: function() {
                this.current_page = this.current_page-=1;
                this.searchQuotes();
            },
            nextPage: function() {
                this.current_page = this.current_page+=1;
                this.searchQuotes();
            }
    },
    mounted: function () {
        for (let i = 0; i< 25; i++) {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd"
            }).then(response => {
                this.quote_array.push(response.data.quote);
            })
        }
    }
})