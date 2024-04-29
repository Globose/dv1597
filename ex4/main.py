import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

PATH_PEOPLE = 'Ex4_Dataset/Ex4/People/'
PATH_TEST = 'Ex4_Dataset/Ex4/Test/'

def distance(m1, m2, s1, s2):
    """Calculates euclidian distance"""
    tot = (m1-m2)**2+(s1-s2)**2
    return round(tot**0.5,4)

def step_1(write=True):
    """Calculates mean and std for all people-images"""
    people = os.listdir(PATH_PEOPLE)
    people_dict = {}

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

        mean = round(np.mean(mean_list),4)
        std = round(np.mean(std_list),4)
        people_dict[p] = (mean,std,mean_list, std_list)

    if write:
        print("-----"*10)
        print("Step 1")
        print('{:<15s} {:<15s} {:<15s}'.format("Person", "Mean", "Standard deviation"))
        for p in people_dict.items():
            print('{:<15s} {:<15s} {:<15s}'.format(p[0], str(p[1][0]), str(p[1][1])))
        print("-----"*10)

    return people_dict

def step_2(write=True):
    """Calculates mean and std for Test images"""
    test_imgs = os.listdir(PATH_TEST)
    for i,img_name in enumerate(test_imgs):
        img = cv2.imread(PATH_TEST+img_name)
        height, width, channels = img.shape

        array = []
        for x in range(width):
            for y in range(height):
                array.append(img[y,x][0])

        mean = round(np.mean(array),4)
        std = round(np.std(array),4)
        test_imgs[i] = (img_name,mean,std)

    if write:
        print("-----"*10)
        print("Step 2")
        print('{:<15s} {:<15s} {:<15s}'.format("Image", "Mean", "Standard deviation"))
        for t in test_imgs:
            print('{:<15s} {:<15s} {:<15s}'.format(t[0], str(t[1]), str(t[2])))
        print("-----"*10)
    return test_imgs

def step_3(people, test_imgs):
    """Calculates distance of each Test image"""
    labels = list(people.keys())
    true_labels = ('Andreas','Marie','Mikael','Stefan','Ulf')

    # Prints result
    print('-----'*25)
    print('{:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'
          .format("Image", labels[0], labels[1], labels[2], labels[3], labels[4], "Predicted as", "True Label"))
    print('-----'*25)
    for i, img in enumerate(test_imgs):
        img_name = img[0]
        img_mean = img[1]
        img_std = img[2]

        res = []
        for name in labels:
            dist = distance(img_mean, people[name][0], img_std, people[name][1])
            res.append((dist, name))
        predicted = min(res)[1]
        print('{:<15s} {:<15f} {:<15f} {:<15f} {:<15f} {:<15f} {:<15s} {:<15s}'
            .format(img_name, res[0][0], res[1][0], res[2][0], res[3][0], res[4][0], predicted, true_labels[i]))
    print('-----'*25)

def plot(people):
    """Creates a scattered plot of the result"""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Mean Intensity Value')
    ax.set_ylabel('Standard Deviation')
    colors = ('Red', 'Green', 'Blue', 'Purple', 'Black')

    for i, item in enumerate(list(people.items())):
        name = item[0]

        mean = item[1][0]
        std = item[1][1]
        mean_values = item[1][2]
        std_values = item[1][3]

        ax.scatter(mean_values,std_values, label=name, c=colors[i])
        ax.scatter(mean,std, label=name+' mean', marker='x', c=colors[i])

    ax.grid()
    ax.legend()
    plt.show()

def main():
    """Main function"""
    people = step_1(write=False)
    test_imgs = step_2(write=False)
    step_3(people, test_imgs)
    plot(people)

if __name__ == '__main__':
    main()