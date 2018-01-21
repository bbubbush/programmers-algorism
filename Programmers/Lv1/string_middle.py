'''
[ 가운데 글자 가져오기 ]
getMiddle메소드는 하나의 단어를 입력 받습니다. 단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요. 
단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.
'''

'''
[ 접근방법 ]
전체길이가 홀수인지 짝수인지 나머지를 통해 판단하고, 홀수면 가운데 한글자를, 짝수면 가운데 2글자를 리턴해주면 된다.

'''

def string_middle(str):
    return len(str) % 2 == 0 and str[len(str)//2 -1:len(str)//2 +1 ] or str[len(str)//2]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("te12st"))