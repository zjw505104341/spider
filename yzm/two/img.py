# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2020/6/30 11:07

def is_px_equal(img1, img2, x, y):
    """
    判断两个像素是否相同
    :param img1: 图片1
    :param img2:图片2
    :param x:位置1
    :param y:位置2
    :return:像素是否相同
    """
    pix1 = img1.load()[x, y]
    pix2 = img2.load()[x, y]
    threshold = 60

    if abs(pix1[0] - pix2[0]) < threshold and abs(pix1[1] - pix2[1]) < threshold and abs(pix1[2] - pix2[2]) < threshold:
        return True
    else:
        return False

def get_gap(img1, img2):
    """
    获取缺口偏移量
    :param img1: 不带缺口图片
    :param img2: 带缺口图片
    :return:
    """
    left = 0
    for i in range(left, img1.size[0]):
        for j in range(img1.size[1]):
            if not is_px_equal(img1, img2, i, j):
                left = i
                return left
    return left