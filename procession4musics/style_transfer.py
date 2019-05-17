'''
Main program
Function: to transfer the style of midi music
Steps:Predicting(with trained models),Strengthen(with music theory)
'''

from keras.models import load_model
import numpy as np
from music_theory import Main_Process
from midi_player import Export_Midi,Note_Split
import deal_with_midi
import sys


def Predicting(Musician, OriginalTrack):
    model = load_model("Models/%s.hdf5" % (Musician))
    Input = OriginalTrack.reshape(1, 900, 1)  # the shape of input data: 1 sample * 900 dimension * 1 filter
    Output = model.predict(Input)
    Start, Duration = Output[3][0][:300], Output[3][0][600:]
    Start, Duration = [x[0] for x in Start], [x[0] for x in Duration]
    New_track = np.concatenate([Start, OriginalTrack[300:600], Duration])  # Ignore the note data of model output
    return New_track


def Transfer(vector,style,path):
    print('Data preprocessing...')
    Track = np.array(deal_with_midi.Main_Process(vector, Type=2))  # preprocessing data
    Entire_track = [[0, '0', 0] for _ in range(len(Track) * 300)]
    print('Predicting with CycleGAN model...\n')
    for x in range(len(Track)):
        New_track = Predicting(style, Track[x])
        New_track, Lefthand_track = Main_Process(style, Track[x], New_track)
        Entire_track[x * 300:x * 300 + 300] = New_track
        print('Finishing parts %d / %d' % (x + 1, len(Track)))
    print('Saving to Output.mid...')
    #Export_Midi('Output.mid', Entire_track)
    Note_Split(Entire_track,path)
    print('Success!')

if __name__=='__main__':
    Transfer('1-refrain.mid','V.K','bugggg.mid')