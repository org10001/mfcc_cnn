
batch_size = 500

print_interval = 1000

step_num0 = 30000

step_num1 = 30000

step_num2 = 30000

step_num3 = 0

learning_rate0 = 0.05

learning_rate1 = 0.03

learning_rate2 = 0.01

learning_rate3 = 1e-4

visible_device = '3'

save_checkpoint_interval = 1000

checkpoint_file = './my-model/my-model'

# data_path = '/home/dai/Projects/emotions/data'
#
#
#
# label_file = './trim_labels_1.txt'
#
#
#
# continue_eles = 50
#
# train_rate = 0.7
#
# classes_pickle = './pickles/classes.pickle'

gt_pickle = './pickles/gt_n200.pickle'

pr_pickle = './pickles/pr_n200.pickle'

# device = '/gpu:0'


# input matrix n * 39
mfcc_n = 200

cnn_kernel1_shape = [5, 5, 1, 16]

cnn_kernel2_shape = [5, 5, 16, 32]

fc1_fs = 512

# n_classes = 6

# classes = ['ang', 'exc', 'fru', 'hap', 'neu', 'sad']
classes = ['neu', 'ang', 'hap', 'sad']

train_d_npy = './train_data_n200_s40.npy'

train_l_npy = './train_l_n200_s40_1hot.npy'

test_d_npy = './test_data_n200_s40.npy'

test_l_npy = './test_l_n200_s40_1hot.npy'
