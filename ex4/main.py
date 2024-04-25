import os
import numpy as np
import cv2

PATH_PEOPLE = 'Ex4_Dataset/Ex4/People/'
PATH_TEST = 'Ex4_Dataset/Ex4/Test/'

def distance(m1, m2, s1, s2):
    tot = (m1-m2)**2+(s1-s2)**2
    return tot**0.5

def step_1():
    people = os.listdir(PATH_PEOPLE)
    pdict = {}

    for i,p in enumerate(people):
        img_paths = os.listdir(PATH_PEOPLE+p)

        std_list = []
        mean_list = []

        for path in img_paths:
            img = cv2.imread(PATH_PEOPLE+p+'/'+path)
            height, width, channels = img.shape

            array = []
            for x in range(width):
                for y in range(height):
                    array.append(img[y,x])

            mean_list.append(np.mean(array))
            std_list.append(np.std(array))

        mean = str(round(np.mean(mean_list),4))
        std = str(round(np.mean(std_list),4))
        pdict[p] = (mean,std)

    print("-----"*10)
    print("Step 1")
    print('{:<15s} {:<15s} {:<15s}'.format("Person", "Mean", "Standard deviation"))
    for p in pdict.items():
        print('{:<15s} {:<15s} {:<15s}'.format(p[0], p[1][0], p[1][1]))
    print("-----"*10)



    return people

def step_2():
    test_imgs = os.listdir(PATH_TEST)
    for i,img_name in enumerate(test_imgs):
        img = cv2.imread(PATH_TEST+img_name)
        height, width, channels = img.shape

        array = []
        for x in range(width):
            for y in range(height):
                array.append(img[y,x][0])

        mean = str(round(np.mean(array),4))
        std = str(round(np.std(array),4))
        test_imgs[i] = (img_name,mean,std)


    print("-----"*10)
    print("Step 2")
    print('{:<15s} {:<15s} {:<15s}'.format("Image", "Mean", "Standard deviation"))
    for t in test_imgs:
        print('{:<15s} {:<15s} {:<15s}'.format(t[0], t[1], t[2]))
    print("-----"*10)
    return test_imgs

def step_3(people, test_imgs):
    labels = ('Andreas', 'Marie', 'Mikael', 'Stefan', 'Ulf')
    print('{:<15s} {:<15s} {:<15s}'.format("Image", labels[0], labels[1], labels[2], labels[3], labels[4], "Predicted as", "True Label"))
    for i, img in enumerate(test_imgs):
        distance(img[1])



if __name__ == '__main__':
    people = step_1()
    test_imgs = step_2()
    step_3(people, test_imgs)