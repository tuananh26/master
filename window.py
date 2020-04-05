
import arcade

from chess import Chess
from definiteClass import Index
from const import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, BACKGROUND_COLOR, PIXEL_WIDTH, LINE_COLOR, NUMBER_COLUMN, NUMBER_ROW
from calculate import caculate_index
from function import is_chess_exists


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        self.chess_img_list = arcade.SpriteList()
        self.chess_type = True
        self.chess_list = []
        self.board = []

    def on_mouse_press(self, x, y, button, modifiers):
        chess_temp = Chess(
            self.chess_type, caculate_index(x), caculate_index(y))
        if not(is_chess_exists(chess_temp, self.chess_list)):
            self.chess_list.append(chess_temp)
            self.chess_img_list.append(chess_temp.img)
            self.chess_type = not(self.chess_type)

    def on_draw(self):
        arcade.start_render()
        for x in range(0, SCREEN_WIDTH+1, PIXEL_WIDTH):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, LINE_COLOR, 2)

        for y in range(0, SCREEN_HEIGHT+1, PIXEL_WIDTH):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, LINE_COLOR, 2)

        self.chess_img_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
