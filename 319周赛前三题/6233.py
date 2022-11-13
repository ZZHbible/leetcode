#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/13
# project = 6223
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32]
