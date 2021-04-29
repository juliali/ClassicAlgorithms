import queue
import os
import csv


def is_undirected_graph_circled(adj_matrix):
    n = len(adj_matrix)
    degrees =  [0] * n
    visited = []
    q = queue.Queue()
    for i in range(0, n):
        degrees[i] = sum([int(value) for value in adj_matrix[i]])
        if degrees[i] <= 1:                                           
            q.put(i)
            visited.append(i)
        
    while not q.empty():
        i = q.get()
        for j in range(0, n):
            if int(adj_matrix[i][j]) == 1:
                degrees[j] -= 1
                if degrees[j] == 1:
                    q.put(j)
                    visited.append(j)

    if len(visited) == n:
        return False
    else:
        return True


def processFile(file_name):    
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_name)
    data = list(csv.reader(open(file_path)))
    result = is_undirected_graph_circled(data)

    if result:
        print("YES. It contains circle(s): " + file_path)
    else:
        print("NO. It doesn't contain circle(s): " + file_path)    

    return


processFile("graph1.csv")
processFile("graph2.csv")