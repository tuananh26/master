
import arcade

import chess
from const import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, BACKGROUND_COLOR, PIXEL_WIDTH, LINE_COLOR


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        pass

    def on_draw(self):
        """ Render the screen. """
        for x in range(0, SCREEN_WIDTH+1, PIXEL_WIDTH):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, LINE_COLOR, 2)

        for y in range(0, SCREEN_HEIGHT+1, PIXEL_WIDTH):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, LINE_COLOR, 2)
        arcade.start_render()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
