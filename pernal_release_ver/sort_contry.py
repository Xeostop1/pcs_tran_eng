# 파일에서 데이터 읽기
with open("sort_contry_rec.txt", "r") as file:
    lines = file.readlines()

# 국가명과 원본 줄 추출 및 저장
entries = []
for line in lines:
    try:
        country = line.split(">")[1].split("<")[0]
        entries.append((country, line))
    except IndexError:
        print(f"Skipping invalid line: {line.strip()}")

# 국가명을 기준으로 오름차순 정렬
entries.sort()

# 결과를 새 txt 파일에 쓰기
with open("sorted_countries.txt", "w") as f:
    for _, entry in entries:
        f.write(entry)
