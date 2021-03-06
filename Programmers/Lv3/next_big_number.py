'''
[ 다음 큰 숫자 ]
어떤 수 N(1≤N≤1,000,000) 이 주어졌을 때, N의 다음 큰 숫자는 다음과 같습니다. N의 다음 큰 숫자는 N을 2진수로 바꾸었을 때의 1의 개수와 같은 개수로 이루어진 수입니다.
1번째 조건을 만족하는 숫자들 중 N보다 큰 수 중에서 가장 작은 숫자를 찾아야 합니다.
예를 들어, 78을 2진수로 바꾸면     1001110 이며, 78의 다음 큰 숫자는 83으로 2진수는 1010011 입니다.
N이 주어질 때, N의 다음 큰 숫자를 찾는 nextBigNumber 함수를 완성하세요.
'''

'''
[ 접근방법 ]
문제의 조건은 크게 2가지이다.

	1) n의 2진수의 값과 1이 같은 갯수여야 한다.
	2) 1의 조건과 동시에 가장 작은 수여야 한다.

n을 2진수로 변환하여 1이 몇개인지 샌 다음 n+1부터 1씩 증가시키며 1의 갯수가 같은지 판단했다.
'''

def nextBigNumber(n):
    cnt = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == cnt:
            return n


#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(949250))
