animals = [
    '사자',
    '호랑이',
    '고양이',
    '강아지'
]

# 01. 데이터 추가하기
animals.append('낙타')

# 02. 데이터 삭제하기
del animals[2]

# 03. 부분 배열 추출
slicedAnimals = animals[1:3]

# 04. 배열 길이
numOfAnimals = len(animals)

# 05. 정렬
animals.sort(reverse=True)
print(animals)