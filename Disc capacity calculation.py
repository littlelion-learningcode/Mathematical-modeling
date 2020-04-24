#！/usr/bin/env python3.7.4
#-*- coding: utf-8 -*-
# Author:lucky,time:2020/4/21

import math

p=math.pi           #获取pi值
laser_name=['红外(CD)','红色(DVD)','蓝色(DVD)']   #定义激光器数组
laser_length=[0.78,0.64,0.41]                   #定义激光波长数组
channel_spacing=[0.0016,0.00074,0.00032]        #定义信道间距数组
linear_density=[121,387,800]                    #定义数据线密度数组
clv_out_radius = 58                 #clv外圆半径
clv_in_radius = 22.6                #clv内圆半径
cav_out_radius = 58                #cav外圆半径
cav_in_radius = cav_out_radius/2   #cav内圆半径

def L_CLV_FUNC(R2,R1,d):        #定义计算LCLV的函数
    L_CLV = (p * (R2**2-R1**2))/d
    return L_CLV

def L_CAV_FUNC(R2,R1,d):        #定义计算LCAV的函数
    L_CAV = (2*p*R1*((R2-R1)/d))
    return L_CAV

#CLV光盘的信息容量
print('CLV光盘的信息容量:')
print('激光器\t   激光波长/um\t 信道长度/mm\t 信息容量/MB\t 影像时间/min')
for i in range(3):
    L_CLV = L_CLV_FUNC(clv_out_radius, clv_in_radius, channel_spacing[i])       #计算CLV光盘的信道长度
    C_CLV = (L_CLV * linear_density[i])/1000**2         #计算CLV光盘的信息容量
    IMAGE_TIME = C_CLV/0.62/60          #计算CLV光盘在此容量下能够存储的影像时间
    print(laser_name[i],'\t',laser_length[i],'\t\t',    int(L_CLV),'\t\t',int(C_CLV),'\t\t',   int(IMAGE_TIME))

#CAV光盘的信息容量
print('\nCAV光盘的信息容量:')
print('激光器\t   激光波长/um\t 信道长度/mm\t 信息容量/MB\t 影像时间/min')
for i in range(3):
    L_CAV = L_CAV_FUNC(cav_out_radius,cav_in_radius,channel_spacing[i])           #计算CAV光盘的信道长度
    C_CAV = (L_CAV * linear_density[i])/1000**2             #计算CAV光盘的信息容量
    IMAGE_TIME = C_CAV/0.62/60               #计算CAV光盘在此容量下能够存储的影像时间
    print(laser_name[i], '\t', laser_length[i], '\t\t', int(L_CAV), '\t\t', int(C_CAV), '\t\t', int(IMAGE_TIME))