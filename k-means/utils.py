import random
import math

iris_array = []


def read_data(path):
    with open(path) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            line = line[:-2]
            iris_array.append(line)
        # print(iris_array)


def choose_random_center(k):
    random_centers = []
    for i in range(k):
        random_num = random.uniform(4.5, 7)
        random_num2 = random.uniform(2.3, 4.2)
        random_num3 = random.uniform(1.0, 6.9)
        random_num4 = random.uniform(0.1, 2.5)
        randomm = [random_num, random_num2, random_num3, random_num4]
        random_centers.append(randomm)
    # print(random_centers)
    return random_centers




def euclidian_distance(array1, array2, feature_num):

    distance = 0
    if(len(array1) == len(array2)):
        for i in range(feature_num):
           distance = distance + (array1[i] - array2[i]) ** 2
        distance =math.sqrt(distance)
        # print(distance)
    return distance


def mean_of_cluster(cluster, feature_size):
    mean = []
    for i in range(feature_size):
        sum = 0
        for j in range(len(cluster)):
            sum = sum + cluster[j][i]
        if(len(cluster)):
            mean.append(sum / len(cluster))
    print(mean)
    return mean


def parse_array():
    new_array = []
    splitting = []
    for i in range(len(iris_array)):
        splitting = iris_array[i].split(",")
        splitting = splitting[:-1]
        new_array.append(splitting)
    new_array = [[float(y) for y in x] for x in new_array]

    return new_array
