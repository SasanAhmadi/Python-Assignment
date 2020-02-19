"""
Author -- Michael Widrich
Contact -- widrich@ml.jku.at
Date -- 01.10.2019

###############################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This  material,  no  matter  whether  in  printed  or  electronic  form,
may  be  used  for personal  and non-commercial educational use only.
Any reproduction of this manuscript, no matter whether as a whole or in parts,
no matter whether in printed or in electronic form, requires explicit prior
acceptance of the authors.

###############################################################################

Template file for solution of assignment 3, exercise 12, 13, 14. Contains
backbone for GameOfLife class and example usage of GameOfLife at the end of the
file. Make sure you only changed the methods you are supposed to change in
the file you hand in as your solution.
"""

# Add your import statements here

# Do not modify these import statements
import os
import numpy as np
from matplotlib import pyplot as plt
import tqdm


class GameOfLife(object):
    # Here you should modify the __init__ method (ex12)
    def __init__(self, configpath: str, outputfile: str):
        """Template version of __init__(). This is not a valid solution for ex12."""
        os.makedirs(os.path.join("a3_template_output", "plots"), exist_ok=True)
        with open(os.path.join("a3_template_output", "output.txt"), 'w') as fh:
            pass
        
        self.n_iterations = 10
        self.state = np.array([[False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, True, True, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, True, True, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, True, True, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, True, True, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, True, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, True, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, True, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False]])
        self.symbol_dead = '-'
        self.symbol_live = 'o'
        self.current_iteration = 0
        self.outputfile = os.path.join("a3_template_output", "output.txt")
    
    # Here you should modify the __state_to_file__ method (ex13)
    def __state_to_file__(self):
        with open(self.outputfile, 'a+') as f:
            for r in self.state:
                f.write(''.join([self.symbol_live if char == True else self.symbol_dead for char in r]) + '\n')
            f.write('\n')

    
    # Here you should modify the make_video method (ex14)
    def make_video(self, videopath: str):
        pass
    
    #
    # DO NOT MODIFY THE CODE BELOW THIS COMMENT IN YOUR SUBMISSION
    #
    def read_config_file(self, configpath: str):
        """Template version of read_config_file(). This is not a valid solution for ex10."""
        state_as_bool = np.array([[False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, True, True, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, True, True, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, True, True, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, True, True, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, True, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, True, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, True, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False],
                                  [False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False, False, False, False, False, False,
                                   False, False, False, False]])
        n_iterations = 10
        symbol_dead = '-'
        symbol_live = 'o'
        return n_iterations, symbol_dead, symbol_live, state_as_bool
    
    def step(self):
        """Compute the next tick of the simulator and return current number of iteration.
        Returns None if game is completed."""
        self.current_iteration += 1
        if self.current_iteration >= self.n_iterations:
            return None
        self.state = self.__compute_next_state__(self.state)
        self.__state_to_file__()
        self.__state_to_image__()
        return self.current_iteration
    
    def __compute_next_state__(self, state: np.ndarray):
        """Template version of __compute_next_state__(). This is not a valid solution for ex11."""
        temp_state_1 = np.array([[False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False,  True,  True, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False,  True,  True, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False,  True,  True, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False,  True,  True, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, True, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, True, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, True, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False]])
        
        temp_state_2 = np.array([[False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False,  True,  True, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False,  True,  False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False,  False,  True, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False,  True,  True, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, True, True, True,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False],
                              [False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False, False, False, False, False, False,
                               False, False, False, False]])
        if np.all(self.state == temp_state_1):
            new_state = temp_state_2
        else:
            new_state = temp_state_1
        return new_state
    
    def __state_to_image__(self):
        """Save state to image file"""
        image_name = os.path.join(os.path.dirname(self.outputfile), "plots", f"state_{self.current_iteration:05}.png")
        fig, ax = plt.subplots()
        ax.imshow(np.asarray(self.state, dtype=np.uint8))
        fig.tight_layout()
        fig.savefig(image_name)
        plt.close(fig)


if __name__ == "__main__":
    import argparse
    
    # Create a parser
    parser = argparse.ArgumentParser()
    parser.add_argument('configpath', help='configuration file', type=str)
    parser.add_argument('outputfile', help='file to write state to', type=str)
    
    # Parse the arguments
    args = parser.parse_args()
    configpath = args.configpath
    outputfile = args.outputfile
    
    # Create game instance
    game = GameOfLife(configpath=configpath, outputfile=outputfile)
    
    current_iteration = 0
    with tqdm.tqdm() as progressbar:  # Show a progressbar
        while current_iteration is not None:  # Continue until current iteration is None (=End of game)
            current_iteration = game.step()
            progressbar.update()
    
    # Save video to file
    game.make_video(os.path.join(os.path.dirname(outputfile), "video.mp4"))
