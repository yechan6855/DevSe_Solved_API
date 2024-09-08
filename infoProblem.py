import requests

# solved.ac API의 기본 URL
BASE_URL = "https://solved.ac/api/v3"

def get_level_string(level):
    # 난이도 숫자를 문자열로 변환하는 함수
    levels = [
        "Unrated",
        "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
        "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
        "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
        "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
        "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
        "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I",
        "Master"
    ]
    # 주어진 level이 유효한 범위 내에 있으면 해당 문자열을, 아니면 "Unknown" 반환
    return levels[level] if 0 <= level < len(levels) else "Unknown"

def get_problem_info(problem_id):
    # 문제 정보를 가져오는 API 엔드포인트 URL
    url = f"{BASE_URL}/problem/show"
    # API 요청 파라미터
    params = {"problemId": problem_id}
    # API 요청 헤더
    headers = {"Accept": "application/json"}

    # GET 요청 보내기
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        # 요청 성공 시 JSON 데이터 파싱
        data = response.json()
        # 필요한 정보만 추출하여 딕셔너리로 반환
        return {
            "problemId": data["problemId"],
            "titleKo": data["titleKo"],
            "level": get_level_string(data["level"]),
            "acceptedUserCount": data["acceptedUserCount"],
            "averageTries": data["averageTries"],
            "tags": [tag["key"] for tag in data["tags"]]
        }
    else:
        # 요청 실패 시 오류 메시지 출력
        print(f"Error fetching data: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

# 테스트 코드
problem_id = input("문제 번호: ")
problem_info = get_problem_info(problem_id)

if problem_info:
    # 문제 정보 출력
    print(f"문제 번호: {problem_info['problemId']}")
    print(f"문제 제목: {problem_info['titleKo']}")
    print(f"난이도: {problem_info['level']}")
    print(f"맞춘 사람 수: {problem_info['acceptedUserCount']}")
    print(f"평균 시도 횟수: {problem_info['averageTries']}")
    print(f"태그: {', '.join(problem_info['tags'])}")