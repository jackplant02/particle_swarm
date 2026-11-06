import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

def compute_vel(x_pos, y_pos, x_best, y_best):
    """Compute the velocity to another position"""

    return [x_best - x_pos, y_best - y_pos]

class bird:
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        """Initialize bird"""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_best = None
        self.y_best = None
        self.score = None

    def assign_new_position(self):
        """Assign new bird position"""
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    def assign_new_velocity(self, vel_to_group_best, vel_to_personal_best, momentum=0.8, group_gravity=0.1, personal_gravity=0.1):
        """Assigns new bird velocity"""
        self.x_vel = momentum * self.x_vel + group_gravity * vel_to_group_best[0] + personal_gravity * vel_to_personal_best[0]
        self.y_vel = momentum * self.y_vel + group_gravity * vel_to_group_best[1] + personal_gravity * vel_to_personal_best[1] 


class swarm:
    def __init__(self, size, scorer, bounds=5):
        """Initialize the swarm."""
        self.size = size
        self.scorer = scorer
        self.bounds = bounds
        self.x_group_best = None
        self.y_group_best = None
        self.best_score = None

        rand_x_positions = rng.uniform(-bounds, bounds, size=size).tolist()
        rand_y_positions = rng.uniform(-bounds, bounds, size=size).tolist()
        rand_x_velocities = rng.uniform(-bounds / 10, bounds / 10, size=size).tolist()
        rand_y_velocities = rng.uniform(-bounds / 10, bounds / 10, size=size).tolist()
        
        self.birds = [bird(x_pos, y_pos, x_vel, y_vel) for x_pos, y_pos, x_vel, y_vel in zip(rand_x_positions, rand_y_positions, rand_x_velocities, rand_y_velocities)]

    def score_birds(self):
        """Scores all birds and assigns the best overall position and score"""
        for bird in self.birds:
            current_score = self.scorer(bird.x_pos, bird.y_pos)

            # update bird's score if it is a new best
            # and check if it's the new best group score

            if not bird.score:
                bird.score = current_score
                bird.x_best = bird.x_pos
                bird.y_best = bird.y_pos
                
            elif current_score < bird.score:
                bird.score = current_score
                bird.x_best = bird.x_pos
                bird.y_best = bird.y_pos

            if not self.best_score:
                self.best_score = current_score
                self.x_group_best = bird.x_pos
                self.y_group_best = bird.y_pos

            elif current_score < self.best_score:
                self.best_score = current_score
                self.x_group_best = bird.x_pos
                self.y_group_best = bird.y_pos
                
    
    def update_positions(self):
        """Update the positions of all of the birds in the swarm"""
        for bird in self.birds:
            bird.assign_new_position()


    def update_velocities(self):
        """Update the velocities for all birds in the swarm"""
        for bird in self.birds:
            vel_to_personal_best = compute_vel(bird.x_pos, bird.y_pos, bird.x_best, bird.y_best)
            vel_to_group_best = compute_vel(bird.x_pos, bird.y_pos, self.x_group_best, self.y_group_best)

            bird.assign_new_velocity(vel_to_group_best, vel_to_personal_best)


    def update_all(self):
        """Performs one iteration of PSO"""
        self.score_birds()
        self.update_velocities()
        self.update_positions()

    def 








        




        