# open(): 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# readline(): 파일 객체로부터 한 줄씩 문자열을 읽는 함수
# readlines(): 전체 내용을 한 번에 리스트에 담는 함수

# file 을 open 하면 close 하는 과정이 번거롭게 느껴질 수 있다.
# file을 자동으로 열러주고, 자동으로 닫아주는 기법, 즉, 메모리에 자동할당하는 기법을 활용해보자
# 편리한 파일 입출력을 지원하는 문법을 다음으로 알아보자
# with 문법이다.

# 특정 파일을 읽어서 그 객체를 f 라고 하겠다 고 설정한다.
# with 구문이 나오는 순간 자동으로 파일 객체의 메모리가 자동 해제 되기 때문에
# 굳이 파일의 close 함수를 불러오지 않아도 자동으로 파일 객체에 사용되는 리소스가 자동으로
# 해제된다는 특징이 있다.

with open("input.txt", "r", encoding= "UTF-8") as f:
    list = f.readlines()
     # 모드 줄을 읽 내용을 list에 담았다가 list 원소 처리기법 활용할 수 있다.
    for i, data in enumerate(list): #enumerate()는 각 원소에 접근 수 있도록
        # 리스트의 인덱스와 원소를 접근한다.
        print("%d번째 줄: %s" %(i+1, data), end='')
# open하는 부분과 close 하는 부분이 생략된다.
# 코드가 짧아지고 간결해 지는 것은 우리가 원하는 목표이다.






