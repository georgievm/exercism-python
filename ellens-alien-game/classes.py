"""Solution to Ellen's Alien Game exercise."""

class Alien:
    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1
    def is_alive(self):
        return self.health > 0
    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    def collision_detection(self, other_object):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
        
def new_aliens_collection(alien_start_positions):
    aliens = []
    for pos in alien_start_positions:
        aliens.append(Alien(pos[0], pos[1]))
    return aliens
