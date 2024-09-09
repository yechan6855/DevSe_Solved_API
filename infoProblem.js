const fetch = require('node-fetch');

// solved.ac API의 기본 URL
const BASE_URL = "https://solved.ac/api/v3";

function getLevelString(level) {
    // 난이도 숫자를 문자열로 변환하는 함수
    const levels = [
        "Unrated", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
        "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
        "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
        "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
        "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
        "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I", "Master"
    ];
    // 주어진 level이 유효한 범위 내에 있으면 해당 문자열을, 아니면 "Unknown" 반환
    return (level >= 0 && level < levels.length) ? levels[level] : "Unknown";
}

async function getProblemInfo(problemId) {
    // 문제 정보를 가져오는 API 엔드포인트 URL
    const url = `${BASE_URL}/problem/show`;

    // API 요청 파라미터
    const params = new URLSearchParams({ problemId });

    // API 요청 옵션
    const options = {
        headers: { "Accept": "application/json" }
    };

    try {
        // GET 요청 보내기
        const response = await fetch(`${url}?${params}`, options);

        if (response.ok) {
            // 요청 성공 시 JSON 데이터 파싱
            const data = await response.json();

            // 필요한 정보만 추출하여 객체로 반환
            return {
                problemId: data.problemId,
                titleKo: data.titleKo,
                level: getLevelString(data.level),
                acceptedUserCount: data.acceptedUserCount,
                averageTries: data.averageTries,
                tags: data.tags.map(tag => tag.key)
            };
        } else {
            // 요청 실패 시 오류 메시지 출력
            console.error(`Error fetching data: ${response.status}`);
            console.error(`Response content: ${await response.text()}`);
            return null;
        }
    } catch (error) {
        console.error("An error occurred:", error);
        return null;
    }
}

// readline 모듈을 사용하여 사용자 입력 받기
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// 테스트 코드
readline.question('문제 번호: ', async (problemId) => {
    const problemInfo = await getProblemInfo(problemId);
    if (problemInfo) {
        // 문제 정보 출력
        console.log(`문제 번호: ${problemInfo.problemId}`);
        console.log(`문제 제목: ${problemInfo.titleKo}`);
        console.log(`난이도: ${problemInfo.level}`);
        console.log(`맞춘 사람 수: ${problemInfo.acceptedUserCount}`);
        console.log(`평균 시도 횟수: ${problemInfo.averageTries}`);
        console.log(`태그: ${problemInfo.tags.join(', ')}`);
    }
    readline.close();
});