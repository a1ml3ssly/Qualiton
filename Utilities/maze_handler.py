class MazeSolver:
    __author__ = "Nitzan Bachar"
    __version__ = "1.0.0"

    def __init__(self, maze, starting_pos, finishing_pos):
        self.starting_pos = starting_pos
        self.finishing_pos = finishing_pos
        self.maze = maze
        self.maze_size = len(self.maze)
        self.solution = [[0 for j in range(self.maze_size)] for i in range(self.maze_size)]

    def print_solution(self):
        """
        prints the solution maze

        :return:
        """
        for i in self.solution:
            for j in i:
                print(str(j) + " ", end="")
            print("")

    def is_safe(self, maze, x, y):
        """
        A utility function to check if x, y is valid

        :param x:
        :param y:
        :return: true if its a valid point, false if not
        """
        if 0 <= x < self.maze_size and 0 <= y < self.maze_size and maze[x][y] == 1:
            return True
        return False

    def solve_maze(self):
        if self.solve_maze_util(self.maze, self.starting_pos[0], self.starting_pos[1]) is False:
            print("Solution doesn't exist")
            return False
        return True

    def solve_maze_util(self, maze, x, y):
        """
        A recursive utility function to solve Maze problem
        :param maze: the maze you want to get through as a 2d list
        :param x: X location in the maze
        :param y: y location in the maze
        :return: true if you solved it, false if you cant
        """

        # if (x, y is goal) return True
        if x == self.finishing_pos[0] and y == self.finishing_pos[1]:
            self.solution[x][y] = 1
            return True

        # Check if maze[x][y] is valid
        if self.is_safe(maze, x, y) is True:
            # Check if the current block is already part of solution path.
            if self.solution[x][y] == 1:
                return False

            # mark x, y as part of solution path
            self.solution[x][y] = 1

            # Move forward in x direction
            if self.solve_maze_util(maze, x + 1, y) is True:
                return True

            # If moving in x direction doesn't give solution
            # then Move down in y direction
            if self.solve_maze_util(maze, x, y + 1) is True:
                return True

            # If moving in y direction doesn't give solution then
            # Move back in x direction
            if self.solve_maze_util(maze, x - 1, y) is True:
                return True

            # If moving in backwards in x direction doesn't give solution
            # then Move upwards in y direction
            if self.solve_maze_util(maze, x, y - 1) is True:
                return True

            # If none of the above movements work then
            # BACKTRACK: unmark x, y as part of solution path
            self.solution[x][y] = 0
            return False
