# 01. 순서대로 별찍기
# num_of_lines = int(input('라인수를 입력해주세요>>> '))

# for line_number in range(1, num_of_lines + 1):
#     print('*' * line_number)

#
# ---
#

# 02. 반전해서 별찍기
# num_of_lines = int(input('라인수를 입력해주세요>>> '))

# for line_number in range(num_of_lines):
#     num_of_stars = num_of_lines - line_number
#     print('*' * num_of_stars)

#
# ---
#

# 03. 우측 정렬 별찍기
# num_of_lines = int(input('라인수를 입력해주세요>>> '))

# for num_of_stars in range(1, num_of_lines + 1):
#     num_of_blanks = num_of_lines - num_of_stars
#     print(' ' * num_of_blanks + '*' * num_of_stars)

#
# ---
#

# 04. 우측 정렬 반전해서 별찍기
num_of_lines = int(input('라인수를 입력해주세요>>> '))

for line_number in range(0, num_of_lines):
    num_of_stars = num_of_lines - line_number

    print(' ' * line_number + '*' * num_of_stars)
