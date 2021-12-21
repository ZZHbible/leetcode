#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/21
# project = leetcode1154

class Solution:
    def dayOfYear(self, date: str) -> int:
        l=date.split('-')
        year,month,day=int(l[0]),int(l[1]),int(l[2])
        def is_lump_year(year):
            if (year%4==0 and year%100!=0) or year%400==0:
                return True
            return False
        month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
        ret=0
        for i in range(month-1):
            ret+=month_day[i]
        ret+=day
        if is_lump_year(year) and month>2:
            ret+=1
        return ret