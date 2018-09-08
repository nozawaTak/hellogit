#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

def tree(length):
	if length > 5:
		turtle.forward(length)
		turtle.right(20)
		tree(length-15)
		turtle.left(40)
		tree(length-15)
		turtle.right(20)
		turtle.backward(length)

turtle.speed(0)
turtle.color("green")
turtle.left(90)
turtle.backward(150)
tree(120)

print("hello")
print("testbranch")
print("hey!")
print("baaa")

print("agaa")

input('type to exit')
