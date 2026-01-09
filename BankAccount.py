import json

# • 클래스명: BankAccount
# • 속성: owner(예금주), balance(잔액)
# • 생성자: owner, balance(기본값 0)
# • 메서드
# • deposit(amount) : 잔액에 입금
# • withdraw(amount) : 잔액에서 출금 (잔액 부족이면 출금하지 않기)
# • info() : "홍길동님의 잔액: 10000원" 형태 문자열 반환

class BankAccount:
  owner = ''
  balance = 0
  amount = 0
  
  def __init__(self, owner='', balance=0):
    self.owner = owner
    self.balance = balance
  
  def deposit(self, amount) :
    self.balance += amount
    
  def withdraw(self, amount) :
    self.balance -= amount
    
  def info(self):
    print(f"{self.owner}님의 잔액 : {self.balance}원")
  
  def to_dict(self) :
    return {
      "owner" : self.owner,
      "balance" : self.balance,
    }

  def to_json(self, pretty=True):
    return json.dumps(
      self.to_dict(),
      ensure_ascii=True,
      indent=2 if pretty else None
    )

bank1 = BankAccount(owner="이민주", balance=50000)
bank1.info()

bank1.deposit(30000)
bank1.info()

bank1.withdraw(5000)
bank1.info()

print(bank1.to_json())

    