import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc
from matplotlib.lines import Line2D  
    
# VISUALIZATION TOOLS
def plot_pitch(lc = 'black', lw = 2, xPitchSize = 100, yPitchSize = 60, scale = 1, axis = 'on'):
    """
    This function plots a soccer pitch of 100 x 60 metres
    """
    assert xPitchSize >= 90 and xPitchSize <= 120, 'The touch line must be between 90 and 120 metres'
    assert yPitchSize >= 45 and yPitchSize <= 90, 'The goal line must be between 90 and 120 metres'
    assert xPitchSize > yPitchSize, ' The touch line must be greater than the goal line'
    
    u  = 1 # metres
    xi = 0  # origin
    yi = 0  # origin
    X  = xPitchSize/2             # half x Pitch Length #m
    Y  = yPitchSize/2             # half y Pitch Length #m
    arcw  = 1                     # Goal Width
    arcl  = 7.3                   # Goal Length
    goalw = 5.5                   # Goal Area Width
    goall = 18.3                  # Goal Area Length
    penaltyw = 16.5               # Penalty Area Width
    penaltyl = 40.3               # Penalty Area Length

    # Create pitch boundaries and center circle
    pitch_border  = Rectangle((xi,yi), 2 * X, 2 * Y, linewidth = lw, color = lc, fill=False)
    halfway_line  = Line2D([X,X],[0, 2 * Y], linewidth = lw, color = lc)
    center_circle = Circle([X,Y], radius = 9.15, linewidth = lw, color = lc, fill = False)
    center_spot   = Circle([X,Y], radius = 0.30, linewidth = lw, color = lc, fill = False)

    # Create left side of the pitch
    goal_l          = Rectangle((-1, Y - arcl/2), 1, arcl, linewidth = lw, 
                               color = 'grey', fc = 'lightgrey', fill = True)
    goal_area_l     = Rectangle((0, Y - goall/2), goalw, goall, linewidth = lw, 
                               color = lc, fill = False)
    penalty_area_l  = Rectangle((0, Y - penaltyl/2), penaltyw, penaltyl, linewidth = lw, 
                               color = lc, fill = False)
    penalty_spot_l  = Circle([11, Y], radius = 0.3, linewidth = lw, color = lc, fill = True)
    penalty_arc_l   = Arc((11, Y), 2 * 9.15, 2 * 9.15, theta1 = -53, theta2 = 53, linewidth = lw, 
                         color = lc, fill = False)
    corner_upper_l  = Arc((0, 2 * Y), 2, 2, theta1 = -90, theta2 = 0, linewidth = lw, color = lc, fill = False)
    corner_bottom_l = Arc((0, 0), 2, 2, theta1 = 0, theta2 = 90, linewidth = lw, color = lc, fill = False)

    
    # Create right side of the pitch
    goal_r          = Rectangle((X*2,Y - arcl/2 ), 1, arcl, linewidth = lw, 
                                color = 'grey', fc = 'lightgrey', fill = True)
    goal_area_r     = Rectangle((2*X-goalw,Y-goall/2), goalw, goall, linewidth = lw, 
                                color = lc, fill = False)
    penalty_area_r  = Rectangle((2*X-penaltyw,Y-penaltyl/2), penaltyw, penaltyl, linewidth = lw, 
                                color = lc, fill = False)
    penalty_spot_r  = Circle([2*X-11,Y], radius = 0.3, linewidth = lw, 
                             color = lc, fill = True)
    penalty_arc_r   = Arc((2*X-11,Y), 2 * 9.15, 2 * 9.15, theta1 = 180 - 53, theta2 = 180 + 53, linewidth = lw, 
                          color = lc, fill = False)
    corner_upper_r  = Arc((2*X,2*Y), 2, 2, theta1 = 180, theta2 = -90, linewidth = lw, color = lc, fill = False)
    corner_bottom_r = Arc((2*X,0), 2, 2, theta1 = 90, theta2 = 180, linewidth = lw, color = lc, fill = False)

    # Draw all the elements
    pitch = [pitch_border,center_circle,center_spot,
             goal_l,goal_area_l, penalty_area_l, penalty_spot_l,penalty_arc_l, corner_upper_l, corner_bottom_l,
            goal_r,goal_area_r,penalty_area_r,penalty_area_r, penalty_spot_r, penalty_arc_r, corner_upper_r, corner_bottom_r]

    fig = plt.figure(figsize=(scale * xPitchSize/10, scale * yPitchSize/10))
    ax = fig.add_subplot(1,1,1)
    ax.axis(axis)
    
    for element in pitch:
        ax.add_patch(element)
    ax.add_line(halfway_line)
    ax.set_xlim(xi-2,2*X+2)
    ax.set_ylim(yi-2,2*Y+2)
    
    return fig, ax

def plot_voronoi(voronoi_matrix,cmap='coolwarm',interpolation = 'bilinear',
                 xPitchSize=100,yPitchSize=60, figsize=(10,6),lc='black',lw=2, scale = 1, axis = 'on'):
    """
    This function plots the Voronoi diagram
    """
    fig,ax = plot_pitch(lc = lc, lw = lw, xPitchSize = xPitchSize, yPitchSize = yPitchSize, scale = scale, axis = axis)
    
    ax.imshow(voronoi_matrix, cmap = cmap, interpolation = interpolation,
              extent = [0,xPitchSize,0,yPitchSize],origin = 'top',aspect = 'auto',vmin=0,vmax=1,
              )
    return fig, ax

# VORONOI CALCULATIONS
def voronoi(home_data,away_data,xPitchSize=100,yPitchSize=60,resolution=200):
    """
    This function calculates the Voronoi
    """
    x = np.linspace(0,xPitchSize,resolution)
    y = np.linspace(0,yPitchSize,resolution)
    X,Y = np.meshgrid(x,y)
    h_xy = []
    a_xy = []

    for hplayer in home_data:
        h_xy.append(np.sqrt((X - hplayer[0])**2 + (Y - hplayer[1])**2)) # distance home players
    for aplayer in away_data:
        a_xy.append(np.sqrt((X - aplayer[0])**2 + (Y - aplayer[1])**2)) # distance away players

    distance_home = np.min(h_xy,axis=0) # at each cell find the closest home player 
    distance_away = np.min(a_xy,axis=0) # at each cell find the closest away player
    voronoi_matrix = np.where(np.argmin([distance_home,distance_away],0) == 0,1,0) # if argmin is distance_home then return 1, else 0
    return voronoi_matrix

def weighted_voronoi(home_data, away_data, xPitchSize=100,yPitchSize=60, resolution=500,beta = 1):
    """
    This function calculates the weighted Voronoi
    """
    x = np.linspace(0,xPitchSize,resolution) 
    y = np.linspace(0,yPitchSize,resolution)
    X,Y = np.meshgrid(x,y)
    h_xy = []
    a_xy = []
  
    for hplayer in home_data:
        h_xy.append(np.sqrt((X - hplayer[0])**2 + (Y - hplayer[1])**2)) # distance home players
    for aplayer in away_data:
        a_xy.append(np.sqrt((X - aplayer[0])**2 + (Y - aplayer[1])**2)) # distance away players

    distance_home = np.min(h_xy,axis=0) 
    distance_away = np.min(a_xy,axis=0) 
    voronoi_matrix = np.where(np.argmin([distance_home,distance_away],0) == 0,0.5+1/(1+beta*distance_home),0.5-1/(1+beta*distance_away))
    return voronoi_matrix
