import os

LEVELS_DIR = os.path.join(RES_DIR, "levels")
LEVEL_PLACEHOLDERS_DIR = os.path.join(RES_DIR, "levels", "placeholders")
GFX_DIRS = os.path.join(RES_DIR, "gfx")
FONTS_DIR = os.path.join(RES_DIR, "fonts")
SOUNDS_DIR = os.path.join(RES_DIR, "sounds")

FPS = 60

#objetos
elements = {}
elements_list = []
levels = {}
pipes = {}
active_states = set()
current_level = None