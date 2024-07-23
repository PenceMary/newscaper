import random

# 定义卦象数据库
gua_database = {
    1: {
        'name': '乾卦',
        'sequence': '☰',
        'yao': '－－－－－－',
        'meaning': '象征纯阳，代表天、刚健、积极向上。'
    },
    2: {
        'name': '坤卦',
        'sequence': '☷',
        'yao': '－－ －－ －－',
        'meaning': '象征纯阴，代表地、柔顺、包容。'
    },
    51: {
        'name': '震卦',
        'sequence': '☳',
        'yao': '－－ －－ －－ － －－',
        'meaning': '象征雷动，代表动荡、变化、开拓。'
    }
}

# 随机生成1到64之间的数值
random_number = random.randint(1, 64)

# 尝试从数据库中获取对应的卦象
gua = gua_database.get(random_number)

if gua:
    print(f"卦名: {gua['name']}")
    print(f"卦象: {gua['sequence']}")
    print(f"爻象: {gua['yao']}")
    print(f"含义: {gua['meaning']}")
else:
    print("未获取到对应的卦象。")