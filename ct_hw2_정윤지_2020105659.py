
def unitconversion():
    while(True):
        code = input("면적 변환기능: A, 길이 변환기능: L, 종료: Q\t입력:")
        #다른 입력코드를 입력하면 입력코드를 입력하는 초기 상태로 돌아간다.

        if (code == 'Q' or code == 'q'):
            break

        elif (code == 'A' or code == 'a'):
            areacode = int(input("평 -> m^2 변환: 1, m^2 -> 평 변환: 2\t입력: "))
            if (areacode == 1):
                area = int(input("평 -> m^2 변환입니다. 변환하고자 하는 면적 값(숫자)을 입력하세요: "))
                print("%f평은 %fm^2입니다." % (area, area*3.3))
            elif (areacode == 2):
                area = int(input("m^2 -> 평 변환입니다. 변환하고자 하는 면적 값(숫자)을 입력하세요: "))
                print("%fm^2는 %f평입니다." % (area, area/3.3))
            else:
                print("코드를 잘못 입력했습니다. 초기 화면으로 돌아갑니다.")
                continue

        elif (code == 'L' or code == 'l'):
            lengthcode = int(input("cm -> inch 변환: 1, inch -> cm 변환: 2\t입력: "))
            if (lengthcode == 1):
                length = int(input("cm -> inch 변환입니다. 변환하고자 하는 길이 값(숫자)을 입력하세요: "))
                print("%fcm는 %finch입니다." % (length, length/2.54))
            elif (lengthcode == 2):
                length = int(input("inch -> cm 변환입니다. 변환하고자 하는 길이 값(숫자)을 입력하세요: "))
                print("%finch는 %fcm입니다." % (length, length*2.54))
            else:
                print("코드를 잘못 입력했습니다. 초기 화면으로 돌아갑니다.")
                continue
        
        else:
            print("코드를 잘못 입력했습니다. 초기 화면으로 돌아갑니다.")
            continue

def sumadjoin():
    data = [4, 28, 43, 21, 8, 26, 23, 48, 29, 22, 
1, 27, 27, 25, 14, 1, 38, 46, 31, 28, 
42, 35, 44, 26, 37, 17, 8, 1, 39, 48, 
2, 19, 14, 41, 31, 40, 11, 30, 48, 23, 
0, 10, 25, 47, 32, 19, 40, 8, 19, 45]
    length = len(data)
    num = int(input("합계할 인접한 숫자의 개수: "))
    if (num == 0 or num == 1 or num == length):
        print("숫자의 범위가 잘못되었습니다.")
    else:
        maxsum = 0
        for i in range(0, length - num + 1):
            sum = 0
            for j in range(0, num):
                sum += data[i+j]
            if (sum > maxsum):
                maxsum = sum
        print(maxsum)


def main():
    unitconversion()
    sumadjoin()

main()