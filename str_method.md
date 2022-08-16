str = 'Python programming is easy!'

기본 함수
```python
>>> print(str.upper()) # 문자열을 모두 대문자로 변환
PYTHON PROGRAMMING IS EASY! 
>>> print(str.lower()) # 문자열을 모두 소문자로 변환
python programming is easy!
>>> print(str.swapcase()) # 문자열의 대문자는 소문자로, 소문자는 대문자로 변환
pYTHON PROGRAMMING IS EASY!
>>> print(str.title()) # 문자열의 각 단어 앞 한자리만 대문자로 변환
Python Programming Is Easy!
```



문자열 찾기 함수

count(), find(), rfond(), index(), rindex(), startswith() -> True False로 반환, endwith()
```python                                             
>>> print(str.count('i')) # 문자열에서 'i'개수를 반환
2
>>> print(str.find('on')) # 문자열에서 'on'의 처음 위치. 없으면 -1반환
4
>>> print(str.rfind('sy')) # 문자열에서 'sy'가 나오는 가장 나중 위치.(또는 오른쪽부터 처음)
24
>>> print(str.index('on')) # 문자열에서 'on'의 처음 위치. 없으면 ValueError
4
```
문자열 개수 세기 함수 count()
```python
>>> print('apple pineapple'.count('pl))
2
```








문자열 공백 삭제, 제거 함수

strip(), rstrip(), lstrip(), replace()

str = ' hello '
```python
>>> print(str.strip()) # 양쪽에서 공백 제거 ( 본래 문자열은 변하지 않는다. print 후 str = ' hello ' )
'hello'
>>> print(str.rstrip() # 오른쪽 공백 제거
' hello'
>>> print(str.istrip() # 왼쪽 공백 제거
'hello '
```      


      
      
      
문자열 분리, 결합 함수

split(), sqlitlines(), join()

```python
s = 'a b' # a와 b사이 공백이 있다
str = 'abc'      
      
>>> print(s.split()) (= print(s.spilt(None)))
['a', 'b']
>>> print(str.split('b')) # 문자열을 ( )속의 문자로 분리 및 반환
['a', 'c']
>>> '*'.join('hello') # *와 문자열의 각 문자를 하나씩 결합한 문자열 생성
'h*e*l*l*o'
```      

  
      
문자열 정렬, 채우기 함수

center(), ljust(), rjust(), zfill()
```python
str = 'abc'
      
print(str.center(10))
>>> '   abc    '
print(str.senter(10, -))
>>> '---abc----'
'he'.rjust(5) # 5자리를 오른쪽으로 정렬
>>> '     he'
'he'.ljust(5) # 5자리를 왼쪽으로 정렬
>>> 'he     '
'he'.center(5) # 5자리를 가운데로 정렬
>>> '  he '
'12'.zfill(5) # 문자열 '12'의 왼쪽을 0으로 채워 5자리를 만든다
'00012'
```

      
 메서드 체이닝
```
 문자열 메서드는 처리한 결과를 반환하도록 만들어져 있습니다. 따라서 메서드를 계속 연결해 호출하는 메서드 체이닝(method channing)이 가능합니다.
```
다음은 문자열을 오른쪽으로 정렬한 뒤 대문자로 바꿉니다. 

```python
>>> 'python'.rjust(10).upper()
'    PYTHON'
```
