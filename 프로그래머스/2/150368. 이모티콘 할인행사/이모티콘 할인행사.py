from itertools import product

def solution(users, emoticons):
    n = len(users)  # 사용자 수
    m = len(emoticons)  # 이모티콘 수

    max_join = 0  # 최대 가입자 수
    max_sales = 0  # 최대 매출액

    # 할인율 조합 생성
    discounts = [10, 20, 30, 40]
    discount_combinations = list(product(discounts,repeat= m))
    # 각 조합별로 이모티콘 판매 액수 계산
    for discount_set in discount_combinations:
        join_count = 0  # 가입자 수
        sales = 0  # 매출액
        for user in users:
            user_ratio, user_price = user
    
            # 이모티콘 구매 여부 결정
            buy_emoticons = []
            for i in range(m):
                if user_ratio <= discount_set[i]:
                    buy_emoticons.append([i+1,discount_set[i]])

            # 이모티콘 구매 비용 계산
            
            total_price = sum([int(emoticons[i[0]-1]*(100-i[1])/100) for i in buy_emoticons])
            
            # 이모티콘 구매 비용이 일정 가격 이상인 경우 이모티콘 플러스 서비스 가입
            if total_price >= user_price:
                join_count += 1
            else:
                sales += total_price
        # print(join_count,sales)
            
        # 최대 가입자 수와 최대 매출액 갱신
        if join_count > max_join:
            max_join = join_count
            max_sales = sales
        elif join_count==max_join:
            max_sales = max(sales,max_sales)

        # print(" max : ",max_join,max_sales)
    return [max_join, max_sales]