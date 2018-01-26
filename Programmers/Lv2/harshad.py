'''
[ 하샤드수 ]
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.

Harshad함수는 양의 정수 n을 매개변수로 입력받습니다. 이 n이 하샤드수인지 아닌지 판단하는 함수를 완성하세요.
예를들어 n이 10, 12, 18이면 True를 리턴 11, 13이면 False를 리턴하면 됩니다.
'''

'''
[ 접근방법 ]
문제에서 제시하는 의사코드를 구현할 수 있으면 크게 어려움 없는 문제이다. 크게 두 부분으로 나누면 아래와 같다.

1) 각 자리수의 덧셈을 한다.
2) 1에서 구한 값으로 n을 나누어 나머지의 여부를 확인한다.

위의 두 과정은 lv1 문제에서 등장했기 때문에 이를 해결했다면 쉽게 해결했을것이다.

다만 의사코드를 코드로 작성하는 것이 어렵거나 문제의 이해가 힘들어서 헤매는 경우가 있을 수 있다.
이럴땐 손으로 몇번 공책에 끄적이며 풀어보면 좋다.

'''

def harshad(n):
    result = 0
    temp = n

    # 자릿수의 합
    while temp > 0:
        result += temp % 10
        temp = temp // 10

    # 하샤드수 여부 확인
    return n % result == 0 and True or False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(harshad(18))