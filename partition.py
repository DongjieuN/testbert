import numpy as np; np.random.seed(1234)
import pandas as pd

ntrain = 150000

# 파일 경로는 실제 파일 위치에 따라 변경해야 합니다.
data = pd.read_csv('../ratings.txt', sep='\t', header=None, names=['document', 'label'])
data = pd.DataFrame(np.random.permutation(data))
trn, tst = data[:ntrain], data[ntrain:]

header = ['document', 'label']
trn.to_csv('../ratings_train.txt', sep='\t', index=False, header=header)
tst.to_csv('../ratings_test.txt', sep='\t', index=False, header=header)

