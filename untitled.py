# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16lCiXCCw-OJG2vBSvyBu4X2frzKZC2S6
"""

def yotoqxonadagi_talabalar(raqami):
    if raqami=="401":
       return "4-etaj"
    elif raqami=="301":
       return "3-etaj"
    elif raqami=="201":
       return "2-etaj"
    elif raqami=="101":
       return "1-etaj"
    else:
       return "Bunday xona mavjud emas"
raqami=input("Xona raqamini kiriting")
natija=yotoqxonadagi_talabalar(raqami)
print (natija)