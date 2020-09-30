new Vue({
    el: '#app',
    data: {
        gender: "",
        eyeColor: "",
        hairColor: "",
        
        matches: [],
        results: []
    },
    methods: {
        faceSearch: function() {
            axios({
                method: "get",
                url: " https://ghibliapi.herokuapp.com/people",
                

            }).then(response=>{
                console.log(response.data);
                this.matches = response.data
                
            })
        },
        sortFaces() {
            let genderMatch = []
            let eyeColorMatch = []
            let hairColorMatch = []

            this.matches.forEach(match => {
                if (this.gender === match.gender) {
                    genderMatch.push(match)
                    
                }
            })
            
            genderMatch.forEach(match => {
                if (this.gender === match.gender) {
                    eyeColorMatch.push(match)
                    
                }
            })
            
            eyeColorMatch.forEach(match => {
                if (this.gender === match.gender) {
                    hairColorMatch.push(match)
                    
                }
            })

            this.results = hairColorMatch
            
        }
    },
    mounted: function() {
        this.faceSearch()
    }
})