#coding: utf8
"""
@author: zhaoshuang
"""
import pandas as pd
file = open("FinalCombinedResult.csv",encoding="latin")

FinalResult = pd.read_csv(file,
            names=["Labelcv2","Labelcv1","Label","NewId","ID","Date","Events"])
#FinalResult = FinalResult.drop([0])
label2 = list(FinalResult['Labelcv2'][1:])
label1 = list(FinalResult['Labelcv1'][1:])
label0 = list(FinalResult['Label'][1:])
newId = list(FinalResult['NewId'][1:])
ID = list(FinalResult['ID'][1:])
date = list(FinalResult['Date'][1:])
event = list(FinalResult['Events'][1:])
label3 = []
wrong = []
for i in range(len(label2)):
  if label0[i] == label1[i] == label2[i]:
    label3.append(label0[i])
  # elif label0[i] == label2[i]:
  #   label3.append(label0[i])
  # elif label1[i] == label2[i]:
  #   label3.append(label1[i])
  else:
    label3.append('False')
out = {'Label3':label3, 'Labelcv2':label2, 'Labelcv1':label1, 'Label':label0, 'NewId':newId, 'ID':ID, 'Date':date, 'Events':event}
df = pd.DataFrame(data = out, columns = ["Label3","Labelcv2","Labelcv1","Label","NewId","ID","Date","Events"])
df.to_csv('ultiResult2.csv')
c = 0
for i in label3:
  if i == 'False':
    c += 1