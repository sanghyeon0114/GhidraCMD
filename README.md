# GhidraCMD 

- 실행 방법

python setup.py

./print_log.sh [file_name]

- 출력 없이 디컴파일하여 log 파일만 만들고 싶을 때.

./decompile.sh [file_name]

-> file_name는 print_log.sh 파일 위치로부터 파일의 상대 경로를 적어주시면 됩니다.


# 파일 구조 설명

- logs

바이너리의 디컴파일된 코드를 파일 형태로 저장하는 위치

- projects

decompile을 위해 ghidra의 프로젝트를 생성하는 위치


# 동작 원리

ghidra는 바이너리를 디컴파일 해주는 GUI 툴입니다.

ghidra를 실행하고 나면 python 코드를 작성하여 기드라 라이브러리를 활용할 수 있습니다.

만약 ghidra를 GUI가 아닌 CLI로 활용하고 싶다면, analyzeHeadless 명령어를 활용할 수 있습니다.

( 경로는 ghidra폴더/support/analyzeHeadless 에 위치해 있음. )

파이썬으로 ghidra 라이브러리를 활용하려면 ghidra를 통해 파이썬 코드를 실행해야 하기 때문에 
analyzeHeadless CLI를 활용하여 파이썬 코드를 실행하여 디컴파일 정보를 CMD 창에 띄워줍니다.


# 참고

https://static.grumpycoder.net/pixel/support/analyzeHeadlessREADME.html