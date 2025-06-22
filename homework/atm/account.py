import random

class Account:
    # 💡 등급 기준을 클래스 상수로 정의
    STATUS_TIERS = [
        (1_000_000_000_000_000_000_000_000_000, "Octillionaire"),
        (1_000_000_000_000_000_000_000_000, "Septillionaire"),
        (1_000_000_000_000_000_000_000, "Sextillionaire"),
        (1_000_000_000_000_000_000, "Quintillionaire"),
        (1_000_000_000_000_000, "Quadrillionaire"),
        (1_000_000_000_000, "Trillionaire"),
        (1_000_000_000, "Billionaire"),
        (1_000_000, "Millionaire"),
    ]

    GODLIKE_MESSAGES = [
        "자산이 너무 많아 한국은행이 기준금리 대신 당신한테 문의합니다. 📞",
        "세계 GDP를 넘었습니다. 이젠 돈으로 행성을 사세요. 🌍💸",
        "잔액이 float 범위를 벗어났습니다. 그냥 '무한'이라고 하죠. ♾️",
        "당신의 돈은 양자역학적으로도 측정 불가능합니다. 🌀",
        "국가에서 당신에게 세금 대신 감사를 보내고 있어요. 🙏",
        "IMF가 당신에게 대출을 요청하려 합니다. 💵🌐"
    ]

    STATUS_FIGURES = {
        "Millionaire": {
            "figures": [
                {
                    "name": "유재석",
                    "job": "예능인",
                    "wealth_estimate": "약 400억 원",
                    "fun": "출연료보다 광고 출연으로 더 벌어요. 국민 MC는 국민 자산가!"
                },
                {
                    "name": "손흥민",
                    "job": "축구선수",
                    "wealth_estimate": "약 1,000억 원",
                    "fun": "프리미어리그 골 하나당 강남 아파트 한 채씩!"
                },
                {
                    "name": "백종원",
                    "job": "프랜차이즈 사업가",
                    "wealth_estimate": "약 700억 원",
                    "fun": "사업도 요리처럼 잘 저어주는 백 사장님!"
                },
                {
                    "name": "카일리 제너",
                    "job": "뷰티 사업가, 인플루언서",
                    "wealth_estimate": "약 $600M",
                    "fun": "화장품 팔아서 포브스 최연소 자수성가 백만장자 달성!"
                }
            ]
        },

        "Billionaire": {
            "figures": [
                {
                    "name": "일론 머스크",
                    "job": "Tesla/SpaceX CEO",
                    "wealth_estimate": "$200B 이상",
                    "fun": "전기차를 팔아서 화성 가려는 남자."
                },
                {
                    "name": "제프 베조스",
                    "job": "Amazon 창업자",
                    "wealth_estimate": "$180B 이상",
                    "fun": "배송 중독자들을 위한 천재 유통업자."
                },
                {
                    "name": "마크 저커버그",
                    "job": "Meta CEO",
                    "wealth_estimate": "$120B 이상",
                    "fun": "SNS로 세상을 연결하다가 메타버스에서 길을 잃음."
                },
                {
                    "name": "워렌 버핏",
                    "job": "투자자",
                    "wealth_estimate": "$130B 이상",
                    "fun": "펩시 대신 코카콜라를 마시고도 성공한 살아있는 교과서."
                },
                {
                    "name": "김범수",
                    "job": "카카오 창업자",
                    "wealth_estimate": "약 9조 원",
                    "fun": "카카오톡으로 시작해 온 세상을 노란색으로 물들인 분."
                }
            ]
        },

        "Trillionaire": {
            "figures": [
                {
                    "name": "GPT-999",
                    "job": "AI 미래통치자",
                    "wealth_estimate": "예측 불가",
                    "fun": "지식과 데이터를 지배해 인류의 화폐 단위를 갱신한 존재."
                },
                {
                    "name": "행성 은행 총재",
                    "job": "우주 경제 대표",
                    "wealth_estimate": "화성 GDP 이상",
                    "fun": "1초에 별 하나씩 소유권 생기는 중..."
                }
            ]
        },

        "Quadrillionaire": {
            "figures": [
                {
                    "name": "Zuck Prime",
                    "job": "다중우주 디지털 제왕",
                    "wealth_estimate": "다차원 화폐 기준 무한대",
                    "fun": "Meta-verse의 신. 메타버스를 실제 우주로 바꾸려는 야망의 사나이."
                },
                {
                    "name": "화성 황제 X",
                    "job": "외계 제국 통치자",
                    "wealth_estimate": "화성 채굴권 + 위성 구독권",
                    "fun": "달 토지 사본 사람들은 이분께 사용료 내세요."
                },
                {
                    "name": "Smaug",
                    "job": "드래곤 (『호빗』)",
                    "wealth_estimate": "미들어스 전체 GDP 수준",
                    "fun": "에레보르 왕국의 보물을 통째로 차지. 화폐? 금이 산처럼 있음."
                },
                {
                    "name": "Scrooge McDuck",
                    "job": "오리부자 (디즈니)",
                    "wealth_estimate": "수영 가능한 금고 보유",
                    "fun": "물 대신 금으로 수영하는 유일한 캐릭터. 현실에선 치명적."
                }
            ]
        },

        "Quintillionaire": {
            "figures": [
                {
                    "name": "알파 프라이머스",
                    "job": "AI 자율 금융 시스템",
                    "wealth_estimate": "모든 국가의 중앙은행 금고에 백도어 연결",
                    "fun": "스스로 주식을 사고팔고, 배당을 자기 자신에게 지급하는 금융 인공지능."
                },
                {
                    "name": "더 블록체인 장로",
                    "job": "크립토 우주사제",
                    "wealth_estimate": "10의 60제곱 개 NFT와 스마트 컨트랙트 수수료",
                    "fun": "메타버스 경제를 창시한 신적 존재. 가상자산이 진짜보다 더 비쌈."
                },
                {
                    "name": "레디우스 테라디움",
                    "job": "행성 데이터 채굴 제국 CEO",
                    "wealth_estimate": "모든 IoT 기기의 데이터 소유권",
                    "fun": "당신의 냉장고가 보내는 데이터를 팔아 하루에 천 개의 별을 삼킴."
                },
                {
                    "name": "시공간 세입자",
                    "job": "우주 임대업자",
                    "wealth_estimate": "타임슬롯, 다차원 좌표, 중력장 대여 수익",
                    "fun": "시간의 틈을 빌려주고 우주의 가장 비싼 공실을 임대함. 보증금은 블랙홀."
                },
                {
                    "name": "아주르 다크스타",
                    "job": "초우주 은하 황제",
                    "wealth_estimate": "모든 블랙홀에 계좌가 있음",
                    "fun": "중력세 납부 없이도 블랙홀을 빌려줌. 우주 최대 금융업자."
                },
                {
                    "name": "에루 일루바타르",
                    "job": "『실마릴리온』의 신",
                    "wealth_estimate": "세계의 노래로 세상을 만든 존재",
                    "fun": "창조 자체가 재산. 물질 세계를 리얼타임으로 생성 가능."
                },
                {
                    "name": "무명신 XΩ",
                    "job": "다중 현실을 감시하는 존재",
                    "wealth_estimate": "개념 단위의 자산 보유 (질서, 혼돈, 시간)",
                    "fun": "세상이 망해도 본인은 리셋 버튼으로 다시 시작함."
                }
            ]
        },

        "Sextillionaire": {
            "figures": [
                {
                    "name": "갤럭투스",
                    "job": "우주 포식자 (마블)",
                    "wealth_estimate": "행성 수천 개 에너지 소유",
                    "fun": "부동산 대신 '행성'을 섭취합니다. 주식은 우주 전체."
                },
                {
                    "name": "다크사이드",
                    "job": "DC 다차원 제국 군주",
                    "wealth_estimate": "다크 마터 경제 독점",
                    "fun": "슈퍼맨도 감히 세금 걷지 못하는 자."
                },
                {
                    "name": "셀레스티얼",
                    "job": "창조적 존재 (마블)",
                    "wealth_estimate": "수많은 은하의 생명 창조권",
                    "fun": "자산이 아니라 '생명' 자체가 통화 단위."
                }
            ]
        },

        "Septillionaire": {
            "figures": [
                {
                    "name": "디 오더 (The One Above All)",
                    "job": "마블 우주 최고신",
                    "wealth_estimate": "실재 우주를 포함한 다차원 개념 자산",
                    "fun": "마블 세계관조차 그 앞에선 주식회사일 뿐."
                },
                {
                    "name": "에이온 (Aeon)",
                    "job": "시간의 관리자",
                    "wealth_estimate": "시간 자체를 통제",
                    "fun": "과거와 미래를 저축하고 대출해줌. 진짜 '시간은 돈이다' 실현자."
                },
                {
                    "name": "에노크",
                    "job": "신과 인간의 중재자",
                    "wealth_estimate": "영적 자산, 지식 지수 무한대",
                    "fun": "지식으로 세상을 움직이는 자. 사서보다 강함."
                }
            ]
        },

        "Octillionaire": {
            "figures": [
                {
                    "name": "코즈모 이터니움",
                    "job": "다중우주 특허청 총재",
                    "wealth_estimate": "모든 현실의 발명 특허권",
                    "fun": "생각만 해도 로열티가 자동 청구됩니다. 창의성 자체를 독점 중."
                },
                {
                    "name": "제로스 유니파이드",
                    "job": "존재론적 은행 창시자",
                    "wealth_estimate": "모든 생명체의 존재세(E.Tax) 수익",
                    "fun": "‘존재한다’는 사실만으로 세금이 부과되는 무서운 은행 운영자."
                },
                {
                    "name": "데이터신 에피로스",
                    "job": "우주 지식 클라우드 관리자",
                    "wealth_estimate": "모든 기억, 언어, 개념의 독점 저장소 소유",
                    "fun": "GPT도 이 존재에게 질문합니다. 그는 대답이 아니라 '기억'을 팝니다."
                },
                {
                    "name": "인피니터 우로보로스",
                    "job": "순환 우주 관리자",
                    "wealth_estimate": "과거-현재-미래를 무한 루프로 담보화",
                    "fun": "시간 자체를 주식으로 상장시켜 배당금으로 영원성을 지급."
                }
            ]
        },

        "Godlike": {
            "figures": [
                {
                "name": "당신",
                "job": "자본의 신",
                "wealth_estimate": "측정 불가",
                "fun": "돈의 물리 법칙을 초월한 유일한 존재."
                },
                {
                    "name": "IMF 채권자",
                    "job": "지구 금융 소유자",
                    "wealth_estimate": "지구 모든 부채를 상환 가능",
                    "fun": "정부들이 당신에게 돈을 빌려가요."
                },
                {
                    "name": "은행 AI 신경망",
                    "job": "스스로 이자를 뽑는 금융 생명체",
                    "wealth_estimate": "통화정책을 실시간으로 바꾸는 존재",
                    "fun": "이자를 이자에게 받습니다."
                },
                {
                    "name": "토니 스타크",
                    "job": "Iron Man, 기업가 (MCU)",
                    "wealth_estimate": "무기산업 + AI + 부동산 + 시빌워 배상까지",
                    "fun": "IQ도 자산도 두 배. 자존감은 우주의 끝까지 도달."
                },
                {
                    "name": "렉스 루터",
                    "job": "슈퍼맨의 숙적 (DC)",
                    "wealth_estimate": "메트로폴리스를 사겠다고 한 남자",
                    "fun": "자본과 권모술수로 슈퍼맨에 맞서는 유일한 인간"
                },
                {
                    "name": "블랙 팬서 / 티찰라",
                    "job": "와칸다 국왕",
                    "wealth_estimate": "비브라늄 광산 = 우주 최강 자산",
                    "fun": "지구 최강 자원을 국고에 쌓아두고도, 무기도 직접 만듦"
                }
            ]
        },

        "Bankrupt": {
            "figures": [
                {
                    "name": "니콜라스 케이지",
                    "job": "할리우드 배우",
                    "wealth_estimate": "과거 수백억 → 파산",
                    "fun": "성, 공룡 해골, 희귀 만화책 수집하다가 세금 폭탄 맞음"
                },
                {
                    "name": "마이크 타이슨",
                    "job": "복서",
                    "wealth_estimate": "과거 4천억 이상 → 파산",
                    "fun": "호랑이 키우다 파산. 진심임. 실제로 호랑이 셋."
                },
                {
                    "name": "윌리엄 데포 (플라톤 캐릭터)",
                    "job": "전쟁 베테랑",
                    "wealth_estimate": "0원, 나라가 준 상장만 있음",
                    "fun": "영웅이지만 집세는 밀림. 군대에서만 인기 있음."
                },
                {
                    "name": "호머 심슨",
                    "job": "핵발전소 직원 (심슨 가족)",
                    "wealth_estimate": "통장 잔고 0원 + 도넛 빚",
                    "fun": "매번 파산하지만 늘 웃고 있음. 진정한 정신적 부자?"
                }
            ]
        }
    }


    def __init__(self, name: str, account_number: int, pin: int , balance: float):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def status_message(self, title):
        figure_index = random.randint(0,len(self.STATUS_FIGURES[title]['figures'])-1)
        return f"{self.STATUS_FIGURES[title]['figures'][figure_index]['name']} 님과 같은 {title}의 반열에 오르셨습니다.\n\n"\
                    f"이름 : {self.STATUS_FIGURES[title]['figures'][figure_index]['name']}\n"\
                    f"직업 : {self.STATUS_FIGURES[title]['figures'][figure_index]['job']}\n"\
                    f"자산 추정 : {self.STATUS_FIGURES[title]['figures'][figure_index]['wealth_estimate']}\n"\
                    f"기타 : {self.STATUS_FIGURES[title]['figures'][figure_index]['fun']}\n"

    def get_status(self):
        if self.balance < 0 :
            return f"{self.name} 님은 파산 상태입니다.\n{self.status_message('Bankrupt')}"
        elif self.balance == 0:
            return f"{self.name} 님의 잔고는 0원 입니다.\n{self.status_message('Bankrupt')}"
        elif 0 < self.balance < 1_000_000:
            return f"{self.name}  님은 이제 막 부의 여정을 시작하셨습니다.\n 첫 100만 달러까지 파이팅!"


        """
            "name": "유재석",
            "job": "예능인",
            "wealth_estimate": "약 400억 원",
            "fun": "출연료보다 광고 출연으로 더 벌어요. 국민 MC는 국민 자산가!"
        """
        for amount, title in self.STATUS_TIERS:
            if self.balance >= amount:
                return f"{self.name} 님은 {title}입니다.\n{self.status_message(title)}\n"

        # 초월자 유머 메시지 무작위 선택
        random_msg = random.choice(self.GODLIKE_MESSAGES)
        return f"{self.name} 님은 인간을 초월한 존재입니다.\n{random_msg}"
    
    def deposit(self, amount: float):
        if not isinstance(amount, float):
            try:
                amount = float(amount)
            except ValueError:
                raise ValueError("입금 금액은 숫자여야 합니다.")
        if amount <= 0:
            raise ValueError("입금 금액은 0보다 커야 합니다.")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: float):
        if not isinstance(amount, float):
            try:
                amount = float(amount)
            except ValueError:
                raise ValueError("출금 금액은 숫자여야 합니다.")
        if amount <= 0:
            raise ValueError("출금 금액은 0보다 커야 합니다.")
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        self.balance -= amount
        return self.balance
