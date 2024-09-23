# Author: Abdul-Kudus Alhassan
# Date: 04/03/2023
# Purpose: Creating a vertex class to hold information for each vertex

class Vertex:
    def __init__(self, name, x, y, adjacency_list):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency_list = adjacency_list

    def list(self):
        new_list = []

        for ele in self.adjacency_list:
            new_list.append(ele.name)
        return new_list

    def __str__(self):
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices:" + ", ".join(self.list())
