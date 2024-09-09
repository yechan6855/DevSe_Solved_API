import requests

BASE_URL = "https://solved.ac/api/v3"

def get_user_info(username):
    url = f"{BASE_URL}/search/user" # 엔드포인트
    params = {
        "query": username
    }
    headers = {
        "Accept": "application/json",
        "x-solvedac-language": "ko"  # 한국어로 응답 받기
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200: # 정상 응답
        data = response.json()
        if data["count"] > 0:
            user = data["items"][0]  # 첫 번째 검색 결과 사용
            return {
                "handle": user["handle"], # 유저명
                "bio": user["bio"], # 소개
                "solvedCount": user["solvedCount"], # 푼 문제 수
                "tier": user["tier"], # 티어
                "rating": user["rating"], # 레이팅
                "maxStreak": user["maxStreak"], # 최장 스트릭
                "rank": user["rank"], # 랭킹
            }
        else:
            print(f"유저 '{username}'를 찾을 수 없습니다.")
            return None
    else: # Response 401 응답 오류
        print(f"Error fetching data: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

def get_tier_string(tier):
    tiers = [
        "Unrated",
        "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
        "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
        "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
        "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
        "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
        "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I",
        "Master"
    ]
    return tiers[tier] if 0 <= tier < len(tiers) else "Unknown"

# 테스트
username = input("유저 이름: ")
user_info = get_user_info(username)

if user_info:
    print(f"유저명: {user_info['handle']}")
    print(f"소개: {user_info['bio']}")
    print(f"푼 문제 수: {user_info['solvedCount']}")
    print(f"티어: {get_tier_string(user_info['tier'])}")
    print(f"레이팅: {user_info['rating']}")
    print(f"스트릭: {user_info['maxStreak']}일")
    print(f"랭킹: {user_info['rank']}위")