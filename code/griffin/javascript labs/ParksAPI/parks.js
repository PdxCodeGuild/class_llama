new Vue({
    el: '#app',
    data: {
        searchItem: "",
        
    },
    methods: {
        searchPlaces: function() {
            axios({
                method: "get",
                url: "https://ridb.recreation.gov/api/v1/activities",
                headers: {
                    apikey: api_key,
                    'Access-Control-Allow-Origin': '*'
                },
                params: {
                    QUERY: "SWIMMING",
                    LIMIT: 50,
                    OFFSET: 0,
                    
                },
            
            })
            .then(response=>{
                console.log(response);
            })
        }
    }
})