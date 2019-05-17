from mido import MidiFile, MidiTrack, Message, MetaMessage
import os
import sys


#  path=sys.argv[1]
#  Min_main=int(sys.argv[2])
#  Max_main=int(sys.argv[3])
#  Control=int(sys.argv[4])
#  Mild=sys.argv[5]

def process_audio(path, Min_main, Max_main, Control, Mild, save_path=""):
    def Initialize_Track(Instrument=1, Tempo=714280, Key='C'):
        Track = MidiTrack()
        Track.append(MetaMessage("track_name", name='Musicine', time=0))
        Track.append(MetaMessage('key_signature', key=Key, time=0))
        Track.append(Message('program_change', channel=0, program=Instrument, time=0))  # change the type of instrument
        # Track.append(MetaMessage("set_tempo", tempo=Tempo, time=0))
        return Track

    def Chord_Type(root, Type='M'):
        if (Type == 'M'):  # major triad
            return [root, root + 4, root + 7]
        elif (Type == 'm'):  # minor triad
            return [root, root + 3, root + 7]
        elif (Type == 'M7'):  # major seventh chord
            return [root, root + 4, root + 7, root + 11]
        elif (Type == 'm7'):  # minor seventh chord
            return [root, root + 3, root + 7, root + 10]
        elif (Type == 'dim'):  # dimished triad
            return [root, root + 3, root + 6, root + 9]
        elif (Tyie == 'aug'):
            return [root, root + 4, root + 8]

    def Add_Notes(Track, Category, Note, Time):
        if (Category == 'on'):
            if (Note >= Min_main and Note <= Max_main):
                Track.append(Message('note_on', channel=0, note=Note, velocity=90, time=Time))  # Main note
            else:
                Track.append(Message('note_on', channel=0, note=Note, velocity=48, time=Time))  # Assistant note
        elif (Category == 'off'):
            Track.append(Message('note_off', channel=0, note=Note, velocity=48, time=Time))  # End of note
        return Track

    Song = MidiFile(path)  # load the midi file
    for i, track in enumerate(Song.tracks):
        if (i == 0):
            Main_track = track  # the main track of midi music
    Onoff_track = [str(x).split(' ') for x in Main_track if str(x)[:5] == 'note_'][:-1]
    Category, Note, Time = [x[0][5:] for x in Onoff_track], [int(x[2][5:]) for x in Onoff_track], [int(x[-1][5:]) for x
                                                                                                   in Onoff_track]
    Track = Initialize_Track()

    '''
    First attempt:To eliminate the note larget then 84 or less then 36
    '''

    Invalid = 0
    Step_one = []
    for x in range(len(Category)):
        if (Note[x] < 40 or Note[x] > 80):
            Invalid += Time[x]
        else:
            Step_one.append([Category[x], Note[x], Time[x] + Invalid])
            Invalid = 0
    for i in range(len(Step_one)):
        if (Step_one[i][2] != 0):
            start = i + 1
            while (start < len(Step_one) - 1 and Step_one[start][2] == 0):
                start += 1
            Step_one[i][1] = Step_one[start - 1][1]
    Step_one[0][2] = min([Step_one[0][2], 100])
    Step_one = [x for x in Step_one if x[2] >= Control * 0.25]
    '''
    Second attempt
    '''
    if (Mild == 'Y'):
        y = [x[1] for x in Step_one]
        time = [x[2] for x in Step_one if x[2] != 0]
        x = [0 for _ in range(sum(time))]
        index = 0
        for i in range(len(time)):
            for j in range(index, index + time[i]):
                x[j] = y[i]
            index += time[i]
        i = 0
        while (i < sum(time) - Control - 1):
            L = x[i:i + Control]
            if (L.count(L[0]) != len(L)):
                right = Control - 1
                while (right > 0 and L[-1] == L[right]):
                    right -= 1
                for j in range(right + 1):
                    x[i + j] = L[0]
            i += Control // 2
        i, start, Step_two = 1, 0, []
        while (i < sum(time) - 1):
            while (x[i] == x[start] and i < sum(time) - 1):
                i += 1
            Step_two.append(['on', x[start], i - start - 1])
            start = i
        Final = []
        for x in Step_two:
            Final.append([x[0], x[1], x[2]])
            Final.append(['off', x[1], 0])
    else:
        Final = []
        for x in Step_one:
            Final.append([x[0], x[1], x[2]])
            Final.append(['off', x[1], 0])
    for x in Final:
        Add_Notes(Track, x[0], x[1], x[2])
    Music = MidiFile()
    Music.tracks.append(Track)
    if save_path == "":
        pure_path = os.path.split(path)
        pure_name = pure_path[1].split('.')
        save_path = os.path.join(pure_path[0], pure_name[0]) + "-processed.mid"
    Music.save(save_path)
    return save_path


if __name__ == "__main__":
    process_audio(r"E:\FileRec\white.mid", 60, 534, 72, "N")
