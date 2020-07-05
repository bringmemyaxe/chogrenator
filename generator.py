known_chord_types = ['m', 'sus2', 'major']
while True:
    mode = input('''0 - add good chord progressions you like
Choose mode: ''')
    if mode == '0':
        waiting_for_an_acceptable_chord = True
        chosen_chords = []
        while waiting_for_an_acceptable_chord:
            temp_chord = input('add the first chord of your progression: ')
            if temp_chord[0] == temp_chord:
                chosen_chords.append(temp_chord)
            else:
                chord_type = temp_chord.replace(temp_chord[0], '')
                if chord_type in known_chord_types:
                    chosen_chords.append(temp_chord)
                    waiting_for_an_acceptable_chord = False
                    second_chord_added = False
                    while not second_chord_added:
                        temp_chord = input('add the next chord: ')
                        if temp_chord[0] == temp_chord:
                            chosen_chords.append(temp_chord)
                        else:
                            chord_type = temp_chord.replace(temp_chord[0], '')
                            if chord_type in known_chord_types:
                                chosen_chords.append(temp_chord)
                                second_chord_added = True
                                progression_finished = False
                                while not progression_finished:
                                    temp_chord = input('if there is another chord, add it. If there are no chords any more, write X: ')
                                    if temp_chord == 'X':
                                        progression_finished = True
                                    else:
                                        if temp_chord[0] == temp_chord:
                                            chosen_chords.append(temp_chord)
                                        else:
                                            chord_type = temp_chord.replace(temp_chord[0], '')
                                            if chord_type in known_chord_types:
                                                chosen_chords.append(temp_chord)
                                            else:
                                                print('sorry... I do not know such chords yet. Maybe something more simple?')
                            else:
                                print('sorry... I do not know such chords yet. Maybe something more simple?')
                else:
                    print('sorry... I do not know such chords yet. Maybe something more simple?')
