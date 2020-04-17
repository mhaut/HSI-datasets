import copy
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio


gtindian_dist = sio.loadmat("indianpines_disjoint_dset.mat")['indianpines_disjoint_dset']
y_test = sio.loadmat("indian_pines_gt.mat")['indian_pines_gt']
y_train2 = sio.loadmat("indianpines_disjoint_dset.mat")['indianpines_disjoint_dset']
y_test = y_test.astype("uint8")
changes = [0,2,3,5,6,8,10,11,12,14,1,4,7,9,13,15,16]
y_train = copy.deepcopy(y_train2)

for i,val in enumerate(changes): y_train[y_train2==i] = val

y_test[y_train!=0] = 0


plt.imshow(y_train, cmap="gist_ncar_r", vmin=0)
plt.imshow(y_test, cmap="gist_ncar_r", vmin=0, alpha=0.25)
plt.show()
