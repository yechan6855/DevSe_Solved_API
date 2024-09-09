const fetch = require('node-fetch');

const BASE_URL = "https://solved.ac/api/v3";

async function getUserInfo(username) {
    const url = `${BASE_URL}/search/user`;
    const params = new URLSearchParams({ query: username });

    const options = {
        headers: {
            "Accept": "application/json",
            "x-solvedac-language": "ko"
        }
    };

    try {
        const response = await fetch(`${url}?${params}`, options);

        if (response.ok) {
            const data = await response.json();
            if (data.count > 0) {
                const user = data.items[0];
                return {
                    handle: user.handle,
                    bio: user.bio,
                    solvedCount: user.solvedCount,
                    tier: user.tier,
                    rating: user.rating,
                    maxStreak: user.maxStreak,
                    rank: user.rank,
                };
            } else {
                console.log(`유저 '${username}'를 찾을 수 없습니다.`);
                return null;
            }
        } else {
            console.error(`Error fetching data: ${response.status}`);
            console.error(`Response content: ${await response.text()}`);
            return null;
        }
    } catch (error) {
        console.error("An error occurred:", error);
        return null;
    }
}

function getTierString(tier) {
    const tiers = [
        "Unrated", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
        "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
        "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
        "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
        "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
        "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I", "Master"
    ];
    return (tier >= 0 && tier < tiers.length) ? tiers[tier] : "Unknown";
}

// readline 모듈을 사용하여 사용자 입력 받기
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// 테스트
readline.question('유저 이름: ', async (username) => {
    const userInfo = await getUserInfo(username);
    if (userInfo) {
        console.log(`유저명: ${userInfo.handle}`);
        console.log(`소개: ${userInfo.bio}`);
        console.log(`푼 문제 수: ${userInfo.solvedCount}`);
        console.log(`티어: ${getTierString(userInfo.tier)}`);
        console.log(`레이팅: ${userInfo.rating}`);
        console.log(`스트릭: ${userInfo.maxStreak}일`);
        console.log(`랭킹: ${userInfo.rank}위`);
    }
    readline.close();
});