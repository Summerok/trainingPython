# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""
import pickle
class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        """Create an instance
        - robot : name of the robot
        - grille : dictionary load of the carte
        - doors : dictionary with doors position"""
        self.robot = robot
        self.grille = obstacles
        self.doors = {}
        
    def __str__(self):
        """Print the labyrinth into console"""
        chaine = ""
        for obj in self.grille.values():
            chaine += obj
        return chaine
    
    def fill_doors(self):
        for pos, door in self.grille.items():
            if door == ".":
                self.doors[pos[0],pos[1]] = "."
    
    def save_your_game(self):
        """Save the current game"""
        with open('game', 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(self)
    
    def load_last_game(self):
        """Load the last game if it exists"""
        try:
            open('game', 'rb')
        
        except FileNotFoundError:
            return None
        else:
            with open('game', 'rb') as fichier :
                mon_depickler = pickle.Unpickler(fichier)
                load_game = mon_depickler.load()
                return load_game

    def is_obstacle(self, x, y):
        """Returns True or False if there is or not an obstacle at
        this position"""
        if self.grille[x, y] == "O":
            return True
        else:
            return False
    
    def is_door(self, pos):
        """Returns True or False if there is or not a door at this
        position"""
        x = pos[0]
        y = pos[1]
        if self.doors.__contains__((x, y)):
            return True
        else:
            return False
    
    def robot_position(self):
        for pos, rob in self.grille.items():
            if rob == "X":
                base_position_x = pos[0]
                base_position_y = pos[1]
                return base_position_x, base_position_y
    
    def get_direction(curr_x, curr_y, direc):

    
    def move_robot(self, movement):
        """Method which defines the movement of the robot"""
        #direction n, s, e, w or q (to save & quit)
        direction = movement[:1]
        
        #number of steps, if not included : 1 (default)
        if len(movement) > 1:
            try:
                step = int(movement[1:])
            except ValueError:
                print("Wrong steps, try another movement, please")
                step = -1
        else:
            step = 1
        
        #getting robot position
        base_position_x, base_position_y = self.robot_position()
        
        #list of positions related with the movement
        intermediate_pos = []

        #flag to determine a wrong movement
        wrong_movement = False

        current_position_x = base_position_x
        current_position_y = base_position_y
        intermediate_pos.append((base_position_x, base_position_y))
        
        #Starting Up movement
        if direction == "n":
            i = 0
            while i < step:
                if not wrong_movement:
                    next_position_x = current_position_x
                    next_position_y = current_position_y - 1
                    if self.is_obstacle(next_position_x, next_position_y):
                        wrong_movement = True
                        print("Wrong! {} is blocked with this movement"\
                            .format(self.robot))
                        print("Try another movement, please")
                    else:
                        intermediate_pos.append((next_position_x, next_position_y))
                        current_position_y = next_position_y
                        current_position_x = next_position_x
                i += 1
            if not wrong_movement:
                i = 0
                while i < step:
                    if self.is_door(intermediate_pos[i]):
                        self.grille[intermediate_pos[i][0],intermediate_pos[i][1]] = "."
                    else:
                        self.grille[intermediate_pos[i][0],intermediate_pos[i][1]] = " "
                    self.grille[intermediate_pos[i + 1][0],intermediate_pos[i + 1][1]] = "X"
                    print("")
                    print(self)
                    print("")
                    i += 1
        else:
            print("Wrong direction, try another movement, please")

            