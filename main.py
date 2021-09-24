import random

iterations = 50  # int(input("Please enter n of iterations"))
particles = 30  # input("Please enter n of particles")
target = 5  # input("Please enter target point")
error = 0.00000001


def fitness(_x, _y, _z):
    return abs(target - ((_x * _x) + (_y * _y) + (_z * _z)))


class Particle:
    def __init__(self, pos):
        self.velocity = 0
        self.position = pos
        self.bestValue = float("inf")
        self.bestPosition = float("inf")


if __name__ == '__main__':
    CPSO = []
    cVec = []
    rMin = [-50, -50, -50]
    rMax = [50, 50, 50]
    W = 0.5
    c1 = 0.8
    c2 = 0.9

    # initialize
    for x in range(len(rMin)):
        swarm = []
        for p in range(particles):
            swarm.append(Particle(random.randrange(rMin[x], rMax[x] + 1)))
        CPSO.append(swarm)
        cVec.append(swarm[random.randrange(0, len(swarm))].position)

    bestFitness = fitness(cVec[0], cVec[1], cVec[2])
    for i in range(iterations):
        # update context vector
        for s in range(0, len(CPSO)):
            tempContext = [cVec[0], cVec[1], cVec[2]]
            for p in range(0, len(CPSO[s])):
                tempContext[s] = CPSO[s][p].position
                f = fitness(tempContext[0], tempContext[1], tempContext[2])
                if f < CPSO[s][p].bestValue:
                    CPSO[s][p].bestValue = f
                    CPSO[s][p].bestPosition = CPSO[s][p].position
                if f < bestFitness:
                    cVec[s] = CPSO[s][p].position
                    bestFitness = f
        # Move all the particles
        for s in range(0, len(CPSO)):
            tempContext = [cVec[0], cVec[1], cVec[2]]
            for p in range(0, len(CPSO[s])):
                CPSO[s][p].velocity = (W * CPSO[s][p].velocity) + \
                                      ((c1 * random.random()) * (CPSO[s][p].bestPosition - CPSO[s][p].position)) + \
                                      ((c2 * random.random()) * (cVec[s] - CPSO[s][p].position))
                CPSO[s][p].position += CPSO[s][p].velocity
        # Break if iteration is found
        if bestFitness < error:
            print("Solution found:", cVec, "error:", bestFitness, "application:",
                  (cVec[0] * cVec[0]) + (cVec[1] * cVec[1]) + (cVec[2] * cVec[2]), "on iteration:", i)
            break
    if bestFitness > error:
        print("Nearest possible solution:", cVec, "error:", bestFitness, "application:",
              (cVec[0] * cVec[0]) + (cVec[1] * cVec[1]) + (cVec[2] * cVec[2]))
