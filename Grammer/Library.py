'''
코테에서 자주 쓰이는 표준 라이브러리
1. 내장함수
2. itertools
    반복되는 형태의 데이터를 처리하기 위한 기능 제공
    특히 순열, 조합 라이브러리
3. heapq
    힙 자료구조를 제공, 일반적으로 우선순위 큐 를 구현하기 위해 사용
4. bisect
    이진 탐색 기능 제공
5. collections
    덱, 카운터 등의 유용한 자료구조 포함
6. math
    필수적인 수학적 기능 제공
    팩토리얼, 제곱근, 최대공약수, 삼각함수, 파이와 같은 상수
'''



def innerFunction():
    '''
    1. 내장 함수 모음
    '''
    #sum
    result = sum([1,2,3,4,5])
    print(result)

    #min(), max()
    min_result = min(7,3,4,2)
    max_result = max(7,3,4,2)
    print(min_result,max_result)

    #eval()
    #사람의 입장에서 표현된 것을 반환해주는 함
    result = eval("(3+5)*7")
    print(result)

    #sorted()
    result = sorted([9,1,8,5,4])
    result_reverse = sorted([9,1,8,5,4],reverse=True)
    print(result,result_reverse)

    #sorted() with key
    #두번째 인자를 기준으로 정렬함.
    #두번째 인자는 함수가 들어가는데, lambda를 통해 구현했음.
    array = [('홍길동',35), ('이순신',75),('아무개',50)]
    result = sorted(array, key= lambda x:x[1],reverse=True)
    print(result)

    '''
    2. 순열과 조합 --> itertools
    1) 순열
        서로 다른 n개에서 서로 다른 r개를 선택해 일렬로 나열하는 것
    2) 조합
        서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
    '''
    # 모든 순열 구하기
    from itertools import permutations
    data = ['A','B','C']
    result = list(permutations(data,3))
    print(result)

    #모든 조합 구하기
    from itertools import combinations
    result = list(combinations(data,2))
    print(result)

    #중복 순열 구하기
    from itertools import product
    result = list(product(data,repeat=2))
    print(result)

    #중복 조합 구하기
    from itertools import combinations_with_replacement
    result = list(combinations_with_replacement(data,2))
    print(result)

    '''
    3. Collection 라이브러리, Counter
    등장 횟수를 세는 기능을 제공.
    리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇번 씩 등장했는지 알려준다.
    '''
    from collections import Counter
    counter = Counter(['red','blue','red','green','blue','blue'])
    print(counter['blue']) # blue의 등장 횟수
    print(counter['green']) # green의 등장 횟수
    print(dict(counter)) # 각 요소의 등장 획수를 사전 자료형으로 반환

    '''
    4. Math
    최대 공약수, 최소 공배수
    '''

    import math

    def lcm(a,b):
        return a*b // math.gcd(a,b)

    a = 21
    b = 14
    print(math.gcd(a,b))
    print(lcm(a,b))