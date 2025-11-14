import matplotlib.pyplot as plt

from random_walk import *

# Keep making new walks, as long as the program is active.

keep_running = True

while keep_running:

    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
                edgecolors='none', s=1)
    # ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    #Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
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
