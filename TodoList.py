# • 클래스명: TodoList
# • 속성: owner, todos(문자열 리스트)
# • 생성자: owner (todos는 빈 리스트로 시작)
# • 메서드
# • add(task) : 할 일 추가
# • remove(task) : 할 일 삭제 (없으면 삭제하지 않기)
# • show() : 할 일 목록을 보기 좋게 문자열로 반환 (예: 번호 붙여 출력)

import json

class TodoList:
  owner = ''
  todos = []
  
  def __init__(self, owner='', todos = []):
    self.owner = owner
    self.todos = todos
  
  def add(self, task):
    self.todos.append(task)
    
  def remove(self, task):
    task = int(task)
    self.todos.pop(task-1)
    
  def show(self):
    print(f"{self.owner}의 할 일\n")
    for i in range(len(self.todos)):
      print(f"({i+1}) {self.todos[i]}\n")
  
  def to_dict(self) :
    return {
      "owner" : self.owner,
      "todos" : self.todos,
    }

  def to_json(self, pretty=True):
    return json.dumps(
      self.to_dict(),
      ensure_ascii=True,
      indent=2 if pretty else None
    )

todo1 = TodoList(owner="이민주", todos=['공부하기', '청소하기', '밥먹기'])
todo1.show()

todo1.add(input("추가할 요소 입력 : "))
todo1.show()

todo1.remove(input("삭제할 요소의 번호 입력 : "))
todo1.show()
      
print(todo1.to_json())