import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel', 'asd']
births = [968,155,77,578,973,666]
custom = [1,5,25,13,232232]

BabyDataset = list(zip(names,births))

#데이터 프레임 선언
#print(BabyDataset)

#
df = pd.DataFrame(data = BabyDataset, columns=['Names', 'Births'])

#print(df)
#
# #.head() 가장 앞 5개만 출력
#print(df.head())

#데이터 타입
#print(df.dtypes)

# 인덱스 정보
# print(df.index)

# 칼럼정보
# print(df.columns)

# 특정 칼럼명으로 열 가져오기
#print(df['Names'])

#print(df[1:4])

# 데이터 프레임 조건을 주는 형태로 만드릭
#print(df[df['Births']>600])

#평균값 계산하기
#print(df['Births'].mean())


#넘파이 기본 활용

#배열 자동 생성
arr1 = np.arange(15).reshape(3,5)
# print(arr1)
# print(type(arr1))

#배열 형태 확인
#print(arr1.shape)

#배열의 요소 타입 확인
#print(arr1.dtype)

#요소가 0인 배열
# arr3 = np.zeros((3,4))
# print(arr3)

#배열을 이용한 사칙연산
# arr4 = np.array([[1,2,3], [4,5,6]], dtype= np.float64)
# arr5 = np.array([[7,8,9], [10,11,12]], dtype= np.float64)
# print("arr4 + arr5 =\n", arr4 + arr5)
# print("arr4 - arr5 =\n", arr4 - arr5)
# print("arr4 * arr5 =\n", arr4 * arr5)
# print("arr4 / arr5 =\n", arr4 / arr5)
#
# a = [[1,2,3],[4,5,6]]
# b = [[7,8,9],[10,11,12]]
# c = []
#
# for i in range(len(a)):
#     d = []
#     for y in range(len(a[0])):
#         d.append(a[i][y] + b[i][y])
#     c.append(d)

# print(a[0][0] + b[0][0])
# print(a[0][1] + b[0][1])
# print(a[0][2] + b[0][2])

# print(a[1][0] + b[1][0])
# print(a[1][1] + b[1][1])
# print(a[1][2] + b[1][2])

# print(c)
#
# a = [[1,2,3],[4,5,6]]
# b = [[7,8,9],[10,11,12]]
# for i in range(len(a)):
#     for y in range(len(a[i])):
#         a[i][y] += b[i][y]
# print(a)
#

# y = df['Births']
# x = df['Names']
# #막대 그래프를 출력합니다.
# plt.bar(x, y) #막대 그래프 객체 생성
# plt.xlabel('Names') #x축 제목
# plt.ylabel('Births') #y축 제목
# plt.title('Bar plot') #그래프 제목
# plt.show() #그래프 출력


#랜덤 추출 시드를 고정합니다.
np.random.seed(19920613)

#산점도 데이터를 생성합니다
x = np.arange(0.0, 100.0, 5.0)
y = (x * 1.5) + np.random.rand(20) * 50

#산점도 데이터를 출력합니다. c의 의미는 색깔, b는 blue의 약자
plt.scatter(x, y, c="b", alpha = 0.5, label = "scatter point")
plt.xlabel("X")
plt.ylabel("Y")
#범례 세팅
plt.legend(loc='upper left')
#그래프 이름
plt.title('Scatter plot')
plt.show()

# # 200ms 간격으로 균일하게 샘플된 시간
# t = np.arange(0., 5., 0.2)
#
# # 빨간 대쉬, 파란 사각형, 녹색 삼각형
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()