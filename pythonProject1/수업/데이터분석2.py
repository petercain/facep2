# 판다스 라이브러리 설치
# (데이터 분석 라이브러리)
# 데이터 프레임 만들기
#
# 넘파이 라이브러리
# 수치계산 라이브러리
#
# 멧플롯립 라이브러리
# 데이터 시각화 라이브러리
# ->다양한 그래프
#
# 정부제공 자료 또는 Raw Data형태들
# (csv파일 불러와서 dataFrame으로)
# csv를 db에 넣어서 용할 수 도 있지만
#
# 데이터 전처리
# Raw Data가 있으면 이를 수집하기, 보여주기 쉽게 하기 위한 작업
# csv


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'chipotle.tsv'
file_path2 = 'drinks.csv'

chipo = pd.read_csv(file_path, sep= '\t')
drinks = pd.read_csv(file_path2)
# #
# print(chipo.shape)
# print("--------------------------")
# print(chipo.info())
#
#
#
# print(chipo.columns)
# print("---------------------------")
# print(chipo.index)
# # ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
chipo['order_id'] = chipo['order_id'].astype(str)
# # ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# #기초통계량 출력하기
# print(chipo.describe())
#
# #범주형 피처의 개수 출력하기, unique -> 중복안되게, len으로 길이(개수)
# #select count(order_id)from chipo -> 쿼리라면?
# print(len(chipo['order_id'].unique()))
# print(len(chipo['item_name'].unique()))
#
# #가장 많이 주문한 아이템 Top 10 출력하기
# Item_count = chipo['item_name'].value_counts()[:10]
# print(Item_count)
#
# for idx, (val, cnt) in enumerate(Item_count.iteritems(), 1):
#     print("Top", idx, ":", val, cnt)
#
# print(type(idx))
# print(type(val))
# print(type(cnt))
#
# #스타복스 같은거를 만들었을때, 공공데이터 csv
# #UI에 반영하면 Top 10 이런거 시각화해서 보여줄 수 있다.
#
# #아이템별 주문 개수와 총량
# #groupby로 아이템별로 묶고, 주문수량을 count로 구한다.
# order_count = chipo.groupby('item_name')['order_id'].count()
# print(order_count[:10]) #아이템별 주문 개수를 출력합니다
# #주문기록을 남겨봤으니까 주문기록에서 메뉴별로 개수를 구하시오
# #slecet menu,count() from ORDERED gruup by menu
#
# # #아이템별 주문 총량
# # #groupby로 아이템별로 묶고, 아이템 수의 합 sum으로 구한다.
# item_quantity = chipo.groupby('item_name')['quantity'].sum()
# # print(item_quantity)
# #
# # #시각화로 분석 결과 살펴보기
#
# item_name_list = item_quantity.index.tolist()
# x_pos = np.arange(len(item_name_list))
# order_cnt = item_quantity.values.tolist()
#
# #그래프 세팅, order_cnt자료 활용
# plt.bar(x_pos, order_cnt, align= 'center') #(x축,y축,정렬)
# #t라벨 이름
# plt.ylabel('ordered_item_count')
# #x라벨 이름
# plt.title('Distribution of all orderd item')
#
# plt.show()
#
# print(x_pos) #아이템 리스트의 길이(개수)
# print(order_cnt) #아이템별 주문 개수 총량을 리스트로 변환
# print(type(order_cnt))
#
#
#전처리 #  $표시 떄문에 계산할 수 가 없다
# print(chipo.info)
# print("----------------------------")
#print(chipo['item_price'].head())
# #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
#처리 후 $표시 제거 후 다시 itme_price에 저장 (float형태로 , 첫번째부터 가져온다.
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
# #☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
#print(chipo.describe())
#
#
# #주문당 평균 계산금액 출력하기
# #주문당(order_id로 groupby)금액의 총합의 평균(sum().mean())
# averagePrice = chipo.groupby('order_id')['item_price'].sum().mean()
# print(averagePrice)
# # #######################################################################################
#여기까지함
# # #######################################################################################
#한 주문에 10달러 이상 지불한 주문 번호(id) 출력하기
# chipo_order_group = chipo.groupby('order_id').sum()
# results = chipo_order_group[chipo_order_group.item_price >= 10]
# print(results[:10])
# print(results.index.values)

# #각 아이템의 가격 구하기
# #주문번호에서 수량이 하나인 주문은 주문가격이 아이템의 가격이다
# #수량이 하나인 order 구하기
# chipo_one_item = chipo[chipo.quantity == 1]
# #해당 item_name기준으로 최저값 구하기
# price_per_item = chipo_one_item.groupby('item_name').min()
# #오름차순으로 정렬하기(ascending = False) (ascending 뜻, 오름차순, 내림차순은 descending)
# results = price_per_item.sort_values(by = "item_price", ascending=False)[:10]
# print(results)

# #가장 비싼 주문에서 아이템이 총 몇개 팔렸는지 구하기
# #order_id로 묶은 후 가격을 더하고 가격별로 내림차순 정렬
# results = chipo.groupby('order_id').sum().sort_values(by = 'item_price', ascending = False)[:5]
# print(results)

# #'Veggie Salad Bowl'이 몇 번 주문 되었는지 구하기
# #'Veggie Salad Bowl'이 몇 번 주문 되었는지 계산
# chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
# #한 주문 내에서 중복 집계된 item_name을 제거 (duplicates 중복 의미)
# chipo_salad = chipo_salad.drop_duplicates(['item_name', 'order_id'])
# pd.set_option('display.max_columns', 4)
# #개수
# print(len(chipo_salad))
# #리스트
# print(chipo_salad.head(5))


# #'Chicken Bowl을 2개 이상 주문한 주문 횟수 구하기
# #item_name이 Chicken Bowl인 것 구하기
# chipo_chicken = chipo[chipo['item_name'] == "Chicken Bowl"]
#
# #같은 주문번호로 묶고 더하고 Chiken Bowl의 수량을 구한다
# chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']
#
# #위에서 구한 CHiken Bowl의 수량이 2이상인 거슬 구한다.
# chipo_chicken_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]
# print(len(chipo_chicken_result))
# print(chipo_chicken_result.head(5))







# #국가별 음주 데이터 분석하기
# print(drinks.info)
# print(drinks.head(10))

#print(drinks.describe())

#피처(요소,칼럼)간의 상관 관계
#데이터간의 관계(양의 관계냐 음의 관계냐)

#beer 소비량과 와인소비량의 상관 계수를 계산합니다.
corr = drinks[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].corr(method = 'pearson')
print(corr)


cols_view = ['beer', 'spirit', 'wine', 'alcohol']
sns.set(font_scale = 1.5)
hm = sns.heatmap(corr.values,
                 cbar = True,
                 annot = True,
                 square = True,
                 fmt = '.2f',
                 annot_kws = {'size':15},
                 yticklabels = cols_view,
                 xticklabels = cols_view)

plt.tight_layout()
# plt.show()

sns.set(style = 'whitegrid', context = 'notebook')
sns.pairplot(drinks[['beer_servings', 'spirit_servings',
                     'wine_servings', 'total_litres_of_pure_alcohol']], height = 2.5)
plt.show()
