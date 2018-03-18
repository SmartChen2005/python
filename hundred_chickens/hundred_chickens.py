# -*- coding: utf-8 -*-

"""
百鸡问题：
公鸡一只5元，
母鸡一只3元，
小鸡三只1元，
如何用100元买100只鸡？
"""

for gong in range(0,21):
    for mu in range(0,34):
        for xiao in range(3,301,3):
            if 5*gong+3*mu+xiao/3.0 == 100 and gong+mu+xiao == 100:
                print("公鸡买"+str(gong)+"只,母鸡买"+str(mu)+"只,小鸡买"+str(xiao)+"只")
