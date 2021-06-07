import os
import csv
import sys
import string


class Vertex:
    name = None
    index = -1
    shortest_distance = sys.maxsize

    def __init__(self, name, index, distance):
        self.name = name
        self.index = index
        self.shortest_distance = distance
        return

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_shortest_distance(self):
        return self.shortest_distance

    def set_shortest_distance(self, new_distance):
        self.shortest_distance = new_distance
        return

    def print(self):
        print("name:", self.name, ", distance:", self.shortest_distance)


def dijkstra(adj_matrix, start_index):
    n = len(adj_matrix)

    s_set = []
    u_set = []

    for i in range(0, n):

        v = Vertex(string.ascii_uppercase[i], i, sys.maxsize)

        if i == start_index:
            print("Start:", v.get_name())
            v.set_shortest_distance(0)
            s_set.append(v)
        else:
            distance_to_start = int(adj_matrix[i][start_index])
            if distance_to_start > 0:
                v.set_shortest_distance(distance_to_start)
            u_set.append(v)

    while len(s_set) < n:
        u_set.sort(key=lambda x: x.shortest_distance, reverse=False)

        nearest_v = u_set[0]

        s_set.append(nearest_v)
        u_set.remove(nearest_v)

        for uv in u_set:
            uv_index = uv.get_index()
            current_distance = uv.get_shortest_distance()

            nearest_index = nearest_v.get_index()

            if int(adj_matrix[nearest_index][uv_index]) > 0:
                new_distance = int(adj_matrix[nearest_index][uv_index])

                if new_distance < 0:
                    new_distance = sys.maxsize
                else:
                    new_distance += nearest_v.get_shortest_distance()

                if new_distance < current_distance:
                    current_distance = new_distance

                uv.set_shortest_distance(current_distance)

    for v in s_set:
        v.print()

    return


def process_file(file_name, index):
    print("\nProcessing:", file_name)
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_name)
    data = list(csv.reader(open(file_path)))
    dijkstra(data, index)
    return


process_file("d_data_1.csv", 3)
process_file("d_data_2.csv", 0)