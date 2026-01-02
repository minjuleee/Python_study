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

def screenRightClick(x, y) :
  # 마우스 오른쪽 버튼을 클릭하면 콘솔창에 "마우스 오른쪽 버튼 눌림!" 과 좌표값 출력하세요
  # 꼬북이가 그림을 그리지 않으면서 x, y 좌표로 이동되도록 코딩 해보세요.
  # hint : penup()
  print("마우스 오른쪽 버튼 눌림! ", x, y)
  # turtle.pencolor((r, g, b))
  turtle.penup()
  turtle.goto(x, y)
  
  
# 전역변수 : 현재 파일이 로딩 되어 실행이되면 메모리에 생성, 끝나면 종료
pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('꼬북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()