import time
import random as rand

from img import displayImage
from classes import Point
from const import *
import utils

def setup():        
    size(800, 800)
    background(WHITE)
    
    start_time = time.time()
    
    # Change FILE_NAME if necessary.
    FILE_NAME = 'square.png'
    # Set this to False if the loaded image is already properly formatted.
    # See block comment of preprocessImage() to know what "properly formatted" 
    # means.
    PREPROCESS = True 
    if displayImage(FILE_NAME, PREPROCESS):
        print('Generating')
        loadPixels()
        fig_random_points, bg_random_points = monte_carlo(pixels, True)
        print('Success')    
    else: 
        print('Failed')
        exit()
    
    print('Program finished execution after {} seconds.'
          .format(round(time.time() - start_time, 3))
    )
    
        
def monte_carlo(canvas_pxls, visualize = False, fig_color_scheme = FIG_COLOR_SCHEME, bg_color_scheme = BG_COLOR_SCHEME):
    '''
    Return a list of random points in the background and a list of random points in the figure. 
    The random points are generated such that they do not overlap with other points, 
    figure boundary, and the canvas wall.
    
    Parameters:
        canvas_pxls: List[color]
        visualize: boolean := If True, the random points will be drawn on the canvas
                              using circles with radius MIN_CIRCLE_RADIUS. Note that 
                              this will draw over the canvas, so if the canvas' pixel 
                              information is needed, don't use this (or transfer the 
                              circles in another image). This is initially set to False.
        fig_color_scheme: List[str] := List of color hex strings for the figure that will be used as argument to fill().
        bg_color_scheme: List[str] := List of color hex strings for the background that will be used as argument to fill().

    Return Value:
        (fig_random_points, bg_random_points): Tuple[List[Point], List[Point]]
    '''
    bg_random_points = []
    fig_random_points = []
    
    noStroke()
    
    for i in range(MAX_NUM_CIRCLES):
        x, y = int(rand.uniform(0, WIDTH)), int(rand.uniform(0, HEIGHT))
        r = rand.randrange(MIN_CIRCLE_RADIUS, MAX_CIRCLE_RADIUS+1)
        p = Point(x, y, canvas_pxls, r)
        overlap = False
                
        if p.will_overlap_wall() or p.will_overlap_fig_boundary(canvas_pxls):
            overlap = True
                                                                            
        if not overlap:
            random_points = fig_random_points if p.in_fig() else bg_random_points
            for p2 in random_points:
                if p.will_overlap_point(p2) or p.will_overlap_circle(p2):
                    overlap = True
                    break
                                                    
        if not overlap:
            if p.in_fig():
                fig_random_points.append(p)
            else:
                bg_random_points.append(p)

    background(WHITE)
    
    if visualize:
        for p in fig_random_points:
            fill(rand.choice(fig_color_scheme))
            x, y = p.get_coord()
            r = p.radius
            circle(x, y, 2*r)
        
        for p in bg_random_points:
            fill(rand.choice(bg_color_scheme))
            x, y = p.get_coord()
            r = p.radius
            circle(x, y, 2*r)
            
    return (fig_random_points, bg_random_points)
            
        
        
        
