import pygame as p
import inspect

import global_values as g
import graphics as gfx
import actions

class Element:
    def __init__(self, rect,z_index=0):
        self.rect = rect
        self.z_index = z_index