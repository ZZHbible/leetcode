# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy
import datetime
import os
import numpy as np
import pandas as pd
import scipy
from scipy import constants
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super(Student, self).__init__(fname,lname)
        print("hello")
    
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n<=0:
        return False
    while n%3==0:
        n//=3
    if n==0:
        return True
    return False

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(self, root) -> bool:
    ret=True
    def digui(root):
        nonlocal ret    # 内函数中想修改闭包变量
        if not root:
            return 0
        left_depth=1+digui(root.left)
        right_depth=1+digui(root.right)
        if abs(left_depth-right_depth)>1:
            ret=False
        return max(left_depth,right_depth)

    digui(root)
    return ret

def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    bcopy=copy.deepcopy(board)
    directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    n=len(board)
    m=len(board[0])
    for i in range(n):
        for j in range(m):
            flag=board[i][j]
            temp=0
            for direction in directions:
                x=i+direction[0]
                y=j+direction[1]
                if x>=0 and x<n and y>=0 and y<m:
                    if board[x][y]==1:
                        temp+=1
            if flag:
                if temp<2 or temp>3:
                    bcopy[i][j]=0
            else:
                if temp==3:
                    bcopy[i][j]=1
    board[:]=bcopy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello")
    i=[1,2]
    print(i[3:])

    # map={1:"a",2:"b"}
    # map_copy=copy.deepcopy(map)
    # map[1]="good"
    # print(map)
    # print(map_copy)



    # board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    # board_copy=copy.deepcopy(board)
    # board[0][0]=100
    # print(board)
    # print(board_copy)
    #
    # a=[1,2,3,4]
    # b=copy.deepcopy(a)
    # b[2]=9
    # print(a)
    # str="hello"
    # for index,i in enumerate(str):
    #     print(index,i)
    # a=[1,2]
    # if 1: pass
    # elif 1:
    #     pass
    # if os.path.exists("demofile.txt"):
    #     os.remove("demofile.txt")
    # else:
    #     print("file not exist")
    #
    # a=np.array([1,2.0,3])
    # print(np.ndim(a))
    # print(a.dtype)
    # str="hello  world     goood  "
    # print(str.split())

    # a=np.array([[1,2,3],[4,4,5]])
    # b=np.array([[4,5,6],[4,4,5]])
    # print(np.stack((a,b),axis=1))
    # print(np.sum(a,axis=0))
    # print(np.where(a - 0 > 1))
    #
    # calories = {"day1": [420], "day2": [380], "day3": [390]}
    # myvar = pd.DataFrame(calories)
    # print(myvar)
    # print(dir(constants))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
