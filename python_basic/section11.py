# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv
# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # Header(1행)를 패스
    next(reader)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    # delimiter 속성을 통해 구분자가 무엇인지 알려줌
    reader = csv.reader(f, delimiter='|')
    # Header(1행)를 패스
    next(reader)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# 예제3(Dict변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for c  in reader:
        for k, v in c.items():
            print(k, v)
        print('---------------')

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

# newline : 줄바꿈 처리를 어떻게 할 것인지 정하는 속성
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        # if등의 조건문을 통해서 검수를 통해서 쓸 수있음
        wt.writerow(v)

# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    # 조건 상관없이 한번에 작성하는 함수
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas



# 예제6
import pandas as pd

# sheet_name = '시트명' 또는 숫자, header =숫자, skiprow=숫자 
xlsx = pd.read_excel('./resource/sample.xlsx', sheet_name=0)

# 상위 데이터 확인
# head() : 1~5번째 값만 보여줌
print(xlsx.head())

# 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) #행, 열

# 엑셀 or CSV 파일 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)