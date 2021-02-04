
'''
파이썬의 조건문
쉬운 내용이라 대부분 스킵했음.

if / elif / else
중요한건 elif는 if의 조건문에 해당 안되면서, elif의 조건문을 만족할 때 분기가 걸림.

pass 키워드
아무것도 처리하고 싶지 않을 때 (디버깅 할 때 사용)

한줄일 경우에는 간략하게 표현 가능.
if score >= 80: result = "Success"
else: result = "Fail"

if ~ else를 한줄에 작성 가능.
score = 85
result = "Success" if score >= 80 else "Fail"

파이썬은 수학의 부등식을 그대로 쓸 수 있음.

x > 0 and x < 20은
0 < x < 20 과 같음.
'''
def condition_statement():
    x = 15
    if x>10:
        print("큼.")
    else:
        pass

    score = 85
    result = "Success" if score >= 80 else "Fail"
    print(result)