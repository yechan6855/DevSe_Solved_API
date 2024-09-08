import requests

BASE_URL = "https://solved.ac/api/v3"

def get_level_string(level):
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
    return levels[level] if 0 <= level < len(levels) else "Unknown"

def get_problem_info(problem_id):
    url = f"{BASE_URL}/problem/show"
    params = {"problemId": problem_id}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "problemId": data["problemId"],
            "titleKo": data["titleKo"],
            "level": get_level_string(data["level"]),
            "acceptedUserCount": data["acceptedUserCount"],
            "averageTries": data["averageTries"],
            "tags": [tag["key"] for tag in data["tags"]]
        }
    else:
        print(f"Error fetching data: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

# 테스트
problem_id = input("문제 번호: ")
problem_info = get_problem_info(problem_id)

if problem_info:
    print(f"문제 번호: {problem_info['problemId']}")
    print(f"문제 제목: {problem_info['titleKo']}")
    print(f"난이도: {problem_info['level']}")
    print(f"맞춘 사람 수: {problem_info['acceptedUserCount']}")
    print(f"평균 시도 횟수: {problem_info['averageTries']}")
    print(f"태그: {', '.join(problem_info['tags'])}")