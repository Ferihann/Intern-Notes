from util import *
import numpy

read_data("iris.data")
iris_unsupervised = parse_array()
random_centers = choose_random_center(3)
# print(iris_unsupervised)
cluster1 = []
cluster2 = []
cluster3 = []

clusters = cluster1, cluster2, cluster3


def calculate_distance_from_random_centers(arr, feature_num):
    distances = []
    for i in range(len(random_centers)):
        distances.append(euclidian_distance(arr, random_centers[i], feature_num))
    return distances


def clustering():
    len_array = len(iris_unsupervised)
    for i in range(len_array):
        distances = calculate_distance_from_random_centers(iris_unsupervised[i], 4)
        nearest_point = distances.index(min(distances))
        clusters[nearest_point].append(iris_unsupervised[i])
    i = 1
    while relocate_the_points(len_array) != -1:
        i = i+1
        relocate_the_points(len_array)
        print("iiiii", i)


def relocate_the_points(len_array):
    len_clust = len(clusters)

    for i in range(len_clust):
        mean = mean_of_cluster(clusters[i], 4)
        if mean == random_centers[i]:
            return -1
        random_centers[i] = mean

    for i in range(len_array):
        distance = euclidian_distance(random_centers, iris_unsupervised[i], 4)

        if distance > 0:
            nearest_point = distance.index(min(distance))

            if iris_unsupervised[i] in clusters[nearest_point]:
                pass
            else:
                for i in clusters:
                    if iris_unsupervised[i] in clusters[i]:
                        clusters[i].remove(iris_unsupervised[i])
                        break
            clusters[nearest_point].append(iris_unsupervised[i])


def control_does_mean_change(previous_mean, current_mean):
    return previous_mean == current_mean


clustering()
print(cluster1)
print(cluster2)
print(cluster3)

