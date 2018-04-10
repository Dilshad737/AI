import matplotlib.pyplot as plt
import matplotlib.animation as animation
def animate():
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line)>1:
            x ,y = line.split(',')
            xs.append(x)
            ys.append(y)
    plt.plot(xs,ys)
    plt.show()
animate()
