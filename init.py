from Pitch import funcPitch
from aubio import pitch
from RMSE import funcRMSE
from PercentSilence import funcPercentSilence
from FrequencyMagnitude import funcFrequencyMagnitude


# >>> pairs = [("a", 1), ("b", 2), ("c", 3)]
# >>> for a, b in pairs:
# ...    print a, b
# ... 
# a 1
# b 2
# c 3

# print('=====Pitch=====')
# print(funcPitch(path, pitch))
# print('=====RMSE=====')
# print(funcRMSE(path))
# print('=====PercentSilence=====')
# print(funcPercentSilence(path))
# print('=====FrequencyMagnitude=====')
# print(funcFrequencyMagnitude(path))
######################################################
import os
# get subpath
listsubpath = []
for x in os.walk("C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/File âm thanh"):
    listsubpath.append(x[0].replace("\\", "/"))
listsubpath.pop(0)

# get files
allpath = []
for subpath in listsubpath:
    f = []
    for (dirpath, dirnames, filenames) in os.walk(subpath):
        f.extend(filenames)
        break
    for namefile in f:
        allpath.append(subpath + "/" + namefile)

# write to csv
import csv

with open('C:/Users/ADMIN/Downloads/Animal_Sound_Recognition_Tools/Animal_Sound_Recognition_Tools/src/CSDLDPT.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    header = ['Path', 'Pitch', 'RMSE', 'PercentSilence', 'FrequencyMagnitude']
    writer.writerow(header)
    
    for path in allpath:
        try:
            data = [
                path, 
                funcPitch(path, pitch), 
                funcRMSE(path), 
                funcPercentSilence(path),
                funcFrequencyMagnitude(path)
            ]
            writer.writerow(data)   
        except:
            print("======" + path)
            print('Have exception')