# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:04:48 2021

@author: DUONG NGOC HIEU
"""

#part1
#câu1: Viết chương trình Python thỏa mãn điều kiện sau:
#a) Kiểm tra một mảng cho trước gồm 4 phần tử. Chương trình sẽ tìm tổng số lượng số nguyên tố trong mảng đó?
# Kiểm tra SNT
a= [1,5,6,7,11]
def KT(arr):
    count =0
    for i in arr:
        if(i<2):
            count=count+1
        else:
            for j in range (2,i-1):
                if(i%j==0 and j<i):
                    count= count+1
                    break
    return len(arr)-count

print(KT(a))
#b) Dùng pytest kiểm tra lại hàm trên với ít nhất ba tình huống: