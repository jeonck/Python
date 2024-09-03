
# 파이썬 네이밍 규칙 및 예시

파이썬에서 많이 사용하는 변수명 및 함수명의 네이밍 규칙과 예시는 다음과 같습니다.

## 1. 변수명 및 함수명 네이밍 규칙

- **snake_case**: 단어를 소문자로 작성하고, 단어 사이를 밑줄(`_`)로 연결합니다. 이는 파이썬에서 가장 일반적으로 사용되는 규칙입니다.
  - 예시: `total_sum`, `user_name`, `calculate_area`

- **CamelCase (PascalCase)**: 각 단어의 첫 글자를 대문자로 작성합니다. 주로 클래스 이름에 사용됩니다.
  - 예시: `EmployeeData`, `StudentRecord`

## 2. 함수명

- **동사로 시작**: 함수명은 주로 어떤 작업을 수행하는지를 나타내기 위해 동사로 시작합니다.
  - 예시: `get_data`, `calculate_sum`, `process_input`, `update_record`

- **명령형**: 함수명은 명령형으로 작성되어야 합니다.
  - 예시: `print_report`, `save_file`, `load_data`

## 3. 변수명

- **명확한 의미 전달**: 변수명은 변수의 역할이나 저장하는 데이터를 명확하게 표현해야 합니다.
  - 예시: `user_age`, `total_cost`, `is_valid`

- **약어 및 생략 최소화**: 불필요한 약어 사용을 지양하고, 변수명이 명확하고 이해하기 쉽게 작성되어야 합니다.
  - 예시: `num_of_students` 대신 `student_count` 사용

## 4. 특수 접미사 및 접두사

- **상수 변수**: 상수는 모두 대문자로 작성하며, 단어 사이를 밑줄로 구분합니다.
  - 예시: `MAX_VALUE`, `DEFAULT_TIMEOUT`

- **플래그 변수**: Boolean 값을 담는 변수명은 `is_`, `has_`, `can_` 등의 접두사로 시작합니다.
  - 예시: `is_active`, `has_permission`, `can_execute`

## 5. 기타 규칙

- **짧지만 의미 있는 이름**: 불필요하게 긴 이름을 피하고, 의미를 담을 수 있는 최대한 간결한 이름을 사용합니다.
  - 예시: `temp_list` 대신 `temps`, `calculate_total` 대신 `calc_total`

- **클래스와 함수 네이밍 차별화**: 클래스 이름은 PascalCase를 사용하고, 함수와 변수는 snake_case를 사용하여 명확하게 구분합니다.
  - 예시: `DataProcessor` (클래스), `process_data` (함수)

## 6. 변수명 예시

- **숫자 관련 변수**
  - `total_sum`: 전체 합계
  - `average_score`: 평균 점수
  - `max_value`: 최대 값
  - `min_temperature`: 최저 온도
  - `item_count`: 아이템 개수

- **시간/날짜 관련 변수**
  - `current_time`: 현재 시간
  - `start_date`: 시작 날짜
  - `end_time`: 종료 시간
  - `timestamp`: 타임스탬프
  - `elapsed_seconds`: 경과된 초

- **사용자 관련 변수**
  - `user_name`: 사용자 이름
  - `user_id`: 사용자 ID
  - `user_email`: 사용자 이메일
  - `is_authenticated`: 인증 여부
  - `user_profile`: 사용자 프로필

- **상태 플래그 변수**
  - `is_active`: 활성화 여부
  - `has_errors`: 오류 여부
  - `is_completed`: 완료 여부
  - `is_visible`: 가시성 여부
  - `can_execute`: 실행 가능 여부

- **파일 및 경로 관련 변수**
  - `file_path`: 파일 경로
  - `log_file`: 로그 파일
  - `config_directory`: 설정 디렉토리
  - `backup_filename`: 백업 파일 이름
  - `output_folder`: 출력 폴더

## 7. 함수명 예시

- **데이터 처리 관련 함수**
  - `load_data()`: 데이터를 로드하는 함수
  - `save_data()`: 데이터를 저장하는 함수
  - `process_data()`: 데이터를 처리하는 함수
  - `filter_data()`: 데이터를 필터링하는 함수
  - `merge_data()`: 데이터를 병합하는 함수

- **계산 관련 함수**
  - `calculate_total()`: 총합을 계산하는 함수
  - `calculate_discount()`: 할인율을 계산하는 함수
  - `compute_average()`: 평균을 계산하는 함수
  - `sum_numbers()`: 숫자들의 합을 구하는 함수
  - `find_maximum()`: 최대 값을 찾는 함수

- **문자열 처리 함수**
  - `split_string()`: 문자열을 분할하는 함수
  - `join_strings()`: 문자열을 합치는 함수
  - `capitalize_text()`: 텍스트를 대문자로 변환하는 함수
  - `replace_substring()`: 부분 문자열을 대체하는 함수
  - `strip_whitespace()`: 공백을 제거하는 함수

- **조건 검증 함수**
  - `is_valid_user()`: 사용자가 유효한지 확인하는 함수
  - `is_even_number()`: 짝수인지 확인하는 함수
  - `has_permission()`: 권한이 있는지 확인하는 함수
  - `is_prime_number()`: 소수인지 확인하는 함수
  - `can_proceed()`: 진행 가능한지 확인하는 함수

- **파일 작업 함수**
  - `read_file()`: 파일을 읽는 함수
  - `write_file()`: 파일을 쓰는 함수
  - `delete_file()`: 파일을 삭제하는 함수
  - `move_file()`: 파일을 이동하는 함수
  - `copy_file()`: 파일을 복사하는 함수

## 8. API/서비스 함수 예시

- **`add_` 함수 예시 (Create)**
  - `add_user()`: 새로운 사용자를 추가
  - `add_product()`: 새로운 제품을 추가
  - `add_item_to_cart()`: 장바구니에 아이템을 추가
  - `add_employee()`: 직원을 추가
  - `add_comment()`: 댓글을 추가

- **`get_` 함수 예시 (Read)**
  - `get_user_by_id()`: ID로 사용자 정보를 가져옴
  - `get_all_products()`: 모든 제품 목록을 가져옴
  - `get_order_details()`: 주문 세부 정보를 가져옴
  - `get_latest_news()`: 최신 뉴스를 가져옴
  - `get_user_permissions()`: 사용자의 권한 정보를 가져옴

- **`update_` 함수 예시 (Update)**
  - `update_user_profile()`: 사용자 프로필을 업데이트
  - `update_product_info()`: 제품 정보를 업데이트
  - `update_order_status()`: 주문 상태를 업데이트
  - `update_settings()`: 설정을 업데이트
  - `update_password()`: 비밀번호를 업데이트

- **`delete_` 함수 예시 (Delete)**
  - `delete_user()`: 사용자를 삭제
  - `delete_product()`: 제품을 삭제
  - `delete_order()`: 주문을 삭제
  - `delete_comment()`: 댓글을 삭제
  - `delete_file()`: 파일을 삭제

- **추가적인 API/Service 관련 함수 예시**
  - **검색 및 조회**
    - `search_users()`: 사용자 검색
    - `find_product_by_name()`: 제품 이름으로 검색
    - `lookup_order_by_id()`: 주문 ID로 조회
    - `query_database()`: 데이터베이스에서 쿼리 실행
    - `fetch_data_from_api()`: API로부터 데이터 가져오기

  - **인증 및 권한**
    - `authenticate_user()`: 사용자 인증
    - `authorize_action()`: 액션 권한 확인
    - `check_permission()`: 권한 확인
    - `login_user()`: 사용자 로그인
    - `logout_user()`: 사용자 로그아웃

  - **서비스 처리**
    - `process_payment()`: 결제 처리
    - `validate_input()`: 입력값 검증
    - `send_email()`: 이메일 전송
    - `generate_report()`: 보고서 생성
    - `schedule_task()`: 작업 스케줄링
