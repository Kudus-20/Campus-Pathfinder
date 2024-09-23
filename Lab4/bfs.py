# Author: Abdul-Kudus Alhassan
# Date: 04/03/2023
# Purpose: implementing Breadth First Search

from collections import deque


# takes a start and goal vertices as parameters
def bfs(start, goal):
    frontier = deque()  # initializing with an empty deque
    back_pointer = {}  # initializing with an empty dictionary to keep track of the back pointers
    frontier.append(start)  # adding the start vertex to the deque
    back_pointer[start] = None  # initializing the value of star to none

    while (len(frontier) != 0) and (
            goal not in back_pointer):  # while the deque is not empty and goal not in back pointer
        curr_vertex = frontier.popleft()
        for vertex in curr_vertex.adjacency_list:  # looping through all adjacent vertices
            if vertex not in back_pointer:  # if the vertex is not already in back pointer,
                frontier.append(vertex)  # add to frontier
                back_pointer[vertex] = curr_vertex  # add as key to back pointer

    vertex_on_path = goal  # vertex on path
    vertex_path = []  # initializing a list to keep all vertices on path
    while vertex_on_path != None:
        vertex_path.append(vertex_on_path)  # add vertex to path
        bp = back_pointer[vertex_on_path]  # fetch the back pointer of that vertex
        vertex_on_path = bp  # assign it to be added to the path
    # return  a list of all vertices on the path
    return vertex_path
