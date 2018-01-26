'''
[ 핸드폰번호 가리기 ]
별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 "*"으로 바꿔야 합니다.
전화번호를 문자열 s로 입력받는 hide_numbers함수를 완성해 별이를 도와주세요
예를들어 s가 "01033334444"면 "*******4444"를 리턴하고, "027778888"인 경우는 "*****8888"을 리턴하면 됩니다.
'''

'''
[ 접근방법 ]
핸드폰번호 뒷자리 4개는 무조건 남아야 하고, 앞에는 길이에 따라 *의 갯수가 달라저야 한다.
전체 길이에서 -4 한 값 만큼 *을 붙이고, 맨 뒤에 숫자 4개를 붙여 출력하면 된다.

복잡하게 생각하면 복잡해질수 있는 문제니깐 한가지 방법만 고민하기 보다 다양하게 풀어보는 것이 좋다.

'''


def hide_numbers(s):
    return "*"*len(s[0:-4]) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'))