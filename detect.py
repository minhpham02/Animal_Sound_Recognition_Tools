from Pitch import funcPitch
from aubio import pitch
from RMSE import funcRMSE
from PercentSilence import funcPercentSilence
from FrequencyMagnitude import funcFrequencyMagnitude

### % phần trăm khoảng lặng 0,1
### độ lệch năng lượng 0,3
### pitch 0,3
### tần số có mật độ lớn nhất 0,3
from attribute import toolInstrumentVoice
from result import pathAndResult

configPercentSilence = 0.1
configRMSE = 0.3
configPitch = 0.3
configFrequencyMagnitude = 0.3

def compareFile(att1, att2): 
    maxRes = 1
    for i in range(3):
        for j in range(3):
            # giongnhau
            same = float(abs(att1[i].percentSilence - att2[j].percentSilence) / max(att1[i].percentSilence, att2[j].percentSilence) * configPercentSilence)
            same = same + float(abs(att1[i].RMSE - att2[j].RMSE) / max(att1[i].RMSE, att2[j].RMSE) * configRMSE)
            if (max(att1[i].pitch, att2[j].pitch) == 0):
                same = same + 0
            else:    
                same = same + float(abs(att1[i].pitch - att2[j].pitch) / max(att1[i].pitch, att2[j].pitch) * configPitch)
            same = same + float(abs(att1[i].magnitude - att2[j].magnitude) / max(att1[i].magnitude, att2[j].magnitude) * configFrequencyMagnitude / 2)
            same = same + float(abs(att1[i].frequency - att2[j].frequency) / max(att1[i].frequency, att2[j].frequency) * configFrequencyMagnitude / 2)
            if(maxRes > same):
                maxRes = same
    
    return maxRes
    
###################################### dữ liệu có trong bộ ###########################
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim chào mào/chao_mao_1.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim chòe lửa/choe_lua_7.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim chòe than/choe_than_3.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim họa mi/hoa_mi_4.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim hút mật 5 màu/Hut_mat_5.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim khiếu/khieu_6.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/chim sâu xanh/sau_xanh_7.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim sẻ/Chim_se_8.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim sơn ca/Chim_Son_Ca_9.wav"
path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh/Chim yến/chim_yen_10.wav"

###################################### dữ liệu không có trong bộ ###########################  
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/choe_than_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/chim_khiếu_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/chim_se_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/Chim_Son_Ca_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/chim_yen_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/choe_lua_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/hoa_mi_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/sau_xanh_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/chim_hut_mat_5_mau_test.wav"
#path = "C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File test/chao_mao_test.wav"

att1 = [] 

pitchAtt = funcPitch(path, pitch)
RMSEAtt = funcRMSE(path)
percentSilenceAtt = funcPercentSilence(path)
frequencyMagnitudeAtt = funcFrequencyMagnitude(path)

magnitudeAtt = []
frequencyAtt = []

for a, b in frequencyMagnitudeAtt:
    magnitudeAtt.append(a)
    frequencyAtt.append(b)

for i in range(3):
    att1.append(
        toolInstrumentVoice(
            pitchAtt[i],
            RMSEAtt[i],
            percentSilenceAtt[i],
            magnitudeAtt[i],
            frequencyAtt[i]
        )
    )
    # print (pitchAtt[i], RMSEAtt[i], percentSilenceAtt[i], magnitudeAtt[i], frequencyAtt[i])s

####################################### get data csv #######################
import csv

with open('C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/CSDLDPT.csv', 'r', encoding='UTF8') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
    metadata = []
    for row in range(len(l)):
        if row > 1 and row %2 == 0 :
            metadata.append(l[row])


lastResult = []
for i in range(len(metadata)):
    att = []

    Pitch = metadata[i][1].strip("[]").split(', ')
    RMSE = metadata[i][2].strip("[]").split(', ')
    PercentSilence = metadata[i][3].strip("[]").split(', ')
    frequencyMagnitudeAtt = metadata[i][4].strip("[]").replace("(", "").replace(")", "").split(', ')

    magnitudeAtt = []
    frequencyAtt = []
    for e in range(6):
        if e % 2 == 1:
            frequencyAtt.append(frequencyMagnitudeAtt[e])
        else:
            magnitudeAtt.append(frequencyMagnitudeAtt[e])

    for j in range(3):
        att.append(
            toolInstrumentVoice(
                float(Pitch[j]),
                float(RMSE[j]),
                float(PercentSilence[j]),
                float(magnitudeAtt[j]),
                float(frequencyAtt[j])
            )
        )

    lastResult.append(
        pathAndResult(
            "Type: " + metadata[i][0].split('/')[9],
            compareFile(att1, att)
        )
    )

#### result
    
for i in range(100):
    for j in range(100):
        if(lastResult[i].distance < lastResult[j].distance):
            swap = lastResult[i]
            lastResult[i] = lastResult[j]
            lastResult[j] = swap

print(lastResult[0].type, lastResult[0].distance)
print(lastResult[1].type, lastResult[1].distance)
print(lastResult[2].type, lastResult[2].distance)
# print(lastResult[3].type, lastResult[3].distance)
# print(lastResult[4].type, lastResult[4].distance)

# att2 = []
# att2.append(toolInstrumentVoice(41.0105, 52.480352808569755, 18.498866213151928, 6044, 752.2972848700547))
# att2.append(toolInstrumentVoice(80.53759, 6.295327728661332, 48.49433106575963, 25529, 144.3187829958743))
# att2.append(toolInstrumentVoice(78.17408, 3.6278046603824587, 47.73242630385488, 45436, 66.06745432748225))
# att2.append(toolInstrumentVoice(79.63045, 3.843097218001882, 48.29478458049886, 70831, 37.561908261746865))
# att2.append(toolInstrumentVoice(78.884094, 7.780515449953133, 49.88208616780045, 108914, 66.06745432748225))
# att2.append(toolInstrumentVoice(80.22667, 5.244177334922521, 49.55555555555555, 128821, 144.3187829958743))
# att2.append(toolInstrumentVoice(80.14571, 7.7701177481295804, 45.35514878292073, 148306, 752.2972848700547))

# print(compareFile(att1, att2))