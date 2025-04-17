# src/config.py

import os

# config.py

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# 游戏逻辑上的画布尺寸（固定逻辑坐标系）
LOGIC_WIDTH = 1000
LOGIC_HEIGHT = 600


# 资源路径
BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "..", "images")
