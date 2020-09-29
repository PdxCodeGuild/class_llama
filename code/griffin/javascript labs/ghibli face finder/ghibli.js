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
                console.log(response);
                this.matches = response.data
                
            })
        },
        sortFaces() {
            let genderMatch = []
            let eyeColorMatch = []
            let hairColorMatch = []
            
            for (match in this.matches) {
                if (this.gender == match.gender) {
                    genderMatch.append(match)
                }
            }
            for (match in genderMatch) {
                if (this.eyeColor == match.eye_color) {
                    eyeColorMatch.append(match)
                }
            }
            for (match in eyeColorMatch) {
                if (this.hairColor == match.hair_color) {
                    hairColorMatch.append(match)
                } 
            }
            this.results = hairColorMatch

        }
    },
    mounted: function() {
        this.faceSearch()
    }
})