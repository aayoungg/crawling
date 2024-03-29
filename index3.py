import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

names = []
x = []
y = []
tel = []
category = []
address = []
abbrAddress = []

metropolitan = "서울특별시"
area = "관악구"
categories = "옷수선"

for page in range(1, 100): 
    url = f"https://map.naver.com/p/api/search/allSearch?query={metropolitan}{area}{categories}&type=all&searchCoord&page={page}"
    http_post_request = requests.get(url, headers=headers)
    print("http_post_request", url)
    data = http_post_request.json()
    if "result" not in data:
        break
    if "address" in data:
        address_info = data["address"]
        print('address', address_info)
    for item in data["result"]["place"]["list"]:
        names.append(item.get("name"))
        x.append(item.get("x"))
        y.append(item.get("y"))
        tel.append(item.get("tel"))
        category.append(item.get("category"))
        address.append(item.get("address"))
        abbrAddress.append(item.get("abbrAddress"))
        print(item.get("name"))
        print(item.get("x"))

# 데이터프레임 생성
df = pd.DataFrame({'상호명': names, '카테고리': category, '전화번호': tel, '주소': address, '주소(도로명)': abbrAddress, '위도': x, '경도': y})

# 데이터프레임을 엑셀 파일로 저장
file_name = f'{metropolitan} {area} {categories}.csv'
df.to_csv(file_name, encoding="cp949", index=False)
print(f'{file_name}로 저장되었습니다.')