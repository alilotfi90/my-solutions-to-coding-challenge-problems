

class State(object):
    """The Problem State is an array of Boolean values, which we represent by a nested list.  True means a green tile, False a red tile.
       
    """
    def __init__(self, gridsize, blocks, used, library, grid=None):
        """
        Initialize the State object.
        
        gridsize: Integer. The size of a square grid to fill
        blocks: Dictionary mapping block names to the number
                still available of that block
        used: List-of-tuples indicating which blocks have been
            placed on the grid and where
        library: Dictionary mapping block names to what they
            look like.  This is NOT copied, but just for reference
        
        """
        self.N = gridsize
        
        # create a copy of the available block counts
        self.blocks = dict(blocks)
        
        # create a copy of current block locations
        self.used = [x for x in used]
        
        # DON'T copy the library, there's no need since
        # it shouldn't change
        self.lib = library
        
        # store the grid contents to make it easier 
        # to check if pieces can be added later
        if grid == None:
            # if no grid is given, make a blank one
            self.grid = self.make_grid(self.N)
        else:
            # if a grid is given, copy it
            self.grid = []
            for row in grid:
                new_row = [x for x in row]
                self.grid.append(new_row)

        
    def make_grid(self, N):
        """ creates a list-of-lists-of-strings that represents the 
        grid.
        We pad it with a border to make the logic for 
        out-of-bounds checks easier.
        
        . means empty, * means block, # means border
        
        N: integer, the size of the grid
        """
        grid = []
        for i in range(N):
            row = ["."] * N + ["#"] * 3
            grid.append(row)
        for j in range(3):
            row = ["#"] * (N+3)
            grid.append(row)       
            
        return grid
    
    def place_block(self, b, row, col):
        """ places the block b onto the grid at the given
        row and col location.
        
        pre-condition: the placement is legal
        """
        move = (b, row, col)
        self.blocks[b] -= 1
        self.used.append(move)
        shape = self.lib[b]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[y][x] == "*":
                    self.grid[row+y][col+x] = shape[y][x]
                
    def remove_block(self, b, row, col):
        """ remove a block from the grid at location row, col
        
        pre-condition: there is a correct block at that location
        """
        move = (b, row, col)
        self.blocks[b] += 1
        self.used.remove(move)
        shape = self.lib[b]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[y][x] == "*":
                    self.grid[row+y][col+x] = "."
                    
    def legal_move(self, b, row, col):
        """ returns true if it is legal to place block b
        at location row, col
        """
        # No block of that type
        if b not in self.blocks or self.blocks[b] < 1:
            return False
        
        legal = True       
        shape = self.lib[b]
        for y in range(len(shape)):
            for x in range(len(shape[y])):
                if shape[y][x] == "*":
                    if self.grid[row+y][col+x] != ".":
                        legal = False
        return legal
                     
    def __str__(self):
        """ A string representation of the State 
        Display the grid, cutting off the internal padding,
        and the number of blocks remaining """
        s = []
        for row in self.grid:
            row = "".join(row[0:-3])
            s.append(row)
        
        s = s[0:-3]
        s = "\n".join(s)
        s += "\n"
        s += "Block locations: \n"
        s += str(self.used)
        s += "\n"
        s += "Fitness score:\n"
        s += str(self.get_score())
        s += "\n"
        s += "Unused blocks: \n"
        s += str(self.blocks)
        return s

    def __eq__(self, other):
        """ Two states are the same if they have put the blocks
        in the same place and have the same blocks left.
        
        """  
        # use 'set()' because we don't care about order
        # of blocks in the list of used blocks
        return set(self.used) == set(other.used) and self.blocks == other.blocks
        
        

    def get_score(self):
        """ compute the fitness score for a state
        """
        #TODO: Decide on a fitness score, implement it
        # we count how many scores are covered, the score will be number of non-covered squares

        count = 0
        # the blocks we used are covering 4 squares or 5
        for tup in self.used:
            if tup[0] in ["|", "Z", "4"]:
                count+=4
            else:
                count+=5
        #score is uncovered squares
        score=(self.N)*(self.N)-count


        return score

        
    def is_better_than(self, other):
        """ 
            Return True if self is a better solution than other.
            Smaller score is better.
            :param: other: a State object
            :return: boolean
        """
        
        return self.get_score() < other.get_score()

    def is_equal_to(self, other):
        """ 
            Return True if self is as good a solution as other
            :param: other: a State object
            :return: boolean
        """
        return self.get_score() == other.get_score()

    def helper(self):
        choice_list=[]
        for block in self.blocks:
            if self.blocks[block] != 0:
                for i in range(self.N):
                    for j in range(self.N):
                        if self.legal_move(block, i, j):
                            # new_state = P.State(s1.N, s1.blocks, s1.used, s1.lib, s1.grid)
                            # new_state.place_block(block,i,j)
                            choice_list.append((block, i, j))
        choice_list.append(False)
        return rand.choice(choice_list)

class Problem(object):
    """The Pr   oblem class defines aspects of the problem.

    """

    def __init__(self, gridsize, blocks):
        """ The problem is defined by an empty grid.
        We want to place blocks to cover as much
        of the grid as possible.

            :param gridsize: dimension for a square grid
            :param blocks: dictionary mapping block names
                to the number available of that block
        """
        # dimensions of the grid to fill
        self.N = gridsize
        
        # initial available blocks
        self.blocks = blocks
        
        # show which spaces on a grid each block
        # would actually cover
        self.library = { "+" : [".*.",
                                "***",
                                ".*."],
                         "|" : ["*",
                                "*",
                                "*",
                                "*"],
                         "L" : ["*..",
                                "*..",
                                "***"],
                         "Z" : ["**.",
                                ".**"],
                         "T" : ["***",
                                ".*.",
                                ".*."],
                         "4" : ["*.", # ok it doesn't really look like a 4...
                                "**",
                                ".*"],                            
                        }
            

    def create_initial_state(self):
        """ returns an initial state.
        """
        s = State(self.N, self.blocks, [], self.library)
        return s
        
    def objective_function(self, state):
        """
            score calculation is done at the state level
        """
        return state.get_score()
        
    def n_choose_k(self, n, k):
        return M.factorial(n) / ( M.factorial(n-k) * M.factorial(k) )
        
    def random_state(self):
        
   
           
    def neighbors(self, s):
        """ return a list of all neighbors of the given state.
    
      
        """
        # list of states that are neighbors to the given state
        neighbors = []
        # example of how to make one copy of the given state, s
        # new_state = State(s.N, s.blocks, s.used, s.lib, s.grid)

        #TODO: Define a neighborhood and fill the list of neighbors
        # with all the neighboring states to s
        #neighbors which could be attained by adding one block
        for i in range(s.N):
            for j in range(s.N):
                for block in s.blocks:
                    if s.legal_move(block, i, j):
                        new_state = State(s.N, s.blocks, s.used, s.lib, s.grid)
                        new_state.place_block(block, i, j)
                        neighbors.append(new_state)

        #neighbors which could be attained by removing one block
        for tup in s.used:
            print("hello")
            new_state = State(s.N, s.blocks, s.used, s.lib, s.grid)
            block=tup[0]
            x_pos = tup[1]
            y_pos = tup[2]
            new_state.remove_block(block, x_pos, y_pos)
            neighbors.append(new_state)

  

        return neighbors
        
    def random_step(self, state):
        """ Return a State that is a random neighbour of the given State.
            :param: state: A State object
        """
        A = self.neighbors(state)
        return rand.choice(A)
        
        
    def best_step(self, state):
        """ Return the best neighbouring State for the given State.
            It doesn't have to be better than the given State!
            :param: state: A State object
        """
        A = self.neighbors(state)
        best = A[0]
        for s in A:
            if s.get_score() < best.get_score():
                best = s
        return best

    def random_better(self, state):
        """ Return a State that is a random BETTER neighbour of the given State.
            Should return None if there isn't one!
            :param: state: A State object
        """
        better = []
        A = self.neighbors(state)
        for s in A:
            if s.get_score() < state.get_score():
                better.append(s)
        
        if len(better) > 0:
            return rand.choice(better)
        else:
            return None




            
# end of file
