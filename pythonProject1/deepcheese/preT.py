import numpy as np
import h5py, os, cv2
import matplotlib.pyplot as plt

base_path = './dataset/original'

train_data = h5py.File(os.path.join(base_path, 'train_happy.h5'), 'r')
x_train = np.array(train_data['train_set_x'][:])
y_train = np.array(train_data['train_set_y'][:])

test_data = h5py.File(os.path.join(base_path, 'test_happy.h5'), 'r')
x_test = np.array(test_data['test_set_x'][:])
y_test = np.array(test_data['test_set_y'][:])

y_train = y_train.reshape((y_train.shape[0], 1))
y_test = y_test.reshape((y_test.shape[0], 1))

np.save('dataset/x_train_color.npy', x_train)
np.save('dataset/x_test_color.npy', x_test)

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

plt.subplot(2, 2, 1)
plt.title(y_train[0])
plt.imshow(x_train[0])
plt.subplot(2, 2, 2)
plt.title(y_train[1])
plt.imshow(x_train[1])
plt.subplot(2, 2, 3)
plt.title(y_test[0])
plt.imshow(x_test[0])
plt.subplot(2, 2, 4)
plt.title(y_test[1])
plt.imshow(x_test[1])

x_result = []
for x in x_train:
    img = cv2.cvtColor(x, cv2.COLOR_RGB2GRAY)
    x_result.append(img)

x_result = np.array(x_result)
np.save('dataset/x_train.npy', x_result)

x_result = []
for x in x_test:
    img = cv2.cvtColor(x, cv2.COLOR_RGB2GRAY)
    x_result.append(img)

x_result = np.array(x_result)
np.save('dataset/x_test.npy', x_result)

np.save('dataset/y_train.npy', y_train)
np.save('dataset/y_test.npy', y_test)