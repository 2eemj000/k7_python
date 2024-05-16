class Car2:
    """자동차 클래스"""

    def __init__(self, make, model, year, color):
        """생성자 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer = 0

    # 던더메소드 [!!!__eq__, __len__, __str__, __del__ 알아두기!!!]
    # (__str__처럼 자동호출되는 것도 있고, del(__del__)이나 ==(__eq__)처럼 간단하게 호출가능한 것도 있음)
    # https://wikidocs.net/192020, https://blog.naver.com/youndok/222566232550
    
    def __str__(self): # 객체를 string으로 바꾸기
        return f"[{self.make},{self.model}]"

    def fill_gas_tank(self):
        print(f"휘발유 차의 탱크")

    def get_descriptive_name(self):
        """자동차 객체 기술"""
        long_name = f"{self.year}식 {self.make}제조사 {self.model} 색상은 {self.color}입니다"
        return long_name
    
    def update_odometer(self, mileage):
        print(f"주행기록계")

class Battery():
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

class ElectricCar(Car2): #(Car2)가 슈퍼클래스
    """슈퍼클래스의 subclass"""
    def __init__(self, make, model, year, color):
        """슈퍼클래스의 생성자 호출"""
        super().__init__(make, model, year, color)
        self.battery = Battery() # 클래스 Battery의 생성자 호출
    def fill_gas_tank(self):
        super().fill_gas_tank() # 오버라이드 하기 전 원래대로 실행
        print(f"전기차는 탱크 없음") # 오버라이드(재정의)

my_new_car = Car2('audi', 'a6', 2024, 'red')
print(my_new_car) # 던더메소드 확인 (출력하기 위해서는 string필요 -> 객체를 str으로 전환필요 -> __str__() 자동호출)
print(my_new_car.get_descriptive_name())

# 속성값 직접 수정하기
my_new_car.color = 'green' # 클래스 객체의 attribute는 public이므로 main에서도 접근가능
print(my_new_car.get_descriptive_name())

# 메서드를 통해 속성값 수정하기
my_new_car.update_odometer(23)

# 오버라이드 확인
my_electric_car = ElectricCar('kia','k3',2024,'red')
my_electric_car.fill_gas_tank()