import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
zs = []
t1_x = []
t1_y = []
t2_x = []
t2_y = []
t3_x = []
t3_y = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys, zs):

    # Randomly generate an integer and a char to simulate received results
    temp_c = random.randint(0, 100)
    status_s = random.choice(['$', 'o','e'])

    # Add x, y and z to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(temp_c)
    zs.append(status_s)

    # Limit x, y and z lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]
    zs = zs[-20:]

    t1_x = []
    t1_y = []
    t2_x = []
    t2_y = []
    t3_x = []
    t3_y = []

    # Draw x, y and status lists
    ax.clear()
    ax.plot(xs, ys)
    for i in range(len(xs)):
        if zs[i] == '$':
            t1_x.append(xs[i])
            t1_y.append(ys[i])
        elif zs[i] == 'o':
            t2_x.append(xs[i])
            t2_y.append(ys[i])
        elif zs[i] == 'e':
            t3_x.append(xs[i])
            t3_y.append(ys[i])
    circle = ax.scatter(t1_x, t1_y, marker = 'o', label='$')
    square = ax.scatter(t2_x, t2_y, marker = 's', label='o')

    # Generate legend of the status
    triangle_up = ax.scatter(t3_x, t3_y, marker = '^', label='e')
    plt.legend(handles=[circle, square, triangle_up], bbox_to_anchor=(1.1, 1.1))

    # Format plot
    plt.ylim(-10,100)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Readings from remote sensor')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, zs), interval=1000)
plt.show()

