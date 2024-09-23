# Author: Abdul-Kudus Alhassan
# Date: 04/03/2023
# Purpose: Creating a vertex class to hold information for each vertex

from cs1lib import *

VERTEX_RAD = 5  # Radius of circle that represents a vertex
EDGE_WIDTH = 3  # thickness of lines


class Vertex:
    # constructor that sets instance variables
    def __init__(self, name, x, y, adjacency_list):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency_list = adjacency_list

    # draws the vertex as a colored circle
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)  # set color
        draw_circle(self.x, self.y, VERTEX_RAD)  # draw circle with given color

    # draws an edge between the current vertex object and the one passes in as a parameter
    def draw_edge(self, vertex, r, g, b):
        set_fill_color(r, g, b)  # setting color
        set_stroke_width(EDGE_WIDTH)  # thickness of line
        set_stroke_color(r, g, b)  # line color
        draw_line(self.x, self.y, vertex.x, vertex.y)  # draw line between the two vertices

    # call draw_edge to draw the edges between the object and all its adjacent vertices
    def draw_adj_vertices(self, r, g, b):
        for vertex in self.adjacency_list:  # loops through all vertices in the adjacency list
            self.draw_edge(vertex, r, g, b)  # draw edge

    # takes x and y coordinates and checks if those coordinates are same or within a certain range of the current vertex
    def is_on_vertex(self, mx, my):
        return (self.x - VERTEX_RAD <= mx <= self.x + VERTEX_RAD) and (self.y - VERTEX_RAD <= my <= self.y + VERTEX_RAD)
