import arcade
import math

SCREEN_WIDHT = 500
SCEEN_HEIGHT = 500
TITLE = "GUN"

class Gun(arcade.Sprite):
    def __init__(self):
        super().__init__("aa.png",0.1)
        self.center_x = SCREEN_WIDHT/2
        self.center_y = 100
        self.angle= 0
        #right 0
        #left 126
    def update(self):
        if self.angle <= 0:
            self.angle = 0
        if self.angle >= 126:
            self.angle = 126
        
        self.angle+=self.change_angle
        print(self.angle)
        
class Game(arcade.Window):
    def __init__(self, widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture("bg.jpg")
        self.left_wheel = arcade.load_texture("wheel.png")
        self.gun = Gun()
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.gun.change_angle=-1
        if key == arcade.key.LEFT:
            self.gun.change_angle=1
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.gun.change_angle = 0
        
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDHT/2, SCEEN_HEIGHT/2, SCREEN_WIDHT, SCEEN_HEIGHT, self.bg)
        self.gun.draw()
        arcade.draw_texture_rectangle(self.gun.center_x, self.gun.center_y, 100, 100, self.left_wheel)
    def update(self, delta_time):
        self.gun.update()


window = Game(SCREEN_WIDHT, SCEEN_HEIGHT, TITLE)
arcade.run()
