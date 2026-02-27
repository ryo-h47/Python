class Member:
    def __init__(self,nickname,account_id):
        self.nickname=nickname
        self.account_id=account_id
    def print_data(self):
        print(f"{self.nickname}の会員IDは{self.account_id}です")
a=Member("マリー・キュリー","MK210")
b=Member("アルベルト・アインシュタイン","AE314")
c=Member("二コラ・テスラ","NT271")
a.print_data()
b.print_data()
c.print_data()

sum=0
total=8
class vote:
    def __init__(self,country,position):
        self.country=country
        self.position=position
    def print_vote(self):
        global sum
        if self.position=="neutral":
          print(f"{self.country} is {self.position} on this amendment")
          sum+=1
        elif self.position=="for":
          print(f"{self.country} is {self.position} this amendment")
          sum+=1
        else:
          print(f"{self.country} is {self.position} this amendment")
    def result(self):
        global sum
        if sum>=total*2/3:
           print("The amendment was adopted")
        else:
           print("The amendment was rejected")

a=vote("United Kingdom","neutral")
b=vote("Russia","against")
c=vote("Pakistan","for")
d=vote("Iran","neutral")
e=vote("Costa Rica","for")
f=vote("South Africa","for")
g=vote("Austria","for")
h=vote("New Zealand","for")
a.print_vote()
b.print_vote()
c.print_vote()
d.print_vote()
e.print_vote()
f.print_vote()
g.print_vote()
h.print_vote()
h.result()
