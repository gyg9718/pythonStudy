# pythonStudy


## 객체지향 프로그래밍
실제 세계의 모든 것들이 여러 객체(object)들로 구성되어 있는 것과 유사하게, 소프트 웨어도 객체로 구성되어 있다는 생각에 바탕을 둔 프로그래밍 방법이 객체지향 프로그래밍(OOP: object-oriented programming)이다. 자바와 C++ 언어도 객체지향 프로그래밍 언어이다.

* 절차 지향 프로그래밍 기법 : 데이터를 다루는 명령어들이 모여 있는 함수들의 조합으로 프로그램을 만드는 방법.
* 객체 지향 프로그래밍 기법 : 위와 달리 데이터와 기능을 묶어 객체를 만들고 이것을 바탕으로 프로그램을 만드는 방법.
```
객체지향 프로그래밍의 장단점
: 이해하기 조금 어렵지만, 제대로 이해하고 프로그래밍하는 방법을 배우면 
나중에 고급 프로그램을 만들 때 쉽고 유지 보수하기 쉬운 장점이 있다.
```
```
객체는 상태와 동작을 가지고 있다.객체의 상태(state)는 객체의 속성이고, 객체의 동작(behavior)은 객체가 취할 수 있는 기능이다.
자동차를 예로 들면 제조사, 모델, 년식, 색상, 속도 등의 자동차의 속성이 있고
가속, 감속, 좌회전, 우회전 등 자동차가 할 수 있는 기능이 있다.
```
* 보통 속성은 변수로, 동직은 메소드(또는 멤버함수)로 구현한다.(클래스 안에서 구현되는 함수를 메소드라 한다.) ㅟ와같이 객체에 대한속석과 동작을 작성하는 설계도를 클래스(class)라고 하며, 클래스로부터 만들어지는 각각의 객체를 그 클래스의 인스턴스(instance)라고 한다.


## 클래스
객체 지향 프로그래밍에서 가장 핵심적인 내용은 클래스(class)인데 객체를 표현하기 위해 클래스를 만들어 사용한다.

일반적으로 클래스는 다음과 같은 모양으로 작성된다. 생성자, 멤버함수(들), 클래스변수는 들여쓰기를 한 블록에 정의한다.
보통 클래스 이름의 첫 글자는 대문자로 하는 것이 관습이다. 
### 클래스의 기본구조
```
class 클래스이름 : # class 키워드로 정의
  클래스 변수(옵션)
  메소드(들)
```
```python
class Car :
    def __init__(self, color, speed) :
        self.color = color
        self.speed = speed

    def speedUp(self, v):
        self.speed = self.speed + v
        return self.speed

    def speedDown(self, v):
        self.speed = self.speed - v
        return self.speed

    def speedDown(self, v):
        self.speed = self.speed - v
        return self.speed
c1 = Car('black', 50)
c2 = Car('red', 70)
print('Car c1 : color = ', c1.color, ', speed = ', c1.speed)
print('Car c2 : color = ', c2.color, ', speed = ', c2.speed)
c1.speedDown(10)
print('Car c1 : speed=', c1.speed)
```
위코드는 위(객체지향 프로그래밍 부분)에서 예를 들었던 자동차를 클래스를 사용해 나타낸 것이다.

## 생성자
__**생성자(constructor)** 는 인스턴스를 생성할 때 무조건 호출되는 메소드__ 인데, 반드시 이름을 __init__()이라고 붙인다. 매개변수에 self만 있는 생성자를 기본 생성자라고 한다.
```
위 프로그램의 2~4행이 생성자를 정의한 것인데 생성자의 첫 매개변수인 self는 클래스 인스턴스이다. slef를 사용하는 이유는 메소드 안에서 필드에 접근하기 위해서이다. 메소드 안에서 필드에 접근할 일이 없다면 self를 생략할 수 있지만 거의 모든 메소드의 첫번째 매개변수에 self를 사용한다. 위의 생성자는 self이외에 두 개의 매개변수 color, speed가 있다. 이렇게 생성자를 만들어 사용하면 인스턴스를 생성하면서 필드값을 초기화까지 할 수 있어 편리하다.

14~15행에서 객체를 만들때는 클래스 이름 뒤에 ()를 붙이고 괄호 속에 인자를 주면 되는데,  속도가 50인 검은색 차와 속도가 70인 빨간색 차를 각각 만들었다. 16~17행에서 두 차의 정보를 출력하고, 그 다음에 차 c1의 속도를 10만큼 감속한 후 속도 정보를 출력했다.
```
## 캡슐화
사람을 표현하기 위해 People이라는 이름의 클래스를 다음과 같이 정의했다. 처음 인스턴스를 만들 때 나이와 이름을 갖도록 생성자를 작성한다. 다음 프로그램은 두 인자 20과 'Kim'을 넘기면서 생성자를 불러 나이가 20이고 이름이 'Kim'이라는 객체(인스턴스)를 생성하도록 한다.
```python
class People:
  def __init__(self, age=0, name=None):
  self.__age = age
  self.name = name
 p1 = People(20, 'Kim')
 print(p1.name)
 print(p1.__age)
 ```
 위 프로그램을 실행해 보면 이름은 Kim이라고 제대로 출력하지만 나이는 제대로 출력되지 않고 아마도 다음과 같은 에러를 만나게 될 것이다.
 ```
 AttributeError: 'People' object has no attribute '__age' 
 ```
 ```
 이런 차이가 발생한 이유는 나이(age)의 변수명 앞에는 '__'가 있고, 이름(name)의 변수명 앞에는 '__'이 없기 떄문이다. 클래스 안에서 만든 변수의 이름 앞에 '__'를 추가해 사용하면 그 변수의 값은 외부에서 읽거나 변경하지 못한다. 따라서 self.name도 변수의 이름 앞에 'self.__name'으로 바꿔 쓰는것이 좋다.
``` 
이와같이 **데이터와 알고리즘을 하나로 묶어 공용 인터페이스만 제공하고 구현의 세부사항을 감추는 것을 캡슐화(enacapsulation)** 라고 한다

감춘 인스턴스 변수 값을 알고 싶거나, 바꾸고 싶을 때 사용할 수 있도록 클래스 내부에 인스턴스 변수값을 반환하는 접근자(getter)와 인스턴스 변수값을 설정하는 설정자(setter)를 구현하는 것이 좋다. 접근자와 설정자는 각각 get과 set으로 시작하는 이름으로 만드는 것이 관례이고 이들(접근자와 설정자)을 이용해 인스턴스 변수에 접근하는 예를 다음 프로그램에 


## 파일 입출력

### 파일 열기모드
|파일 열기모드|의미|
|:------------:|:---:|
|'w'|파일에 내용을 새로 쓸 때 사용|
|'r'|파일 내용을 읽을때 사용|
|'a'|파일에 내용을 추가할 때 사용|





### round함수
```
round(반올림할 숫자, 표시할 소수점 자릿수)
round(반올림할 숫자)
```
- round(37.666666666666664, 1) = 37.7
- round((50 + 45 + 33 + 39 + 29 + 30) / 6, 1) = 37.7

- round(4/3) = 1

### 향상for문
```
for 변수 in 리스트(또는 튜플이나 문자열):       # '변수'에 대입할 원소를 '리스트'에서 하나씩 가져옵니다
  수행할 문장                                  # 변수에 원소를 하나씩 대입할 때마다 문장을 수행합니다
```



### print 형식지정자
```
print('%d를 포함한 출력 내용' %%d에 넣을 숫자
print('%d, %d를 포함한 출력 내용' %(%d, %d에 넣을 숫자)
```
- print('%d' %5) == 5
- print('%d X %d = %d ' %(5, 4, 5*4) == 5 X 4 = 20


















