import random as rand

from const import *
import utils

class Point:
    ''' 
    Represents the center point of a circle to be generated on the Ishihara Plate.
    '''
    def __init__(self, x, y, canvas_pxls, radius):
        self._x = x
        self._y = y
        self._loc = WIDTH*self._y + self._x
        self._in_fig = (canvas_pxls[self.get_loc()] == BLACK_RGB)
        self.radius = radius
        
    def get_loc(self):
        return self._loc
        
    def _set_loc(self):
        self._loc = WIDTH*self._y + self._x
        
    def get_coord(self):
        return (self._x, self._y)
   
    def set_coord(self, new_coord):
        self._x, self._y = new_coord
        self._set_loc()
        
    def in_fig(self):
        return self._in_fig

    def will_overlap_point(self, p2):
        p_coord = self.get_coord()
        p2_coord = p2.get_coord()
        return utils.distance_squared(p_coord, p2_coord) <= (2 * MIN_CIRCLE_RADIUS)**2

    def will_overlap_circle(self, p2):
        p_coord = self.get_coord()
        p2_coord = p2.get_coord()
        return utils.distance(p_coord, p2_coord) < (self.radius + p2.radius)
    
    def will_overlap_wall(self):
        px, py = self.get_coord()
        
        if utils.distance((px,py), (WIDTH/2, HEIGHT/2)) + self.radius > WALL_RADIUS:
            return True
                
        return False
    
    def will_overlap_fig_boundary(self, canvas_pxls):
        return utils.opposite_colr_point_in_circle(self, self.radius, canvas_pxls)
    
        
    
