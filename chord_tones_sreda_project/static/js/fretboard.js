(function() {
    const fretboard_div = document.querySelector('.fretboard')


    const fretboard_app = {
        init() {
            this.setup_fretboard();
        },

        setup_fretboard() {
            fretboard_div.innerHTML = "ALL OF THIS STUFF"
        }
    }

    fretboard_app.init()
})();