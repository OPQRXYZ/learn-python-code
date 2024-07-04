from re import A
# 정수 number와 n,m이 주어지며, number 가 n 의 배수이면서 m 의 배수라면 1을 아니면 0을 return하도록 solution 함수를 작성하시오
def solution(number,n,m): # answer함수 생성
    if number%n == 0:  # n이 number의 공배수일 경우
        if number%m == 0: # m이 number의 공배수일 경우
            return True
        else:
          return False
    else :
        return False
number=int(input("공배수인 정수를 적어주세요"))
n=int(input("1번째 인수를 적어주세요"))
m=int(input("2번째 인수를 적어주세요"))
if solution(number,n,m)==True:
  print(1)
elif solution(number,n,m) == False:
  print(0)
else:
  print("오류")