const fetch = require('node-fetch');

async function checkProblemSolved(username, problemId) {
    // solved.ac API 엔드포인트
    const apiUrl = "https://solved.ac/api/v3/search/problem";

    // API 요청 파라미터
    const params = new URLSearchParams({
        'query': `@${username} id:${problemId}`,
        'page': 1,
        'sort': 'id',
        'direction': 'asc'
    });

    try {
        // API 요청 보내기
        const response = await fetch(`${apiUrl}?${params}`);

        // 응답 확인
        if (response.ok) {
            const data = await response.json();
            // 검색 결과가 있으면 문제를 풀었다는 의미
            return data.count > 0;
        } else {
            console.log(`API 요청 실패: ${response.status}`);
            return null;
        }
    } catch (error) {
        console.error("오류 발생:", error);
        return null;
    }
}

// readline 모듈을 사용하여 사용자 입력 받기
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// 사용 예시
readline.question('사용자 이름을 입력하세요: ', (username) => {
    readline.question('확인할 문제 번호를 입력하세요: ', async (problemId) => {
        const result = await checkProblemSolved(username, problemId);

        if (result === true) {
            console.log(`${username}는 ${problemId}번 문제를 해결했습니다.`);
        } else if (result === false) {
            console.log(`${username}는 ${problemId}번 문제를 해결하지 못했습니다.`);
        } else {
            console.log("문제 해결 여부를 확인할 수 없습니다.");
        }

        readline.close();
    });
});