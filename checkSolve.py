import requests


def check_problem_solved(username, problem_id):
    # solved.ac API 엔드포인트
    api_url = f"https://solved.ac/api/v3/search/problem"

    # API 요청 파라미터
    params = {
        'query': f'@{username} id:{problem_id}',
        'page': 1,
        'sort': 'id',
        'direction': 'asc'
    }

    # API 요청 보내기
    response = requests.get(api_url, params=params)

    # 응답 확인
    if response.status_code == 200:
        data = response.json()
        # 검색 결과가 있으면 문제를 풀었다는 의미
        if data['count'] > 0:
            return True
        else:
            return False
    else:
        print(f"API 요청 실패: {response.status_code}")
        return None


# 사용 예시
username = input("사용자 이름을 입력하세요: ")
problem_id = input("확인할 문제 번호를 입력하세요: ")

result = check_problem_solved(username, problem_id)

if result is True:
    print(f"{username}는 {problem_id}번 문제를 해결했습니다.")
elif result is False:
    print(f"{username}는 {problem_id}번 문제를 해결하지 못했습니다.")
else:
    print("문제 해결 여부를 확인할 수 없습니다.")