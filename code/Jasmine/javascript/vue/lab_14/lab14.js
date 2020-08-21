let vm = new Vue ({
    el: '#app',
    data: {
        token: '',
        results: {},
        searchmusic: '',
        type: 'album,artist,playlist,track',
        browsenew: {},
    
    
        
    }, 

    methods: {
        getresults: function() {
            axios({
                method: "get", 
                url: `https://api.spotify.com/v1/search?q=${this.searchmusic}&type=${this.type}`,
                headers: {Authorization: `Bearer ${this.token}`}
        }).then(response=> {
            this.results = response.data
        })
    },

        getnew: function() {
            axios({
                method: "get", 
                url: `https://api.spotify.com/v1/browse/new-releases?country=US`,
                headers: {Authorization: `Bearer ${this.token}`}
        }).then(response=> {
            this.browsenew = response.data
        })
    }},


    created: function() {
        axios({
            method: "post", 
            url: "https://accounts.spotify.com/api/token",
            auth: {username: '8e8ffa3d46714a2cb205b6f0f67a825b', password: 'a6ed18a3293b4778a29e80bc01cc5a3f'},
            data: 'grant_type=client_credentials'
        }).then(response=> {
            this.token = response.data.access_token
        })
    }
})