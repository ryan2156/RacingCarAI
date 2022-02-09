# class xxxx():
    # any class you may create here
import random
from urllib.robotparser import RobotFileParser

from resources.app.MLGame.games.arkanoid.ml.train import Direction
class MLPlay:
    def __init__(self):
        self.other_cars_position = []
        self.coins_pos = []
        print("Initial ml script")

        #####################################################
        #                                                   #
        # initializing anything in the begining of the game #
        #                                                   #
        #####################################################

        ###############################################
        #                                             #
        # If play the game by model, read model here. #
        #                                             #
        ###############################################

    # def xxxx():
        # any function you may create here

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if scene_info.__contains__("coin"):
            self.coin_pos = scene_info["coin"]

        ###############################################
        #                                             #
        # pure rule / rule + model to control the car #
        #                                             #
        ###############################################
        
        """
        There are seven commands you can use.
        """
        
        x = scene_info["x"]
        y = scene_info["y"]
        
        turn_right = False

        for i in scene_info['all_cars_pos']:
            # print(element[0])
            if ((y > 123) and (y < 127)):
                    turn_right = True
            if ((y > 523) and (y < 527)):
                    turn_right = False
            if x == i[0] and abs(y - i[1]) > 25: 
                continue #next car pos
            if abs(y - i[1]) < 50 and abs(x - i[0])  < (scene_info["velocity"]*8) and x < i[0]:#switching lanes/換道
                if turn_right == True:
                    return ["MOVE_RIGHT"]
                else:
                    return["MOVE_LEFT"]
                #if abs(y - 125) <1:#Lane 1 failsafe
                #   return ["MOVE_RIGHT"]
                #else:
                #   return['MOVE_LEFT']
            #frontal collisions
        return ["SPEED"]
        #return ["MOVE_LEFT", "SPEED"]
        #return []
        #car volume:60*30

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass