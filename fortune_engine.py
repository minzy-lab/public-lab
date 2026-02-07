"""
운세 데이터 생성 엔진
사용자 정보를 받아 일일 맞춤 운세를 생성합니다.
"""

from datetime import datetime
import random
from typing import Dict, List, Any


class FortuneEngine:
    """운세 생성 엔진"""

    # 별자리 정의
    ZODIAC_SIGNS = {
        (3, 21, 4, 19): {"sign": "양자리", "emoji": "♈", "element": "fire"},
        (4, 20, 5, 20): {"sign": "황소자리", "emoji": "♉", "element": "earth"},
        (5, 21, 6, 21): {"sign": "쌍둥이자리", "emoji": "♊", "element": "air"},
        (6, 22, 7, 22): {"sign": "게자리", "emoji": "♋", "element": "water"},
        (7, 23, 8, 22): {"sign": "사자자리", "emoji": "♌", "element": "fire"},
        (8, 23, 9, 22): {"sign": "처녀자리", "emoji": "♍", "element": "earth"},
        (9, 23, 10, 23): {"sign": "천칭자리", "emoji": "♎", "element": "air"},
        (10, 24, 11, 22): {"sign": "전갈자리", "emoji": "♏", "element": "water"},
        (11, 23, 12, 21): {"sign": "사수자리", "emoji": "♐", "element": "fire"},
        (12, 22, 1, 19): {"sign": "염소자리", "emoji": "♑", "element": "earth"},
        (1, 20, 2, 18): {"sign": "물병자리", "emoji": "♒", "element": "air"},
        (2, 19, 3, 20): {"sign": "물고기자리", "emoji": "♓", "element": "water"},
    }

    # MBTI별 특성
    MBTI_TRAITS = {
        "INTJ": {"keyword": "전략가", "strength": "분석적 사고"},
        "INTP": {"keyword": "논리학자", "strength": "창의적 문제해결"},
        "ENTJ": {"keyword": "통솔자", "strength": "리더십"},
        "ENTP": {"keyword": "변론가", "strength": "혁신적 아이디어"},
        "INFJ": {"keyword": "옹호자", "strength": "통찰력"},
        "INFP": {"keyword": "중재자", "strength": "공감 능력"},
        "ENFJ": {"keyword": "선도자", "strength": "사람들과의 소통"},
        "ENFP": {"keyword": "활동가", "strength": "열정과 에너지"},
        "ISTJ": {"keyword": "현실주의자", "strength": "책임감"},
        "ISFJ": {"keyword": "수호자", "strength": "헌신적 배려"},
        "ESTJ": {"keyword": "경영자", "strength": "조직화 능력"},
        "ESFJ": {"keyword": "집정관", "strength": "협력적 태도"},
        "ISTP": {"keyword": "장인", "strength": "실용적 접근"},
        "ISFP": {"keyword": "모험가", "strength": "예술적 감각"},
        "ESTP": {"keyword": "사업가", "strength": "순발력"},
        "ESFP": {"keyword": "연예인", "strength": "사교성"},
    }

    # 운세 메시지 템플릿
    DO_MESSAGES = [
        "중요한 결정을 내리기 좋은 날이에요",
        "새로운 사람과의 만남을 추천해요",
        "창의적인 아이디어를 실행에 옮겨보세요",
        "가까운 사람에게 먼저 연락해보세요",
        "운동이나 건강관리를 시작하기 좋아요",
        "재정 계획을 세워보는 것을 추천해요",
        "배우고 싶었던 것을 시작해보세요",
        "중요한 프레젠테이션이나 미팅을 잡아보세요",
        "오랜만에 친구들과 만나보세요",
        "자기계발에 투자하기 좋은 날이에요",
    ]

    AVOID_MESSAGES = [
        "급한 결정은 미루는 것이 좋겠어요",
        "감정적인 대화는 피하는 것이 좋아요",
        "큰 금액의 지출은 신중하게 고려하세요",
        "새로운 시도보다는 기존 일에 집중하세요",
        "논쟁이나 갈등 상황은 피하세요",
        "과도한 약속은 삼가세요",
        "충동적인 구매는 자제하세요",
        "무리한 일정은 피하고 여유를 가지세요",
        "복잡한 계약이나 서류 작업은 신중하게",
        "타인의 일에 과도하게 개입하지 마세요",
    ]

    LUCKY_COLORS = [
        "파란색", "빨간색", "노란색", "초록색", "보라색",
        "분홍색", "주황색", "흰색", "검은색", "민트색"
    ]

    LUCKY_ITEMS = [
        "노트", "펜", "시계", "향수", "액세서리",
        "책", "이어폰", "텀블러", "가방", "스카프"
    ]

    @classmethod
    def get_zodiac_sign(cls, month: int, day: int) -> Dict[str, str]:
        """생일로 별자리 계산"""
        for (start_m, start_d, end_m, end_d), zodiac in cls.ZODIAC_SIGNS.items():
            if (month == start_m and day >= start_d) or (month == end_m and day <= end_d):
                return zodiac
        return {"sign": "알 수 없음", "emoji": "⭐", "element": "unknown"}

    @classmethod
    def calculate_fortune_score(cls, birth_date: str, today: str) -> float:
        """
        운세 점수 계산 (임시 알고리즘)
        실제로는 사주, 천체 운행 등을 고려해야 함
        """
        # 간단한 시드 기반 랜덤 (같은 날짜면 같은 결과)
        seed = hash(birth_date + today) % 100
        random.seed(seed)
        return round(random.uniform(3.0, 5.0), 1)

    @classmethod
    def calculate_category_scores(cls, birth_date: str, today: str) -> Dict[str, float]:
        """카테고리별 운세 점수"""
        seed = hash(birth_date + today)
        random.seed(seed)

        categories = ["love", "money", "health", "work"]
        scores = {}

        for i, category in enumerate(categories):
            # 각 카테고리마다 다른 시드 사용
            random.seed(seed + i)
            scores[category] = round(random.uniform(2.5, 5.0), 1)

        return scores

    @classmethod
    def generate_daily_fortune(cls, name: str, birth_date: str, mbti: str = None) -> Dict[str, Any]:
        """
        일일 맞춤 운세 생성

        Args:
            name: 사용자 이름
            birth_date: 생년월일 (YYYY-MM-DD)
            mbti: MBTI 유형 (선택)

        Returns:
            운세 데이터 딕셔너리
        """
        today = datetime.now().strftime("%Y-%m-%d")
        today_display = datetime.now().strftime("%Y년 %m월 %d일")

        # 생년월일 파싱
        try:
            birth = datetime.strptime(birth_date, "%Y-%m-%d")
            month, day = birth.month, birth.day
        except ValueError:
            month, day = 1, 1

        # 별자리 계산
        zodiac = cls.get_zodiac_sign(month, day)

        # 종합 운세 점수
        overall_score = cls.calculate_fortune_score(birth_date, today)

        # 카테고리별 점수
        category_scores = cls.calculate_category_scores(birth_date, today)

        # 오늘 하면 좋은 일 3가지
        seed = hash(birth_date + today + "do")
        random.seed(seed)
        do_list = random.sample(cls.DO_MESSAGES, 3)

        # 오늘 피해야 할 일 3가지
        seed = hash(birth_date + today + "avoid")
        random.seed(seed)
        avoid_list = random.sample(cls.AVOID_MESSAGES, 3)

        # 행운 아이템
        seed = hash(birth_date + today + "lucky")
        random.seed(seed)
        lucky_color = random.choice(cls.LUCKY_COLORS)
        lucky_item = random.choice(cls.LUCKY_ITEMS)
        lucky_numbers = sorted(random.sample(range(1, 46), 6))

        # MBTI 조합 메시지
        mbti_message = ""
        if mbti and mbti.upper() in cls.MBTI_TRAITS:
            trait = cls.MBTI_TRAITS[mbti.upper()]
            mbti_message = f"{mbti.upper()} {trait['keyword']}인 당신은 {trait['strength']}이/가 빛나는 날이에요!"

        # 운세 데이터 구성
        fortune_data = {
            "user": {
                "name": name,
                "birth_date": birth_date,
                "mbti": mbti.upper() if mbti else None,
                "zodiac": zodiac
            },
            "date": {
                "today": today,
                "display": today_display
            },
            "scores": {
                "overall": overall_score,
                "love": category_scores["love"],
                "money": category_scores["money"],
                "health": category_scores["health"],
                "work": category_scores["work"]
            },
            "messages": {
                "mbti": mbti_message,
                "summary": f"오늘은 전체적으로 {'좋은' if overall_score >= 4.0 else '괜찮은'} 날이에요!"
            },
            "actions": {
                "do": do_list,
                "avoid": avoid_list
            },
            "lucky": {
                "color": lucky_color,
                "item": lucky_item,
                "numbers": lucky_numbers
            }
        }

        return fortune_data


# 테스트용 코드
if __name__ == "__main__":
    # 샘플 운세 생성
    sample_fortune = FortuneEngine.generate_daily_fortune(
        name="지은",
        birth_date="1995-03-15",
        mbti="ENFP"
    )

    import json
    print(json.dumps(sample_fortune, ensure_ascii=False, indent=2))
