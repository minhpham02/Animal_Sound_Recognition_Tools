import sys
import numpy as np
from aubio import source, pitch



def funcPitch(path, pitch):
    win_s = 4096 #kích thước cửa sổ lấy mẫu
    hop_s = 512 #bước nhảy

    samplerate = 44100 #tần số lấy mẫu
    s = source(path, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8 #sai số cho phép

    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    total_frames = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        pitches += [pitch]
        confidence = pitch_o.get_confidence()
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break

    result = []

    #print(len(pitches))
    step = int(len(pitches)/3)

    for i in range(0, 3, 1):
        max = step*(i+1)
        if(i == 2):
            max = len(pitches) - 1
        pitchLocal = []
        for j in range(step*i, max, 1):
            pitchLocal.append(pitches[j])
        result.append(np.array(pitchLocal).mean())  # tính trung bình

    # print("Average frequency = " + str(np.array(pitches).mean()) + " hz")
    # print(len(result))
    # print(result)
    return result
#print(funcPitch()