'''
[ 자연수를 뒤집어 리스트로 만들기 ]
digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.
'''

'''
[ 접근방법 ]
문제의 포인트는 다음과 같다.

1) 파라미터의 타입은 문자열, 리턴 타입은 리스트이다.
2) 파라미터의 값을 뒤집어 리스트의 맨 앞부터 담아야 한다.

위의 두 조건만 충족한다면 어떤 알고리즘을 짜도 실패할 가능성이 적다.


'''

def digit_reverse(n):
    return [int(i) for i in str(n)[::-1]]
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)))