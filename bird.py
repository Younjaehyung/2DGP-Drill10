# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, load_font
import time
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100,1400), 90
        self.face_dir = 1
        self.frame = 0
        self.action =2
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.frame  == 0:
            self.action -= 1
        if self.action == 0:
            self.action = 2
        self.x += self.face_dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600 or self.x < 0:
            self.face_dir *= -1


    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * 180 + 20, self.action * 150 + 30, 180, 150, 0, 'V',self.x, self.y)
        else:
            self.image.clip_draw(int(self.frame) * 180 + 20, self.action * 150 + 30, 180, 150, self.x, self.y)
