# 문자열 서식 지정자와 포매팅 사용하기
서식 지정자 또는 포매팅을 사용하는 예시로 학생의 이름과 평균점수를 출력한다고 할때,
```
제임스의 평균 점수는 87.7점 입니다.
```
```
마리아의 평균 점수는 98.7점 입니다.
```
와 같은 특정 부분을 원하는 값으로 바꿀 때 서식 지정자 또는 문자열 포매팅을 사용합니다.
## 서식지정자(format formating)
서식지정자의 사용 예시입니다.
* '%s' %'문자열'
아래 경우는 넣어야할 값이 두개 이상일 경우입니다.
* '%s%s' % ('문자열', '문자열')
* '%s%s%s' % ('문자열', '문자열', '문자열')
```python
>>> print('I am %s. ' % 'james')
I am james.
>>> print('My name is %s and her name is %s.' % ('james', 'maria')
My name is james and her name is maria.
```
서식지정자는 %로 
시작하며 그 뒤에 자료형을 뜻하는 문자가 붙습니다. %s는 문자열이라는 뜻이며 string의 s입니다. 이처럼 문자열안에 %s를 넣고 %'james'를 지정해주면 %s부분이 'james'로 바뀝니다.
변수로 지정하는 것도 가능합니다.
```python
>>> name = james
>>> print('I am %s' % name)
I am james
```
각각의 서식 지정자 예입니다.
* %d -> 정수
```python
>>> 'I am %d years old.' % 20
I am 20 years old
```
* %f -> 실수(기본적으로 소수점 이하 6자리까지 표시한다.)
```python
>>> '%f' % 2.3
2.300000
```
* %.자릿수f -> 자릿수 지정 실수
```python
>>> '%.2f' % 2.3
'2.30'
>>> '%.3f' % 2.3
'2.300'
```
서식지정자로 문자열 정렬하기
* % 길이s -> 오른쪽 정렬
```python
>>> '%10s' % 'python'
'    python'(공백 4칸, python)
```
* %-길이s -> 왼쪽 정렬
```python
>>> '%-10s' % 'python'
'python    '(python, 공백 4칸)
```

## 포매팅(string formating)
서식지정자 방식보단 더 간단한 문자열 포맹팅(string formating)입니다. 문자열 포매팅은 {}(중괄호) 안에 포매팅을 지정하고 format 메서드로 값을 넣습니다.
* '{인덱스}'.format(값)
```python
>>> 'Hello, {0}'.format('world!')
'Hello, world!'
>>> 'Hello, {0}'.format(100)
'Hello, 100'
```
서식지정자는 %뒤에 자료형에 맞는 알파벳을 넣어야하는 반면 포매팅은 중고라호 안에 포매팅 순서(들)만 지정하기만 하면 됩니다.

####  다음은 값을 여러개 넣는 방법입니다.
```python
>>> Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'Hello, Python 3.6 Script'
>>> '{0} {0} {1} {1}'.format('Python', 'Script')
'Python Python Script Script'
>>> Hello, {language} {version}'.format(language='Python', version=3.6
'Hello, Python Script 3.6'
```
