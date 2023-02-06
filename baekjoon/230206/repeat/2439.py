import sys

a = int(sys.stdin.readline())

for i in range(1, a+1):
    print(('*'*i).rjust(a))

    #오른쪽 정려 .rjust(몇칸) 왼쪽정렬.ljust(몇칸) 전체차리수 .zfill(전체자리수) 남은 숫자는 0으로 처리