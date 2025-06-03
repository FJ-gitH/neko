import pygame
import sys

# ゲームの設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 40

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# マップデータ（0: 空きスペース, 1: 壁, 2: ゴール）
MAP_DATA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# プレイヤークラス
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

    def move(self, dx, dy):
        # 移動先の座標を計算
        new_x = self.x + dx
        new_y = self.y + dy

        # 壁との衝突判定
        if MAP_DATA[new_y // TILE_SIZE][new_x // TILE_SIZE] != 1:
            self.x = new_x
            self.y = new_y
            # ゴール到達の判定
            if MAP_DATA[new_y // TILE_SIZE][new_x // TILE_SIZE] == 2:
                return True
        return False

    def draw(self, screen):
        # ネコキャラクターを描画（シンプルな四角形）
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

def main():
    try:
        print("ゲームを開始します...")
        print(f"Pythonバージョン: {sys.version}")
        print(f"Pygameバージョン: {pygame.__version__}")
        
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("ネコの迷路ゲーム")
        clock = pygame.time.Clock()
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        raise

    # プレイヤーの初期位置
    player = Player(40, 40)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # キー入力処理
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move(0, -TILE_SIZE)
        if keys[pygame.K_DOWN]:
            player.move(0, TILE_SIZE)
        if keys[pygame.K_LEFT]:
            player.move(-TILE_SIZE, 0)
        if keys[pygame.K_RIGHT]:
            player.move(TILE_SIZE, 0)

        # 画面の描画
        screen.fill(BLACK)

        # マップの描画
        for y in range(len(MAP_DATA)):
            for x in range(len(MAP_DATA[0])):
                if MAP_DATA[y][x] == 1:  # 壁
                    pygame.draw.rect(screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif MAP_DATA[y][x] == 2:  # ゴール
                    pygame.draw.rect(screen, RED, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        # ゴール到達の判定と処理
        if player.move(0, 0):  # 移動処理の結果を確認
            # クリアメッセージの表示
            font = pygame.font.Font(None, 74)
            text = font.render("クリア！", True, RED)
            text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            screen.blit(text, text_rect)
            
            # リスタートの表示
            restart_text = font.render("Rキーでリスタート", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100))
            screen.blit(restart_text, restart_rect)
            
            # リスタート処理
            if keys[pygame.K_r]:
                player.x = 40
                player.y = 40
        else:
            # プレイヤーの描画
            player.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        print("ゲームを開始します...")
        print(f"Pythonバージョン: {sys.version}")
        print(f"Pygameバージョン: {pygame.__version__}")
        
        main()
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        input("Enterキーを押して終了してください...")
