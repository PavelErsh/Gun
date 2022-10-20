from tkinter import SEL
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
       
    def update(self):
        if self.angle <= 0:
            self.angle = 0
        if self.angle >= 126:
            self.angle = 126
        self.angle+=self.change_angle
    
class Bullet(arcade.Sprite):
    def __init__(self, gun):
        super().__init__("bullet.png",0.05)
        self.gun = gun
        self.bottom = self.gun.top
        self.center_x = self.gun.center_x
        self.change_y = 2
    def update(self):
       self.center_y+= self.change_y
       self.change_y-=0.01

class Game(arcade.Window):
    def __init__(self, widht, height, title):
        super().__init__(widht, height, title)
        self.bg = arcade.load_texture("bg.jpg")
        self.left_wheel = arcade.load_texture("wheel.png")
        self.draw = False
        self.gun = Gun()
        self.bullet = Bullet(self.gun)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.gun.change_angle=-1
        if key == arcade.key.LEFT:
            self.gun.change_angle=1
        if key == arcade.key.SPACE:
            self.bullet = Bullet(self.gun)
            self.draw = True
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.gun.change_angle = 0
        
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDHT/2, SCEEN_HEIGHT/2, SCREEN_WIDHT, SCEEN_HEIGHT, self.bg)
        self.gun.draw()
        arcade.draw_texture_rectangle(self.gun.center_x, self.gun.center_y, 100, 100, self.left_wheel)
        if self.draw:
            self.bullet.draw()
    def update(self, delta_time):
        self.gun.update()
        if self.draw:
            self.bullet.update()


window = Game(SCREEN_WIDHT, SCEEN_HEIGHT, TITLE)
arcade.run()
