tonics = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
extended_tonics = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
                   'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']
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
def special_selection():
    extended_tonics_copy = extended_tonics.copy()
    rejected = False
    for xx in assimilated_notes:
        if xx not in current_scale:
            rejected = True
            break
    if not rejected:
        for xxx in extended_tonics:
            if xxx != tonic:
                extended_tonics_copy.remove(xxx)
            else:
                break
        if scale == major:
            normal_scale_name= 'Major'
        elif scale == natural_minor:
            normal_scale_name = 'Natural Minor'
        elif scale == harmonic_minor:
            normal_scale_name = 'Harmonic Minor'
        elif scale == pentatonic_major:
            normal_scale_name = 'Pentatonic Major'
        elif scale == pentatonic_minor:
            normal_scale_name = 'Pentatonic Minor'
        first_note_type_index = extended_tonics_copy.index(first_chord_notes[0])
        first_interval_to_scale_tonic = note_types[first_note_type_index]
        name_of_the_current_chord = first_interval_to_scale_tonic + ' ' + first_chord_type
        special_selection_path = 'Special Selection/' + normal_scale_name + '/' + name_of_the_current_chord + '.CHORD'
        second_note_type_index = extended_tonics_copy.index(second_chord_notes[0])
        second_interval_to_scale_tonic = note_types[second_note_type_index]
        name_of_the_next_chord = second_interval_to_scale_tonic + ' ' + second_chord_type
        existing_contents = []
        try:
            with open(special_selection_path, encoding='UTF-8') as opener:
                existing_contents = opener.read().splitlines()
        except FileNotFoundError:
            pass
        if name_of_the_next_chord not in existing_contents:
            with open(special_selection_path, 'a', encoding='UTF-8') as save_to_file:
                save_to_file.write(name_of_the_next_chord + '\n')
while True:
    mode = input('''0 - add good chord progressions you like
1 - try generating some progressions...
Choose mode: ''')
    if mode == '0':
        waiting_for_an_acceptable_chord = True
        chosen_chords = []
        while waiting_for_an_acceptable_chord:
            print('do not use flats, use sharps!')
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
                                for scale in scales:
                                    for tonic in tonics:
                                        assimilated_notes = []
                                        two_current_chords_assimilated = False
                                        scale_index = tonics.index(tonic)
                                        current_scale = []
                                        current_scale.append(tonic)
                                        for step in scale:
                                            scale_index += step
                                            current_scale.append(extended_tonics[scale_index])
                                        first_chord_notes = []
                                        if first_chord[0] == first_chord:
                                            first_tonic = tonics.index(first_chord)
                                            first_chord_type = 'major'
                                            for another_step in chord_type_major:
                                                first_index = note_types.index(another_step)
                                                current_note = first_tonic + first_index
                                                first_chord_notes.append(extended_tonics[current_note])
                                            if not two_current_chords_assimilated:
                                                for x in first_chord_notes:
                                                    assimilated_notes.append(x)
                                        else:
                                            first_tonic = tonics.index(first_chord[0])
                                            first_chord_type = first_chord.replace(tonics[first_tonic], '')
                                            for chord_type in known_chord_types:
                                                if first_chord_type == chord_type:
                                                    chord_type_index = known_chord_types.index(chord_type)
                                                    for another_step in actual_chord_types[chord_type_index]:
                                                        first_index = note_types.index(another_step)
                                                        current_note = first_tonic + first_index
                                                        first_chord_notes.append(extended_tonics[current_note])
                                                    if not two_current_chords_assimilated:
                                                        for x in first_chord_notes:
                                                            assimilated_notes.append(x)
                                        second_chord_notes = []
                                        if second_chord[0] == second_chord:
                                            second_tonic = tonics.index(second_chord)
                                            second_chord_type = 'major'
                                            for another_step in chord_type_major:
                                                second_index = note_types.index(another_step)
                                                current_note = second_tonic + second_index
                                                second_chord_notes.append(extended_tonics[current_note])
                                            if not two_current_chords_assimilated:
                                                for x in second_chord_notes:
                                                    assimilated_notes.append(x)
                                                two_current_chords_assimilated = True
                                        else:
                                            second_tonic = tonics.index(second_chord[0])
                                            second_chord_type = second_chord.replace(tonics[second_tonic], '')
                                            for chord_type in known_chord_types:
                                                if second_chord_type == chord_type:
                                                    chord_type_index = known_chord_types.index(chord_type)
                                                    for another_step in actual_chord_types[chord_type_index]:
                                                        second_index = note_types.index(another_step)
                                                        current_note = second_tonic + second_index
                                                        second_chord_notes.append(extended_tonics[current_note])
                                                    if not two_current_chords_assimilated:
                                                        for x in second_chord_notes:
                                                            assimilated_notes.append(x)
                                                        two_current_chords_assimilated = True
                                        special_selection()
                            chosen_chords_copy.remove(chord_x)
                    else:
                        print('sorry... I do not know such chords yet. Maybe something more simple?')
            else:
                print('sorry... I do not know such chords yet. Maybe something more simple?')
    if mode == '1':
        scale_order = ['Major', 'Natural Minor', 'Harmonic Minor', 'Pentatonic Major', 'Pentatonic Minor']
        type_order = ['major', 'm', 'sus2']
        chord_orders = []
        for aa_type in type_order:
            for aa_note in note_types:
                for_chord_order = aa_note + ' ' + aa_type
                chord_orders.append(for_chord_order)
        for a_scale in scale_order:
            for a_tonic in tonics:
                temp_scale_name = a_tonic + ' ' + a_scale
                for a_note in note_types:
                    for a_type in type_order:
                        try:
                            path = 'Special Selection/' + a_scale + '/' + a_note + ' ' + a_type + '.CHORD'
                            with open(path, encoding='UTF-8') as checker:
                                contents = checker.read().splitlines()
                            current_chain = []
                            first_chord_in_chain = a_note + ' ' + a_type
                            current_chain.append(first_chord_in_chain)
                            for aaa_chord in chord_orders:
                                if aaa_chord in contents:
                                    try:
                                        path = 'Special Selection/' + a_scale + '/' + aaa_chord + '.CHORD'
                                        with open(path, encoding='UTF-8') as checker:
                                            contents_2 = checker.read().splitlines()
                                        current_chain.append(aaa_chord)
                                        for aaaa_chord in chord_orders:
                                            if aaaa_chord in contents_2:
                                                try:
                                                    path = 'Special Selection/' + a_scale + '/' + aaaa_chord + '.CHORD'
                                                    with open(path, encoding='UTF-8') as checker:
                                                        contents_3 = checker.read().splitlines()
                                                    current_chain.append(aaaa_chord)
                                                    for aaaaa_chord in chord_orders:
                                                        if aaaaa_chord in contents_3:
                                                            try:
                                                                path = 'Special Selection/' + a_scale + '/' + aaaaa_chord + '.CHORD'
                                                                with open(path, encoding='UTF-8') as checker:
                                                                    contents_4 = checker.read().splitlines()
                                                                current_chain.append(aaaaa_chord)
                                                                for aaaaaa_chord in chord_orders:
                                                                    if aaaaaa_chord in contents_4:
                                                                        if aaaaaa_chord == first_chord_in_chain:
                                                                            forbidden = False
                                                                            for xxxxx in current_chain:
                                                                                repeats = current_chain.count(xxxxx)
                                                                                if repeats > 1:
                                                                                    forbidden = True
                                                                            if not forbidden:
                                                                                print('It is in', temp_scale_name, current_chain)
                                                                del current_chain[len(current_chain)-1]
                                                            except FileNotFoundError:
                                                                pass
                                                    del current_chain[len(current_chain) - 1]
                                                except FileNotFoundError:
                                                    pass
                                        del current_chain[len(current_chain) - 1]
                                    except FileNotFoundError:
                                        pass
                        except FileNotFoundError:
                            pass
