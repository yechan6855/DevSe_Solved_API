const fetch = require('node-fetch');

function getTierName(tierNumber) {
    const tierMap = {
        0: "Unrated",
        1: "Bronze V", 2: "Bronze IV", 3: "Bronze III", 4: "Bronze II", 5: "Bronze I",
        6: "Silver V", 7: "Silver IV", 8: "Silver III", 9: "Silver II", 10: "Silver I",
        11: "Gold V", 12: "Gold IV", 13: "Gold III", 14: "Gold II", 15: "Gold I",
        16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
        21: "Diamond V", 22: "Diamond IV", 23: "Diamond III", 24: "Diamond II", 25: "Diamond I",
        26: "Ruby V", 27: "Ruby IV", 28: "Ruby III", 29: "Ruby II", 30: "Ruby I",
        31: "Master"
    };
    return tierMap[tierNumber] || "Unknown";
}

async function getUserTier(handle) {
    const url = `https://solved.ac/api/v3/user/show?handle=${handle}`;

    const headers = {
        "Content-Type": "application/json"
    };

    try {
        const response = await fetch(url, { headers });
        if (response.ok) {
            const userData = await response.json();
            const tierNumber = userData.tier || 0;
            const tierName = getTierName(tierNumber);
            return [tierNumber, tierName];
        } else {
            console.log(`오류: 데이터를 가져올 수 없습니다. 상태 코드: ${response.status}`);
            return [null, null];
        }
    } catch (error) {
        console.error("Error:", error);
        return [null, null];
    }
}

// 메인 실행 부분
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('handle 입력: ', async (handle) => {
    const [tierNumber, tierName] = await getUserTier(handle);

    if (tierNumber !== null) {
        console.log(`${handle}의 티어: ${tierName}`);
    } else {
        console.log("티어 정보를 가져오는 데 실패했습니다.");
    }

    readline.close();
});