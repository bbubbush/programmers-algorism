'''
[ 2 x N 타일링 ]
1x1 정사각형 2개가 붙어 있는 타일이 있습니다. 이 타일을 이용하여 총 2xN 의 보드판을 채우려고 합니다.
타일은 가로, 세로 두 가지 방향으로 배치할 수 있습니다.

보드판의 길이 N이 주어질 때, 2xN을 타일로 채울 수 있는 경우의 수를 반환하는 tiling 함수를 완성하세요.

단, 리턴하는 숫자가 매우 커질 수도 있으므로 숫자가 5자리를 넘어간다면 맨 끝자리 5자리만 리턴하세요.

예를 들어 N = 2일 경우 가로로 배치하는 경우와 세로로 배치하는 경우가 있을 수 있으므로 2를 반환해 주면 됩니다.

하지만 만약 답이 123456789라면 56789만 반환해주면 됩니다.
리턴하는 숫자의 앞자리가 0일 경우 0을 제외한 숫자를 리턴하세요. 리턴타입은 정수형이어야 합니다.
'''

'''
[ 접근방법 ]
처음엔 n개가 각각 1, 2, 3, 4, 5 일때 나올수 있는 경우의 수를 노트에 다 그렸다. 그러다 발견한 내용이

n번째 타일의 수 = n-2번째 타일의 수 + n-1번째 타일의 수

즉 피보나치수열이었다. 단, 지문의 경우 5자리가 넘어가면 끝에 5자리만 반환하라는 말에서 Testcase가 엄청 큰 수겠구나
싶어서 메모이제이션을 사용했다. 그리고 n-1, n-2번째 타일의 수가 5자리가 넘는다고 하더라도 다섯자리 수를 더한 수는
올림을 버린 다시 다섯자리 수가 되기 때문에 답이 엉키는 것을 막을 수 있다.(이게 답이 엉킬거라고 생각해서 고민하느라
시간을 많이 소모했다) ex) n-2 타일의 수가 99999고 n-1 타일의 수가 11111이면 n 타일의 수는 111110에서 맨 앞을 제거한
11110이 된다. 앞이 0으로 끝나는 경우에도 전혀 문제가 되지 않는다.

'''

result = [0, 1, 2]

def tiling(n):
    if len(result) > n:
        return result[n] > 9999 and result[n] % 100000 or result[n]

    result.append(tiling(n-2) + tiling(n-1))

    return result[n] > 9999 and result[n] % 100000 or result[n]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(tiling(2))
print(tiling(132))