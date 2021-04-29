import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    L = 101 #dimensions of a square grid of LxL
    I = 50 #initial position in the x direction
    J = 50 #initial position in the y direction
    N = 10000 #number of steps of movement to perform

    positionList = [(I, J)]
    NCount = 0
    while NCount < N:
        #positionList.append((I, J))
        roll = np.random.random()
        if roll < 0.25:
            if J - 1 > 0:
                J = J - 1
                positionList.append((I, J))
                NCount += 1
            else:
                continue #If hits an edge, go back to top of loop
        elif 0.25 < roll < 0.5:
            if I + 1 < L:
                I = I+1
                positionList.append((I, J))
                NCount += 1
            else:
                continue #If hits an edge, go back to top of loop
        elif 0.5 < roll < 0.75:
            if J+1 < L:
                J = J+1
                positionList.append((I, J))
                NCount += 1
            else:
                continue #If hits an edge, go back to top of loop
        elif roll > 0.75:
            if I-1 > 0:
                I = I-1
                positionList.append((I, J))
                NCount += 1
            else:
                continue #If hits an edge, go back to top of loop

    xlist = []
    ylist = []
    for i in range(len(positionList)):
        xlist.append(positionList[i][0])
        ylist.append(positionList[i][1])

    #Creates a line plot showing path of the particle
    plt.plot(xlist, ylist)#, marker='.')
    plt.title("Brownian Motion Over 10000 Steps")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()
    plt.clf()

    #Creates an animation of the motion of the particle
    pos = np.array([50, 50])
    plt.ion()
    fig, ax = plt.subplots(figsize=(10,10))
    plt.xlim((0, L))
    plt.ylim((0, L))
    ax.set_aspect('equal')
    scat = ax.scatter(*pos)
    plt.title('Brownian motion in a box')
    for i in range(10000):
        scat.set_offsets([positionList[i][0], positionList[i][1]])
        plt.draw()
        plt.pause(0.01)
            
        
