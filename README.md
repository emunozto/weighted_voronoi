# Weighted Voronoi for Soccer
A Voronoi diagram allows us to partition the pitch space by assigning every cell to the closest player, these regions are called dominace regions. 


The weighted Voronoi is a variation of the Voronoi where a weighting function $w$ is added to control the relative level of influence that a player has over a cell. Each cell on the grid can be expressed as

$$ C^i_m = \left\{ \begin{array}{lcc}
             \frac{1}{1+w^i_m} &  if & i= argmin_j \ w^j_m \\
             \\ x &  if & otherwise 
             \end{array}
             \right.$$
where a typical weight function would be $w=\beta d^j_m$, $\beta$ could be a constant, the parameter controlling the distance to any location.

The Voronoi accounts for the space owned by each team considering only distance, while the weighted Voronoi can be modified to account for other parameters such as time.
Notice that Voronoi diagrams do not account for player velocity but they are apropiate if one wants to find the space dominated by a player.

## Source Code
* `voronoi_weighted.py`: This script contains visualization and calculation functions for weighted Voronoi.
* `tutorial_voronoi_weighted.ipynb`: This notebook shows how to use the `voronoi_weighted.py`.

