# Author: Abdul-Kudus Alhassan
# Date: 04/03/2023
# Purpose: reading data and creating vertex objects out of the data

from vertex import Vertex


# This function takes a line as a parameter, splits it and returns  the main vertex name, the x coordinates,
# y coordinates and empty adjacency list
def parse_line(line):
    section_split = line.split(";")  # split line into the three sections
    vertex_name = section_split[0].strip()  # split out the main vertex name

    adjacency_list = []  # initializing with an empty list

    coordinates = section_split[2].strip().split(",")  # separating the coordinates into a list
    x = coordinates[0]  # x components
    y = coordinates[1]  # y components

    return vertex_name, x, y, adjacency_list


# This function takes a line as a parameter, splits it and returns  the vertex name, and the adjacency list
def get_vertex(line):
    section_split = line.split(";")  # split line into the three sections
    vertex_name = section_split[0].strip()  # split out the main vertex name

    adjacent_vertices = section_split[1].strip().split(",")  # strips vertices into a list

    # adds all vertices except empty strings
    adjacency_list = []
    for vertex in adjacent_vertices:
        if vertex:
            adjacency_list.append(vertex.strip())  # stripping the vertex and appending to the list

    return vertex_name, adjacency_list


def load_graph(file_name):
    vertex_dict = {}  # initializing the dictionary to an empty dictionary

    # Open the file for read mode and vertex objects
    file = open(file_name, "r")
    for line in file:

        # if the line is in the correct format:
        if len(line.split(";")) == 3:
            vertex_name, x, y, adjacency_list = parse_line(line)

            vertex_obj = Vertex(vertex_name, int(x), int(y),
                                adjacency_list)  # creating a vertex object with the vertex class
            vertex_dict[vertex_name] = vertex_obj  # adding the created object to the dictionary of vertex

    file.close()

    # Open file for second time in read mode
    file1 = open(file_name, "r")

    for line in file1:
        vertex_name, adjacency_list = get_vertex(line)

        main_vertex = vertex_dict[vertex_name]  # getting the main vertex object from the dictionary

        # for every vertex in the adjacency list, append the object of the vertex to the adjacency list of the main
        # vertex
        for vertex in adjacency_list:
            main_vertex.adjacency_list.append(vertex_dict[vertex])

    file1.close()

    return vertex_dict
