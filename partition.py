import pandas as pd

# 파일 경로는 실제 파일 위치에 따라 변경하세요.
train = pd.read_csv("testbert/ratings_train.txt", sep='\t', header=None, names=['document', 'label'])
test = pd.read_csv("testbert/ratings_test.txt", sep='\t', header=None, names=['document', 'label'])

print(train)
print(test)
