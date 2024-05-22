import matplotlib.pyplot as plt
from random import choice

class RandomWalk2DGrid:
    """2차원 그리드에서 랜덤 워크를 생성하는 클래스."""

    def __init__(self, rows=10, cols=10):
        """랜덤 워크의 속성을 초기화."""
        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        
    def fill_walk(self, x_start=0, y_start=0, num_points=100):
        x = x_start
        y = y_start
        
        while len(self.board) < num_points:
            # 이동할 방향을 결정.
            x_new = x + choice([1, 0, -1])
            y_new = y + choice([1, 0, -1])

            # 그리드 범위 내에 있는지 확인
            if 0 <= x_new < self.rows and 0 <= y_new < self.cols:
                # 새로운 위치를 방문한 것으로 표시
                self.board[x_new][y_new] += 1
                # 현재 위치를 업데이트
                x, y = x_new, y_new

    def plot_walk(self):
        plt.imshow(self.board, cmap=plt.cm.Blues, interpolation='nearest')
        plt.colorbar()
        plt.show()

# 테스트
rw = RandomWalk2DGrid()
rw.fill_walk()
rw.plot_walk()