import turtle
import random

# 지역변수 : 함수나 모듈내에서 생성된 변수. 그 함수가 모듈이 종료되면 소멸됨.

def screenLeftClick(x, y) :
  print("마우스 왼쪽 버튼 눌림! ", x, y)
  turtle.pencolor((r, g, b))
  turtle.pendown()
  turtle.goto(x, y)
  
def screenMidClick(x, y) :
  print("마우스 미디 버튼 눌림! ", x, y)
  global r, g, b
  tSize = random.randrange(1, 10)
  turtle.shapesize(tSize)   # 커서 크기 변경
  r = random.random()
  g = random.random()
  b = random.random()
  
  
# 전역변수 : 현재 파일이 로딩 되어 실행이되면 메모리에 생성, 끝나면 종료
pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('꼬북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)

turtle.done()