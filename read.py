import numpy as np
def read(file):
    hexs = []
    with open(file) as f:
        line = f.read()
        line = line.splitlines()
        for i in range(len(line)):
            hexs.append(line[i])
    return hexs
    #print(rgb[0])
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
def hex2rgb(string_num):
    rgb=[hex2dec(string_num[0:2]),hex2dec(string_num[2:4]),hex2dec(string_num[4:6])]
    return rgb     



#rgb是一个list，里面是代表r g b的一个list
#rgb_chs和rgb_jap是两个list分别保存了中国的颜色rgb list 和 日本的颜色rgb list
#下面我将考虑做一个sigmoid分类器，建立任意一个颜色是偏向中国传统还是日本传统
#下一步是好标签 日本用1 中国用0


#print(rgbs_chs)
# for i in range(len(rgb)):
#    label.append(1)
# #print(label)
# y = dict(zip(rgb,label))
# print(y)
def load_data_set():
    label = []
    rgbs_jap = []
    hexs = read('rgb.txt')
    for i in range(len(hexs)):
        rgbs_jap.append(hex2rgb(hexs[i]))
    #print(rgbs_jap)
    rgbs_chs = []
    hexs_chs = read('rgb_chs.txt')
    for i in range(len(hexs_chs)):
        rgbs_chs.append(hex2rgb(hexs_chs[i]))
    X_train_data_set_jp = np.array(rgbs_jap[0:200],dtype=np.int) #(200,3) 使用时应该转秩使用
    Y_train_data_set_jp = np.zeros([200,1],dtype=np.int)+1#（200，1）
    X_train_data_set_ch = np.array(rgbs_chs[0:500],dtype=np.int)#(500,3)
    Y_train_data_set_ch = np.zeros([500,1],dtype=np.int)
    X_train_data_set = np.hstack((X_train_data_set_jp.T,X_train_data_set_ch.T))
    Y_train_data_set = np.vstack((Y_train_data_set_jp,Y_train_data_set_ch))
    X_test_data_set_jp = np.array(rgbs_jap[200:],dtype=np.int) #(50,3) 使用时应该转秩使用
    Y_test_data_set_jp = np.zeros([50,1],dtype = np.int)+1#（50，1）
    X_test_data_set_ch = np.array(rgbs_chs[500:],dtype=np.int)#(26,3)
    Y_test_data_set_ch = np.zeros([26,1],dtype=np.int)
    X_test_data_set = np.hstack((X_test_data_set_jp.T,X_test_data_set_ch.T))
    Y_test_data_set = np.vstack((Y_test_data_set_jp,Y_test_data_set_ch))
    return X_train_data_set,Y_train_data_set,X_test_data_set,Y_test_data_set