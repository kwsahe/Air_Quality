import pandas as pd

# 설정: 데이터 경로 및 저장 경로
INPUT_FILE = "data/who_air_quality_data.xlsx"
OUTPUT_FILE = "data/processed_data.csv"

# 데이터 전처리 함수
def preprocess_data(input_file, output_file):
    # 데이터 읽기
    try:
        data = pd.read_excel(input_file, sheet_name="Update 2024 (V6.1)")
    except Exception as e:
        print(f"데이터를 읽는 중 오류 발생: {e}")
        return

    # 필요한 열 선택
    columns_to_keep = [
        'country_name', 'city', 'year', 'pm25_concentration', 'pm10_concentration'
    ]
    data = data[columns_to_keep]

    # 결측값 처리
    data = data.dropna(subset=['pm25_concentration', 'pm10_concentration'])  # 주요 열의 결측값 제거
    data = data.fillna(0)  # 기타 결측값은 0으로 대체

    # 연도 데이터를 월별 데이터로 확장
    def expand_to_monthly(row):
        return [
            {
                'country_name': row['country_name'],
                'city': row['city'],
                'year': row['year'],
                'month': month,
                'pm25_concentration': row['pm25_concentration'],
                'pm10_concentration': row['pm10_concentration']
            }
            for month in range(1, 13)
        ]

    monthly_data = data.apply(lambda row: expand_to_monthly(row), axis=1)
    monthly_data = [item for sublist in monthly_data for item in sublist]  # 리스트 평탄화

    # DataFrame으로 변환
    processed_data = pd.DataFrame(monthly_data)

    # 결과 저장
    try:
        processed_data.to_csv(output_file, index=False)
        print(f"전처리 완료. 파일이 저장되었습니다: {output_file}")
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")

# 실행
if __name__ == "__main__":
    preprocess_data(INPUT_FILE, OUTPUT_FILE)
