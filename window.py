
import arcade

from chess import Chess
from const import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH, BACKGROUND_COLOR, PIXEL_WIDTH, LINE_COLOR
from calculate import caculate_index


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        self.chess_list = arcade.SpriteList()
        self.is_chess_x = True

    def on_mouse_press(self, x, y, button, modifiers):
        chess = Chess(self.is_chess_x, caculate_index(x), caculate_index(y))
        self.chess_list.append(chess.img)
        self.is_chess_x = not (self.is_chess_x)

    def on_draw(self):
        arcade.start_render()
        for x in range(0, SCREEN_WIDTH+1, PIXEL_WIDTH):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, LINE_COLOR, 2)

        for y in range(0, SCREEN_HEIGHT+1, PIXEL_WIDTH):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, LINE_COLOR, 2)

        self.chess_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
