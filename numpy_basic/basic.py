# coding: utf-8
from numpy import *
random.rand(4,4)
randMat = mat(random.rand(4,4))
randMat.A
randMat.I
randMat
invRandMat = randMat.I
randMat*invRandMat
randMat*invRandMat - eye(4)
