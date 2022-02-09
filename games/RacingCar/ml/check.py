import pickle
import os

with open("../log/ml_1_NORMAL_20_3_off_2022-02-09_14-24-50.pickle", "rb") as f:
    p = pickle.load(f)

print(p)
p = str(p)
txt = open(os.path.join(os.path.dirname(__file__),'pickleCheck'), 'wt')
txt.write(p)
txt.close()
