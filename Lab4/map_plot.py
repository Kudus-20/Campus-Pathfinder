# Author: Abdul-Kudus Alhassan
# Date: 04/03/2023
# Purpose: drawing the map

from cs1lib import *
from load_graph import *
from bfs import bfs

WIDTH = 1012    # window width
HEIGHT = 811    # window height

vertex_dict = load_graph("dartmouth_graph.txt")  # dictionary with all the vertex objects

# initializing the start and goal vertices to none
start_vertex = None
goal_vertex = None

click = False  # checks if the mouse has been clicked


# Detects when mouse is clicked
def mouse_press(mx, my):
    global start_vertex, click
    click = True  # update click
    for key in vertex_dict:  # checking all vertices in the dictionary
        if vertex_dict[key].is_on_vertex(mx, my):  # if the mouse position matches the location of any vertex
            start_vertex = vertex_dict[key]  # update start vertex to that clicked vertex


# Tracks the location of the mouse as it moves
def mouse_move(mx, my):
    global goal_vertex
    if click:  # update only if mouse has been clicked
        for key in vertex_dict:  # checking all vertices in the dictionary
            if vertex_dict[key].is_on_vertex(mx, my):  # if the mouse position matches the location of any vertex
                goal_vertex = vertex_dict[key]  # update goal vertex to that clicked vertex


map_img = load_image("dartmouth_map.png")  # load  map image into window


def draw():
    global start_vertex, goal_vertex
    clear()
    draw_image(map_img, 0, 0)  # draws map image into window

    # drawing all the vertices in the vertex dictionary
    for key in vertex_dict:
        vertex_dict[key].draw_adj_vertices(1, 0, 0)  # draw the edge between the vertex and it's adjacent vertices
        vertex_dict[key].draw_vertex(1, 0, 0)  # draw the vertex

    path = bfs(start_vertex, goal_vertex)  # getting the path from bfs

    i = 0
    # loops through the path list and draws all vertices and the edges connecting them
    while i < len(path) - 1:
        path[i].draw_edge(path[i + 1], 0, 0, 0)  # draw edge between the current index and the next
        path[i].draw_vertex(0, 0, 0)    # draw the vertex at index i in a different colour
        path[i + 1].draw_vertex(0, 0, 0)    # draw the vertex at index i+1 in a different colour
        i += 1  # increment i


start_graphics(draw, 2400, width=WIDTH, height=HEIGHT, mouse_press=mouse_press, mouse_move=mouse_move)
