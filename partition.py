import pandas as pd

# 가정: 각 줄은 탭으로 구분된 document와 label 정보를 가지고 있음
data = pd.read_csv('파일경로.txt', sep='\t', header=None, names=['document'])

# document 열에서 마지막 문자(라벨 정보) 분리
data['label'] = data['document'].str[-1].astype(int)
data['document'] = data['document'].str[:-2]

print(data)

