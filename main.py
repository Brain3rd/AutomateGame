from PIL import ImageOps, ImageGrab
import pyautogui
from numpy import *

# Autoplay this game
# https://elgoog.im/t-rex/

# Get current mouse position app
# http://efigureout.com/free-utility-to-locate-mouse-cursor-position/


class DinoGame:
    def __init__(self):
        # Use app mentioned above to get coordinates
        self.replay_btn_pos = (441, 426)
        self.dino_pos = (160, 449)

    def restart(self):
        # Click restart button
        pyautogui.click(self.replay_btn_pos)

    def front_of_dino(self):
        # draw box in front of dino
        box = (self.dino_pos[0]+55, self.dino_pos[1], self.dino_pos[0]+145, self.dino_pos[1]+5)
        image = ImageGrab.grab(box)
        # Make box grayscale
        grayscale_image = ImageOps.grayscale(image)
        # Return color of the box
        return sum(grayscale_image.getcolors())


if __name__ == '__main__':

    dino_game = DinoGame()

    dino_game.restart()

    while True:
        # If color front of dino is not white
        if dino_game.front_of_dino() != 697:
            # Dino jump
            pyautogui.keyDown('space')
