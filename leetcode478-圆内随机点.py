#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/5
# project = leetcode478-圆内随机点
import math
import random
from typing import List

import matplotlib.pyplot as plt


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius=radius
        self.x_center=x_center
        self.y_center=y_center

    def randPoint(self) -> List[float]:
        angle=random.random()*(2*math.pi)
        radius=math.sqrt(random.random())*self.radius
        x_bias=math.cos(angle)*radius
        y_bias=math.sin(angle)*radius
        return [self.x_center+x_bias,self.y_center+y_bias]

solution=Solution(1,0,0)
for _ in range(3000):
    point=solution.randPoint()
    plt.scatter(point[0],point[1])

plt.show()
