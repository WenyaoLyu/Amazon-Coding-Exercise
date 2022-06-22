# Amazon-Coding-Exercise
Intership Experience UK 2022 - Technology Stream - Amazon Coding Exercise

Breadth Fisrt Search algorithm can solve the shortest path problem when all edge weights are the same. Since the self-driving delivery vehicles can navigate to any of the adjacent squares (even diagonally), as long as the squares are inbound and do not contain an obstacle, BFS can be used. 

Therefore, the basic process is:
1. First move horizontally or diagonally and visit all the nodes of the current layer
2. Move to the next layer

Since the aim of the programmme is to find the shorest path, and the endpoints are placed at the top left (0, 0) and botoom right (9, 9) corners, only three directions are required:
(i+1, j), (i, j+1), (i+1, j+1).

For example:
Layer 0: start point
  (0,0)

Layer 1: traverse next step from the start point
  (0,0) --> (0,1)
        --> (1,1)
        --> (1,0)
Layer 2: traverse next step followed by nodes on the previous layer 
  (0,0) --> (0,1) --> (0,2)
                  --> (1,2)
                  --> (1,1)
        --> (1,1) --> (1,2)
                  --> (2,2)
                  --> (2,1)
        --> (1,0) --> (1,1)
                  --> (2,1)
                  --> (2,0)
Layer 3: the start points of Layer 3 are the end points of the Layer 2. 
         Note: Different paths ending at the same nodes in the Layer 2 are equivalent (same number of steps), take one path among then randomly. 
  (0,0) --> (0,1) --> (0,2) --> (0,3)
                            --> (1,2)
                            --> (1,3)
                  --> (1,2) --> (1,3)
                            --> (2,2)
                            --> (2,3)
                  --> (1,1) --> (1,2)
                            --> (2,1)
                            --> (2,2)
        --> (1,1) --> (2,2) --> (2,3)
                            --> (3,2)
                            --> (3,3)
                  --> (2,1) --> (2,2)
                            --> (3,1)
                            --> (3,2)
        --> (1,0) --> (2,0) --> (2,1)  
                            --> (3,0)
                            --> (3,1)
                            
Layer ...: traverse the grid until one path reach the final end at (9,9)

To avoid the obstacles and grid boundary:
  The coordinate values of obstacles are saved in list true_obstacles.
  The grid boundary is considered as the obstacles on (10:) and (:10), and they are saved in the list fake_obstacles.
  When the endpoint of a path reaches any obstacles, this path would be considered to be unsucessful and would be deleted. 
  
To run the programme:
  Phase 1:
    new_obstacles_number = 0
    
  Phase 2:
    new_obstacles_number = 20
    Note: May be unable to reach the delivery point when the added obstacles has (7,9)
    
Sample:

Phase 1: 
  The number of obstacles is: 4
  The positions of the obstacles are: [[9, 7], [8, 7], [7, 7], [7, 8]]
  The path is: [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [6, 7], [6, 8], [7, 9], [8, 9], [9, 9]]
  The path costs: 11 steps

Phase 2 (randomly):
  The number of obstacles is: 24
  The positions of the obstacles are: [[9, 7], [8, 7], [7, 7], [7, 8], [3, 6], [7, 2], [0, 3], [5, 9], [4, 4], [6, 4], [4, 3], [8, 4], [3, 7], [5, 5], [0, 1], [3, 0], [5, 0], [1, 2], [4, 2], [2, 0], [7, 5], [9, 0], [2, 7], [2, 9]]
  The path is: [[0, 0], [1, 1], [2, 2], [3, 3], [3, 4], [4, 5], [5, 6], [6, 7], [6, 8], [7, 9], [8, 9], [9, 9]]
  The path costs: 11 steps

