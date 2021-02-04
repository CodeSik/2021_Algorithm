#이코테 2021 with python

'''
파이썬의 자료형
정수형 / 실수형 / 복소수형 / 문자 / 리스트 / 튜플 / 사전

--> 파이썬의 나누기 연산자(/)의 결과는 실수형이다.
--> 나머지 연산자(%), 몫을 얻기위한 연산자(//), 거듭 제곱 연산자(**)
--> in / not in을 통해 리스트, 튜플, 문자열, 딕셔너리에서 데이터가 포함되어 있는지 확인 가능
'''
def IntegerdataType():
    #Integer
    #코딩테스트에서는 주로 정수형을 다룬다.

    a = 1000
    print(a)
    a = -7
    print(a)
    a = 0+30
    print(a)


def RealNumberdataType():
    #Real Number
    #파이썬은 변수에 소스점을 붙인 수를 대입하면 실수형 벼수로 처리된다.

    a=157.93
    print(a)
    #5.0
    a=5.
    print(a)
    #-0.7
    a=-.7
    print(a)
    #지수표현 방식, 1e9는 1 * 10^9, 이는 실수 데이터임.로
    #최단 경로 알고리즘에서 도달할 수 없는 노드에 대해 최단거리를 무한으로 설정하곤 함.
    INF = 1e9
    #정수형으로 변환하는 것이 좋음.
    INF = int(1e9)

    '''
    컴퓨터는 실수를 정확히 표현하는데 한계가 있어, 근삿값으로 표현하기 때문에 비교하는게 어렵다.
    따라서 밑의 소스코드는 False를 출력한다.
    a=0.8999999999999
    --> round()함수를 사용함.
    --> 123.456을 셋째자리에서 반올림 하려면, round(123.456,2) =123.46
    '''

    #False
    a = 0.3 + 0.6
    print(a)
    if a == 0.9:
        print(True)
    else:
        print(False)

    #True
    a = 0.3 + 0.6
    print(round(a,4))
    if round(a,4) == 0.9:
        print(True)
    else:
        print(False)

'''
사용자 입장에서 C, Java의 배열의 기능 및 연결 리스트와 유사한 기능을 지원한다.
C++ STL의 vector와 기능적으로 유사하다.
리스트 대신 배열, 테이블이라고 부르기도 함.

'''
def ListDataType():
    '''
    1. 리스트 초기화
    대괄호([])안에 원소를 넣어 초기화, 쉼표로 원소 구분
    비어있는 리스트 선언은 list() 혹은 [] 이용
    '''

    #직접 데이터를 넣어 초기화
    a = [1,2,3,4]
    print(a)

    #2번째 원소만 출력
    print(a[1])

    #크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
    n=10
    a=[0]*n
    print(a)

    '''
    2. 인덱싱
    인덱스 값을 입력해 리스트의 특정한 원소에 접근하는 것
    '''
    a = [1,2,3,4,5,6,7,8,9]
    print(a[7])
    print(a[-1]) #뒤에서 첫번째 원소 출력, 9
    print(a[-3]) #뒤에서 3번째 원소 출력, 7
    a[3] = 7
    print(a)

    '''
    3. 슬라이싱
    연속적인 위치를 갖는 원소들을 가져와야 할 때 이용함.
    대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있음.
    끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.
    '''
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #index 1부터, 3까지 가져오는것
    #2,3,4
    print(a[1:4])

    '''
    4. 리스트 컴프리헨션
    리스트를 초기화하는 방법 중 하나.
    대괄호 안에 조건문과 반복문을 적용해 리스트를 초기화 할 수 있다.
    '''
    #0부터 9까지의 수를 포함하는 리스트 초기화
    #반복문 먼저 넣는 것을 추천.
    #반복문의 변수가 담기도록 함.
    arr = [i for i in range(10)]
    print(arr)

    #0부터 19까지의 수 중, 홀수만 포함하는 리스트
    arr = [i for i in range(20) if i%2 == 1]
    print(arr)

    #1부터 9 까지의 수들의 제곱 값을 포함하는 리스트
    arr = [i*i for i in range(10)]
    print(arr)

    #2차원 리스트를 초기화 하는 법

    #N*M 크기의 2차원 리스트 초기화
    n=4
    m=3
    # 3*4 크기의 2차원 리스트
    print("정상 예")
    '''
    여기서의 _(언더바)는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용하는 것이다.
    '''
    arr = [[0]*m for _ in range(n)]
    arr[1][1] = 5
    print(arr)

    # 잘못된 예시
    # arr = [[0]*m]*n
    # 위 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식됌.시
    print("잘못된 예시, 같은 객체로 인식하여 모두 동일한 값으로 됌. 같은 주소를 참조하기 때")
    arr = [[0]*m]*n
    arr[1][1] = 5
    print(arr)

    '''
    5. 리스트의 Method
    1) 변수명.append() / 끝에 삽입 O(1)
        리스트에 원소를 끝에 삽입할 때 사용
    2) 변수명.sort() = 오름차순 / 변수명.sort(reverse=True) = 내림차순 O(NlogN)
        리스트를 정렬할 때 사용
    3) 변수명.reverse() O(N)
        리스트의 원소의 순서를 모두 뒤집음.
    4) 변수명.insert(index,value) O(N)
        특정 index에 값을 삽입할 때
    5) 변수명.count(value) O(N)
        value라는 특정 값의 데이터 갯수를 세어주는 함수
    6) 변수명.remove(value) O(N)
        특정한 값을 갖는 원소를 제거하는데, 여러개면 하나만 제거함.
    따로 코드를 작성하진 않겠다.
    다만 특정값 여러개를 제거할 때는 어떻게 하는지 코드만 적어보겠다.
    '''
    a = [1,2,3,4,5,5,5]
    remove_set = {3,5} # 집합 자료형
    #remove_list에 포함되지 않은 값만을 저장
    result = [i for i in a if i not in remove_set]
    print("3과 5를 제외함",result)


'''
문자열 변수를 초기화 할때는 큰따옴표("), 작은 따옴표(') 사용
'''
def StringDataType():
    data = "Hello World"
    print(data)
    # 문자열 안에 큰 따옴표 넣을 때 \" 사용.
    data = "Dont u know \"Python\"?"
    print(data)

    '''
    1. 문자열 연산
    +: 문자열 변수를 더하면 연결이 됌.
    *: 문자열 변수를 곱하면 여러번 더해짐.
    문자열도 인덱싱과 슬라이싱이 가능하지만 특정 인덱스의 값을 변경할 수는 없음.
    '''
    a = "ABCDEF "
    print(a+a)
    print(a*3)
    print(a[2:4])
    #a[2]='a' 불가.

'''
튜플 자료형은 리스트와 유사하지만 문법적 차이가 있음.
1. 한번 선언된 값을 변경할 수 없다.
2. 리스트는 대괄호를 사용하지만, 튜플은 소괄호 () 를 이용한다.
튜플은 리스트에 비해 공간 효율적이다.

사용하면 좋은 경우?
1. 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
    최단 경로 알고리즘에서 (비용, 노드번호)의 형태로 튜플 자료형을 사용한다.
2. 데이터의 나열을 해싱의 Key 값으로 사용해야 할 때
    변경이 안되기 때문에 키값으로 사용 가능.
3. 메모리를 효율적으로 사용해야 할 때
'''
def TupleDataType():
    a = (1,2,3,4,5,6,7,8,9)
    #Indexing, Slicing 지원
    print(a[3])
    print(a[1:4])
    #a[2]=2 불가.

'''
사전 자료형
Key와 Value의 쌍을 데이터로 가지는 자료형임. (리스트, 튜플이 값을 순차적으로 저장하는 것과 대비 됌.)
사전자료형을 키와 값의 쌍을 데이터로 가지며, 원하는 변경 불가능한(Immutable) 자료형을 키로 사용할 수 있다.
파이썬의 사전 자료형은 해시 테이블을 이용해서 조회 및 수정의 시간 복잡도가 O(1)임.
'''

def DictDataType():
    #초기화 방법 1
    data = dict()
    data['사과'] = "Apple"
    data['바나나'] = "Banana"
    data['코코넛'] = "Coconut"

    #초기화 방법 2
    b={
        '홍길동' : 97,
        '이순신' : 98
    }
    print(data)
    print(b)
    if '사과' in data:
        print("'사과' 존재함.")

    '''
    1. 관련 메서드
    1) keys()
        키 데이터만 뽑아서 객체로 반환
        리스트로 쓰기 위해선 list()안에 넣어 객체 변환 해야 함.
    2) values()
        값 데이터만 뽑아서 객체로 반환
        리스트로 쓰기 위해선 list()안에 넣어 객체 변환 해야 함.
    '''
    key_list = data.keys()
    value_list = data.values()
    print(list(key_list))
    print(value_list)

    #각 키에 따른 값을 하나씩 출력
    for key in key_list:
        print(data[key])

'''
집합 자료형
1. 중복을 허용하지 않음.
2. 순서가 없음.
집합은 리스트 혹은 문자열을 이용해서 초기화 할 수 있음.
이때 set()함수를 이용함.
혹은 중괄호({}) 안에 각 원소를 콤마로 구분하여 초기화할 수 있음.
'''

def SetDataType():
    #초기화 방법 1
    data = set([1,1,2,3,4,4,5])
    print(data)

    # 초기화 방법 2
    data = {1,1,2,3,4,4,5}
    print(data)
    '''
    1. 연산
    1) 합집합
    2) 교집합
    3) 차집
    '''
    a = set([1,2,3,4,5])
    b = {3,4,5,6,7}

    #합집합
    print(a|b)
    #교집합
    print(a&b)
    #차집합
    print(a-b)

    '''
    2. 관련 메서드
    1) add(value) 한 원소 추가
    2) update(value1,value2) 여러 원소 추가 
    3) remove(value) 특정 값 삭제
    '''

'''
사전 자료형과 집합 자료형의 특징
리스트, 튜플은 순서가 있기 때문에 Indexing으로 자료형의 값을 얻음.
사전 자료형, 집합은 순서가 없기 때문에 Indexing으로 얻을 수 없음.
--> Key 또는 원소를 이용해 O(1)로 조회함.
'''


