'''
[ 숫자의 표현 ]
수학을 공부하던 민지는 재미있는 사실을 발견하였습니다.
그 사실은 바로 연속된 자연수의 합으로 어떤 숫자를 표현하는 방법이 여러 가지라는 것입니다.
예를 들어, 15를 표현하는 방법은
(1+2+3+4+5)
(4+5+6)
(7+8)
(15)
로 총 4가지가 존재합니다.
숫자를 입력받아 연속된 수로 표현하는 방법을 반환하는 expressions 함수를 만들어 민지를 도와주세요.
예를 들어 15가 입력된다면 4를 반환해 주면 됩니다.
'''

'''
[ 접근방법 ]
1부터 n까지 차례대로 더해가며 총합이 n과 같은지, n보다 큰지, 작은지 비교한다.
총합이 n과 같은 경우 : 연속된 자연수의 합이니깐 answer에 +1을 한다
총합이 n보다 큰 경우 : 이 경우엔 범위를 벗어낫으므로 break
총합이 n보다 작은 경우 : 다음 숫자를 차례대로 더해가면서 위 두 조건이 나올때 까지 진행한다

1에서 시작하는 방법을 조사했으면 다음은 2에서 시작하는 방법... 이런식으로 n까지 진행한다

하지만 시간복잡도를 줄이기 위해 식을 더 단순화 할수 없을까 고민하다 보니 n이 홀수던 짝수이던
n//2 + 1이 최대 범위라는 것을 알아냈다. 예를 들어 15의 경우 15//2 + 1 = 8보다 더 큰 연속된 수는
2개만 더해도 15를 넘어간다 (ex 8 + 9 = 17)
따라서 기존에 num까지 구했던 경우를 num // 2 + 1 까지 구하면 시간복잡도를 반으로 줄일 수 있


'''
def expressions(num):
    answer = 1
    for i in range(1, num//2 + 1): # 기존엔 for i in range(1, num)
        sum = 0
        for j in range(i, num):
            sum += j
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(14));