# 정수 number와 n,m이 주어지며, number 가 n 의 배수이면서 m 의 배수라면 1을 아니면 0을 return하도록 solution 함수를 작성하시오
def solution(number,n,m): # answer함수 생성
  result =0
  for i in range(n,number,n):
    print(i)
    if number ==i:
      print("found!")
      break
  for i in range(m,number,m):
    print(i)
    if number ==i:
      print("found!")
      break

number=int(input("공배수인 정수를 적어주세요"))
n=int(input("1번째 인수를 적어주세요"))
m=int(input("2번째 인수를 적어주세요"))
solution(number,n,m)