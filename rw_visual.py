import matplotlib.pyplot as plt

from random_walk import *

# Keep making new walks, as long as the program is active.

keep_running = True

while keep_running:

    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
                edgecolors='none', s=15)
    # ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    while True:
        user_input = input("Make another walk? (y/n): ")
        if user_input == 'y':
            break
        elif user_input == 'n':
            keep_running = False
            break
        else:
            print("Wrong input. Please enter 'y' or 'n'.")
