# -*- coding: utf-8 -*-
"""event driven.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qS8bGaeUqtsZsCchrNg_6adQq1WQ9acm
"""

import tkinter
import time

def alarm():
  print('calling the pizza company.')

def doorbell():
  print('ding!')
  time.sleep(4)
  print('opening the door!')
def phonecall():
  print('answering the phone!')

root = tkinter.Tk()
tkinter.Button(root, text='Ring doorbell', command=doorbell).pack()
tkinter.Buttom(root, text='Call phone', command=phonecall).pack()

root.after(4000, alarm)

root.mainloop()