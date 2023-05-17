### 스택 Stack (선입후출)
- append() : 가장 뒤쪽에 데이터 삽입
- pop() : 가장 뒤쪽에서 데이터를 꺼냄

### 큐 Queue (선입선출)
- from collections import deque : collections 모듈에서 제공하는 deque 라이브러리 사용
- 변수명 = deque()
- 변수명.popleft() : 가장 앞쪽에서 데이터를 꺼냄
### 재귀 함수 Recursive Function
- 자기 자신을 다시 호출하는 함수
```
def R_fcn():
  print('재귀 함수를 호출합니다.")
  R_fcn()
  
R_fcn()
# 어느 정도 출력하다가 오류 메시지를 출력
 ```
 
- 재귀 함수는 종료 조건을 곡 명시, 무한 호출을 방지
```
def R_fcn(i):
  if i == 100:
    return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    R_fcn(i + 1)
    print(i, '번째 재귀 함수를 종료합니다.')
    
R_fcn(1)
```
- 2가지 방식으로 구현한 팩토리얼
