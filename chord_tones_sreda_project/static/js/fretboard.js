(function() {
    const fretboard_div = document.querySelector('.fretboard')

    const root = document.documentElement;
    const chord_section = document.querySelectorAll('.chord-notes')

    const single_fret_mark_positions = [3, 5, 7, 9, 15, 17, 19, 21];
    const double_fret_mark_positions = [12, 24];
    const flat_notes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'];
    const sharp_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#','G', 'G#'];
    const instrument_tuning_presets = {
        "Guitar": [7, 2, 10, 5, 0, 7],
        "Bass (4 strings)": [10, 5, 0, 7],
        'Ukulele': [0, 7, 3, 10],
    };

    const test = document.querySelector('.test')

    let all_notes;
    let show_duplicate_notes = false;
    let show_all_notes = false;
    let selected_instrument = 'Guitar';
    let accidentals = 'sharps';
    let number_of_frets = 12;
    let number_of_strings = instrument_tuning_presets[selected_instrument].length;

    // Const contain handy function to create html elements, and if needed
    // with innerHTML content
    const fretboard_tools = {
        createElement(element, content) {
            element = document.createElement(element);
            if (arguments.length > 1) {
                element.innerHTML = content;
            }
            return element;
        }
    }

    const fretboard_app = {
        init() {
            this.setup_fretboard();
        },

        setup_fretboard() {
            // Initialize a guitar fretboard div
            fretboard_div.innerHTML = ""
            root.style.setProperty('--number-of-strings', number_of_strings)
            // add 'strings' to div
            for (let i = 0; i < number_of_strings; i++) {
                let string = fretboard_tools.createElement('div');
                string.classList.add('string');
                fretboard.appendChild(string);

                // add 'frets' to the 'string'
                for (let fret = 0; fret <= number_of_frets; fret++) {
                    let fret_note = fretboard_tools.createElement('div');
                    fret_note.classList.add('fret-note');
                    string.appendChild(fret_note);

                    let note_name = this.generate_notes_name((fret + instrument_tuning_presets[selected_instrument][i]), accidentals);
                    fret_note.setAttribute('note-data', note_name);

                }
            }

        },

        // Return a note, based on list of notes,
        // that passed in the function (flats or sharps)
        generate_notes_name(note_index, accidentals) {
            note_index = note_index % 12;
            let note_name;
            if (accidentals === 'flats') {
                note_name = flat_notes[note_index];
            } else if (accidentals ==='sharps') {
                note_name = sharp_notes[note_index];
            }
            return note_name;
        },

        setup_selected_instrument() {
            for (instrument in instrument_tuning_presets) {
                let instrument_option = fretboard_tools.createElement('option', instrument);
                instrument_selector.appendChild(instrument_option);
            }
        },
        setup_note_name_section() {
            note_name_section.innerHTML = '';
            let note_names;
            if (accidentals === 'flats') {
                note_names = flat_notes;
            } else {
                note_names = sharp_notes;
            }
            note_names.forEach((note_name) => {
                let note_name_element = fretboard_tools.createElement('span', note_name);
                note_name_section.appendChild(note_name_element);
            });
        },

        toggle_duplicate_notes(note_name, opacity) {
        /* When checkbox flag toggled
            change opacity of a target note
        */
            all_notes = document.querySelectorAll('.fret-note');
            for (let i = 0; i < all_notes.length; i++) {
                if (all_notes[i].getAttribute('note-data') === note_name) {
                    all_notes[i].style.setProperty('--note-dot-opacity', opacity); 
                }
            }
        },
    }


    fretboard_app.init()
})();