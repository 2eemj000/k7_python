import matplotlib.pyplot as plt

from bug_random import RandomWalk2DGrid

# RandomWalk2DGrid 객체 생성 및 랜덤 워크 수행
rw = RandomWalk2DGrid()
rw.fill_walk()

# 방문 횟수 시각화
plt.style.use('classic')
fig, ax = plt.subplots()
ax = ax.matshow(rw.visited, cmap=plt.cm.Blues)
ax.set_aspect('equal')

plt.show()