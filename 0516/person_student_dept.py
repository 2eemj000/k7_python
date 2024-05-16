class Person:
    def __init__(self, pid, pname, age):
        self.pid = pid
        self.pname = pname
        self.age = age

class Dept():
    def __init__(self, department):
        self.department = department

class Student(Person):
    def __init__(self, pid, pname, age, sid, syear, sdept):
        super().__init__(pid, pname, age)
        self.sid = sid
        self.syear = syear
        self.sdept = sdept # 클래스 Dept의 생성자 호출

d1 = Dept('수학과')
d2 = Dept('화학과')
d3 = Dept('생명공학과')

s1 = Student('000p1','가영',25,'000s1',2000,d1)
s2 = Student('000p2','나영',24,'000s2',2001,d2)
p3 = Person('000p3','다영',26)
p4 = Person('000p4','라영',29)
p5 = Person('000p5','마영',21)
p6 = Person('000p6','바영',26)
p7 = Person('000p7','사영',26)
s8 = Student('000p8','아영',26,'000s8',1999,d3)
s9 = Student('000p9','자영',23,'000s9',2002,d2)
s10 = Student('000p10','차영',26,'000s10',1999,d1)

class MyList:
    def __init__(self, data):
        self.data = data
    def __getitem__(self,index):
        return self.data[index]
    def __str__(self):
        return '\n'.join(str(item) for item in self.data)
    
def detail_tList(obj):
    if isinstance(obj, Person):
        if isinstance(obj, Student):
            return (f"Student(pid={obj.pid}, pname={obj.pname}, age={obj.age}, "
                    f"sid={obj.sid}, syear={obj.syear}, sdept={obj.sdept.department})")
        return f"Person(pid={obj.pid}, pname={obj.pname}, age={obj.age})"
    elif isinstance(obj, Dept):
        return f"Dept(department={obj.department})"
    return str(obj)

tList=MyList([s1,s2,p3,p4,p5,p6,p7,s8,s9,s10])
print('\n'.join(detail_tList(item) for item in tList))
