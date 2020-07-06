tonics = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
extended_tonics = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
                   'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G',]
note_types = ['R', 'b2', '2', '3m', '3', '4', 'b5', '5', '#5', '6', '7', '7M']
major = [2, 2, 1, 2, 2, 2]
natural_minor = [2, 1, 2, 2, 1, 2]
harmonic_minor = [2, 1, 2, 2, 1, 3]
pentatonic_major = [2, 2, 3, 2]
pentatonic_minor = [3, 2, 2, 3]
scales = [major, natural_minor, harmonic_minor, pentatonic_major, pentatonic_minor]
known_chord_types = ['m', 'sus2', 'major']
chord_type_m = ['R', '3m', '5']
chord_type_sus2 = ['R', '2', '5']
chord_type_major = ['R', '3', '5']
actual_chord_types = [chord_type_m, chord_type_sus2]
while True:
    mode = input('''0 - add good chord progressions you like
Choose mode: ''')
    if mode == '0':
        waiting_for_an_acceptable_chord = True
        chosen_chords = []
        while waiting_for_an_acceptable_chord:
            temp_chord = input('add the first chord of your progression: ')
            chord_type = temp_chord.replace(temp_chord[0], '')
            if temp_chord[0] == temp_chord:
                chord_type = 'major'
            if chord_type in known_chord_types:
                chosen_chords.append(temp_chord)
                waiting_for_an_acceptable_chord = False
                second_chord_added = False
                while not second_chord_added:
                    temp_chord = input('add the next chord: ')
                    chord_type = temp_chord.replace(temp_chord[0], '')
                    if temp_chord[0] == temp_chord:
                        chord_type = 'major'
                    if chord_type in known_chord_types:
                        chosen_chords.append(temp_chord)
                        second_chord_added = True
                        progression_finished = False
                        while not progression_finished:
                            temp_chord = input(
                                'if there is another chord, add it. If there are no chords any more, write X: ')
                            if temp_chord == 'X':
                                progression_finished = True
                            else:
                                chord_type = temp_chord.replace(temp_chord[0], '')
                                if temp_chord[0] == temp_chord:
                                    chord_type = 'major'
                                if chord_type in known_chord_types:
                                    chosen_chords.append(temp_chord)
                                else:
                                    print('sorry... I do not know such chords yet. Maybe something more simple?')
                        temp_chord = chosen_chords[0]
                        chosen_chords.append(temp_chord)
                        chosen_chords_copy = chosen_chords.copy()
                        for chord_x in chosen_chords:
                            first_chord = chosen_chords_copy[0]
                            try:
                                second_chord = chosen_chords_copy[1]
                            except IndexError:
                                second_chord = ''
                            if second_chord != '':
                                print('analyzing', first_chord, 'to', second_chord)
                                for scale in scales:
                                    for tonic in tonics:
                                        scale_index = tonics.index(tonic)
                                        current_scale = []
                                        current_scale.append(tonic)
                                        for step in scale:
                                            scale_index += step
                                            current_scale.append(extended_tonics[scale_index])
                                        first_chord_notes = []
                                        if first_chord[0] == first_chord:
                                            first_tonic = tonics.index(first_chord)
                                            for another_step in chord_type_major:
                                                first_index = note_types.index(another_step)
                                                current_note = first_tonic + first_index
                                                first_chord_notes.append(extended_tonics[current_note])
                                                print(first_chord_notes)
                                        else:
                                            first_tonic = tonics.index(first_chord[0])
                                            print(tonics[first_tonic])
                                            first_chord_type = temp_chord.replace(temp_chord[0], '')
                                            for chord_type in actual_chord_types:
                                                if first_chord_type == 
                            chosen_chords_copy.remove(chord_x)
                    else:
                        print('sorry... I do not know such chords yet. Maybe something more simple?')
            else:
                print('sorry... I do not know such chords yet. Maybe something more simple?')
