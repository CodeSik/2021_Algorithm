
'''
1. 입력
1) input()
    한줄의 문자열을 입력받는 함수
2) input().split()
    문자열을 공백 기준으로 나눠서 리스트로 반환.
3) map()
    리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
'''
import sys


def input_method():
    #데이터의 개수 입력
    n = int(input())
    #각 데이터를 공백을 기준으로 구분하여 입력
    #map 함수를 통해 각 원소에 int 함수를 적용함.

    #이러한 형식이 아주 많이 쓰임. 정수형으로 보통 코딩테스트에서 사용되기 때문임.
    data = list(map(int,input().split()))

    data.sort(reverse=True)
    print(data)

    #리스트 형식 말고, 3개 정도 들어온다고 치면 각 변수에 입력값을 저장할 수 있음.
    #우항에서 packing, 좌항으로 unpacking
    a,b,c = map(int, input().split())
    print(a,b,c)

    '''
    입력을 최대한 빠르게 받아야 하는 경우?
    sys.stdin.readline()
    단 입력 후 엔터가 줄 바꿈 기호로 입력되므로, rstrip() 메서드를 함께 사용함.
    시간 복잡도를 줄이기 위한 테크닉.
    '''

    #import sys
    data =sys.stdin.readline().rstrip()
    print(data)

'''
출력은 print()
1. , 로 구분해서 출력 가능하다.
2. 기본적으로 출력 이후 줄 바꿈을 수행한다.
    원치 않으면 end 속성을 이용할 수 있다.
'''
def print_method():
    a=1
    b=2
    print(a,b)
    print(7, end= " ")
    print(8, end= " ")

    answer = 7
    #answer를 형변환
    print("정답은 "+str(answer) + "입니다")

    '''
    1. f-string
        파이썬 3.6부터 사용 가능하며 문자열 앞에 접두사 'f'를 붙여 사용한다.
        중괄호 안에 변수명을 넣어서 간단히 문자열과 정수를 함께 넣을 수 있다.
    '''
    print(f"정답은 {answer}입니다.")