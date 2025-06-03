import sys
print("Pythonバージョン:", sys.version)
print("Python実行ファイルのパス:", sys.executable)

try:
    import pygame
    print("Pygameバージョン:", pygame.__version__)
except ImportError:
    print("Pygameがインストールされていません")
