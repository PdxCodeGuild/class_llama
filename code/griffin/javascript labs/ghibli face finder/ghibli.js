new Vue({
    el: '#app',
    data: {
        gender: null,
        eyeColor: null,
        hairColor: null,
        age: null,
    },
    methods: {
        faceSearch: function() {
            axios({
                method: "get",
                url: " https://ghibliapi.herokuapp.com/people",
                params: {
                    fields: `${this.gender},${this.eye_color},${this.hair_color},${this.age}`,
                }

            }).then(response=>{
                console.log(response);
            })
        }
    }
})