import math
from simpleai.search import SearchProblem, astar

class MazeSolver(SearchProblem):

    def __init__(self, gameboard):
        self.gameboard = gameboard
        self.goal = (0, 0)

        for y in range(len(self.gameboard)):
            for x in range(len(self.gameboard[y])):
                if (self.gameboard[y][x].lower() == "o"):
                    self.initial = (x, y)
                elif (self.gameboard[y][x].lower() == "x"):
                    self.goal = (x, y)

        super(MazeSolver, self).__init__(initial_state=self.initial)

    # Define the method that takes actions
    # to arrive at the solution
    def actions(self, state):
        actions = []
        for action in COSTS.keys():
            newx, newy = self.result(state, action)
            if self.gameboard[newy][newx] != "#":
                actions.append(action)

        return actions

    # Update the state based on the action
    def result(self, state, action):
        x, y = state

        if action.count("up"):
            y -= 1
        if action.count("down"):
            y += 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1

        new_state = (x, y)

        return new_state

    # Check if we have reached the goal
    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return COSTS[action]

    def heuristic(self, state):
        x, y = state
        vx, vy = self.goal
        return math.sqrt((x - vx) ** 2 + (y - vy) ** 2)

if __name__ == "__main__":
    # Define the map
    GameMap = """
           #############################
           #           #           p   #
           # ####            # #########
           #    #       #              #
           #  O ###      #             #
           #      #       #    p       #
           #      #       #            #
           #     ######                #
           #              #            #
           #              #          X #
           #############################
             """

    print()
    print("Before: (x=uitgang, p=checkpoints, o= ai agent")
    # Convert map to a list
    print(GameMap)
    GameMap = [list(x) for x in GameMap.split("\n") if x]

    # Define the cost of moving around the map
    cost_regular = 1.0


    # Create the cost values
    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
    }

    # Create maze solver object
    problem = MazeSolver(GameMap)

    # Run the solver
    result = astar(problem, graph_search=True)


    # Extract the path
    path = [x[1] for x in result.path()]


    # Print the result
    print("After")
    for y in range(len(GameMap)):
        for x in range(len(GameMap[y])):
            if (x, y) == problem.initial:
                print('o', end='')
            elif (x, y) == problem.goal:
                print('x', end='')
            elif (x, y) in path:
                print('·', end='')
            else:
                print(GameMap[y][x], end='')

        print()
