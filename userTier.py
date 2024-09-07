import requests

def get_tier_name(tier_number):
    # 티어 번호에 해당하는 티어 이름을 반환하는 함수
    tier_map = {
        0: "Unrated",
        1: "Bronze V", 2: "Bronze IV", 3: "Bronze III", 4: "Bronze II", 5: "Bronze I",
        6: "Silver V", 7: "Silver IV", 8: "Silver III", 9: "Silver II", 10: "Silver I",
        11: "Gold V", 12: "Gold IV", 13: "Gold III", 14: "Gold II", 15: "Gold I",
        16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
        21: "Diamond V", 22: "Diamond IV", 23: "Diamond III", 24: "Diamond II", 25: "Diamond I",
        26: "Ruby V", 27: "Ruby IV", 28: "Ruby III", 29: "Ruby II", 30: "Ruby I",
        31: "Master"
    }
    return tier_map.get(tier_number, "Unknown")


def get_user_tier(handle):
    # solved.ac API를 사용하여 사용자의 티어 정보를 가져오는 함수
    url = f"https://solved.ac/api/v3/user/show?handle={handle}"

    headers = {
        "Content-Type": "application/json"
    }

    # API 요청 보내기
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # 요청 성공 시 사용자 데이터에서 티어 정보 추출
        user_data = response.json()
        tier_number = user_data.get("tier", 0)
        tier_name = get_tier_name(tier_number)
        return tier_number, tier_name
    else:
        # 요청 실패 시 오류 메시지 출력
        print(f"오류: 데이터를 가져올 수 없습니다. 상태 코드: {response.status_code}")
        return None, None


# 메인 실행 부분
if __name__ == "__main__":
    # 조회할 사용자의 handle 설정
    handle = input("handle 입력: ")

    # 사용자의 티어 정보 가져오기
    tier_number, tier_name = get_user_tier(handle)

    if tier_number is not None:
        # 티어 정보 출력
        print(f"{handle}의 티어: {tier_name}")
    else:
        print("티어 정보를 가져오는 데 실패했습니다.")