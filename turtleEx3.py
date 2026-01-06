# 리스트를 사용해 터틀 그래픽 응용 프로그램을 만든다
# 100마리에 대한 거북이를 리스트에 넣은 후 거북이가 임의의 좌표에 임의의 크기로, 임의의 색상으로
# 그리며 이동하도록 만든다.
# 리스트
# [거북이모양, x위치, y위치, 거북이크기, R, G, B]
# [[거북이모양, x위치, y위치, 거북이크기, R, G, B], [거북이모양, x위치, y위치, 거북이크기, R, G, B]
# , [거북이모양, x위치, y위치, 거북이크기, R, G, B], ....]

import turtle
import random

myTurtle, tX, tY, tSize, tColor, tShape = [None] * 6
shapeList = []
playerTurtles = []  # 거북이 2차원 리스트
sWidth, sHeight = 500, 500

turtle.title('리스트를 활용한 꼬북이')
turtle.setup(width = sWidth + 50, height = sHeight + 50)
turtle.screensize(sWidth, sHeight)

shapeList = turtle.getshapes()
for i in range(0, 100):
  random.shuffle(shapeList)  # 커서 모양
  myTurtle = turtle.Turtle(shapeList[0])    # 커서 모양
  tX = random.randint(int(-sWidth / 2), int(sHeight / 2)) # x좌표 
  tY = random.randint(int(-sHeight / 2), int(sHeight / 2)) # y좌표
  r = random.random(); g = random.random(); b = random.random() # 색상
  tSize = int(random.randrange(1, 3))
  playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
  
# print(playerTurtles)

for tList in playerTurtles:
  myTurtle = tList[0]
  myTurtle.color((tList[4], tList[5], tList[6]))
  myTurtle.pencolor((tList[4], tList[5], tList[6]))
  myTurtle.turtlesize(tList[3])
  myTurtle.goto(tList[1], tList[2])
  
turtle.done()