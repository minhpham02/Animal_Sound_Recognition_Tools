import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd



def funcRMSE(tool1_file):
    tool1, sr = librosa.load(tool1_file, duration = 3)
    #tool1, sr = librosa.load(tool1_file, duration = 10, offset=32)
    FRAME_SIZE = 1024
    HOP_LENGTH = 512
    rms = librosa.feature.rms(y=tool1, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0] #RMS là mảng năng lượng trung bình mặc định mà Librosa trả về


    arr = np.array_split(rms, 3) 
    result = []
    result = [0 for i in range(3)]
    window = 0

    #-----------------------Difference Percentage------------
    for i in range(len(arr)):
        sum = 0
        count = 0
        for j in range(len(arr[i])-1):
            if(arr[i][j] != 0):
                sum += ((abs(arr[i][j] - arr[i][j+1]))/arr[i][j])*100 #TBC hiệu 2 giá trị cạnh nhau / giá trị tiếp theo để tính xem
                                                                        #năng lượng trung bình ở giá trị tiếp theo lệch bn % so với giá trị hiện tại
            else:
                sum += 0
            #print(sum)
            count += 1
        #print(count)
        avg = sum/count
        result[window] = avg
        window += 1
    return result

#----------------------Average Window--------------------
# for i in range(len(arr)):
#     sum = 0
#     count = 0
#     for j in range(len(arr[i])):
#         sum += arr[i][j]
#         count += 1
#     avg = sum/count
#     result[window] = avg
#     window += 1
