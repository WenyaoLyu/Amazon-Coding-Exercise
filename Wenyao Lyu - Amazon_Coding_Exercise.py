# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:23:04 2022

@author: Wenyao Lyu
"""

import numpy as np

###############Parameters###############
#np.random.seed(2)

#set grid
row = 10
column = 10

#set endpoints
initial_point = [0, 0]
end_point = [9, 9]

#solid obstacles
obstacles = [[9, 7], [8, 7], [7, 7], [7, 8]]

#additional random obstacles
new_obstacles_number = 0
###############Parameters###############


###############Produce Obstacles###############
row_obstacles = []
column_obstacles = []

for i in range(row):
    row_obstacles.append([row, i])

for j in range(column):
    column_obstacles.append([j, column])

fake_obstacles = obstacles + row_obstacles + column_obstacles + [[row, column]]


produce_obstacle = 0
new_obstacles = []
while produce_obstacle < new_obstacles_number:
    new_row = np.random.randint(row)
    new_column = np.random.randint(column)
    if ([new_row, new_column] in (fake_obstacles + [initial_point] + [end_point] + new_obstacles)) == False:
        new_obstacles.append([new_row, new_column])
        produce_obstacle = produce_obstacle + 1
        
fake_obstacles = fake_obstacles + new_obstacles
true_obstacles = obstacles + new_obstacles
###############Produce Obstacles###############

                
###############Functions###############       
def one_step(steps):
    new_step_list = []
    step_number = len(steps)
    last_step = steps[step_number-1]
    
    if ([last_step[0] + 1, last_step[1]] in fake_obstacles) == False:
        new_step_list.append(steps + [[last_step[0] + 1, last_step[1]]])
    if ([last_step[0] + 1, last_step[1] + 1] in fake_obstacles) == False:
        new_step_list.append(steps + [[last_step[0] + 1, last_step[1] + 1]])
    if ([last_step[0], last_step[1] + 1] in fake_obstacles) == False:
        new_step_list.append(steps + [[last_step[0], last_step[1] + 1]])
    
    return new_step_list


def non_repeat(step_list):
    non_repeat_steps = []
    last_steps = []
    for i in step_list:
        if (i[len(i)-1] in last_steps) == False:
            last_steps.append(i[len(i)-1])
            non_repeat_steps.append(i)
    return non_repeat_steps


def judge_end(step_list):
    last_steps = []
    for i in step_list:
        last_steps.append(i[len(i)-1])
    if end_point in last_steps:
        position = last_steps.index(end_point)
        true_steps = step_list[position]
        return True, true_steps
    else:
        return False, []
###############Functions###############
        

###############Running Area###############
previous_step = [[initial_point]]
step = 0

while True:
    new_step_list = []
    for i in previous_step:
        new_step_list = new_step_list + one_step(i)
    if new_step_list == []:
        true_step = 'Unable to reach delivery point'
        break
    new_step_list = non_repeat(new_step_list)
    end = judge_end(new_step_list)
    
    step = step + 1
    previous_step = new_step_list
    
    if end[0]:
        true_step = end[1]
        break
###############Running Area###############

print('The number of obstacles is:', new_obstacles_number + 4)
print('The positions of the obstacles are:', true_obstacles)
print('The path is:', true_step)
print('The path costs:', step, 'steps')


