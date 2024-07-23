import random

# 定义六十四卦的数据库
gua_database = {
    1: {'name': '乾卦', 'sequence': '☰', 'yao': '－－－－－－', 'meaning': '象征纯阳，代表天、刚健、积极向上。'},
    2: {'name': '坤卦', 'sequence': '☷', 'yao': '－－ －－ －－', 'meaning': '象征纯阴，代表地、柔顺、包容。'},
    3: {'name': '屯卦', 'sequence': '☳☵', 'yao': '－－ －－ －', 'meaning': '象征初生、艰难。'},
    4: {'name': '蒙卦', 'sequence': '☷☳', 'yao': '－－ －－ －－ －', 'meaning': '象征启蒙、成长。'},
    5: {'name': '需卦', 'sequence': '☰☵', 'yao': '－－－－－－ －', 'meaning': '象征等待、积蓄。'},
    6: {'name': '讼卦', 'sequence': '☵☰', 'yao': '－－ －－ －－', 'meaning': '象征争讼、争论。'},
    7: {'name': '师卦', 'sequence': '☷☷', 'yao': '－－ －－ －－', 'meaning': '象征军队、组织。'},
    8: {'name': '比卦', 'sequence': '☷☵', 'yao': '－－ －－ －', 'meaning': '象征合作、联合。'},
    9: {'name': '小畜卦', 'sequence': '☰☴', 'yao': '－－－－－－', 'meaning': '象征积蓄、小有收获。'},
    10: {'name': '履卦', 'sequence': '☱☰', 'yao': '－－－－－－ －－', 'meaning': '象征行走、步伐。'},
    11: {'name': '泰卦', 'sequence': '☷☰', 'yao': '－－ －－ －－ －', 'meaning': '象征顺畅、和谐。'},
    12: {'name': '否卦', 'sequence': '☰☷', 'yao': '－－－－－－ －－', 'meaning': '象征闭塞、不通。'},
    13: {'name': '同人卦', 'sequence': '☰☲', 'yao': '－－－－－－ －－', 'meaning': '象征合作、团结。'},
    14: {'name': '大有卦', 'sequence': '☲☰', 'yao': '－－ －－ －－', 'meaning': '象征拥有、富足。'},
    15: {'name': '谦卦', 'sequence': '☷☶', 'yao': '－－ －－ －－', 'meaning': '象征谦虚、退让。'},
    16: {'name': '豫卦', 'sequence': '☷☳', 'yao': '－－ －－ －－ －', 'meaning': '象征欢乐、愉快。'},
    17: {'name': '随卦', 'sequence': '☱☷', 'yao': '－－ －－ －－ －', 'meaning': '象征随从、依从。'},
    18: {'name': '蛊卦', 'sequence': '☶☷', 'yao': '－－ －－ －－', 'meaning': '象征纠正、整顿。'},
    19: {'name': '临卦', 'sequence': '☱☷', 'yao': '－－ －－ －－ －', 'meaning': '象征临近、接近。'},
    20: {'name': '观卦', 'sequence': '☷☴', 'yao': '－－ －－ －－ －', 'meaning': '象征观察、审视。'},
    21: {'name': '噬嗑卦', 'sequence': '☲☳', 'yao': '－－ －－ －－', 'meaning': '象征惩罚、制约。'},
    22: {'name': '贲卦', 'sequence': '☳☲', 'yao': '－－ －－ －－ －', 'meaning': '象征装饰、美丽。'},
    23: {'name': '剥卦', 'sequence': '☶☷', 'yao': '－－ －－ －－', 'meaning': '象征剥落、衰败。'},
    24: {'name': '复卦', 'sequence': '☷☳', 'yao': '－－ －－ －－ －', 'meaning': '象征复归、返回。'},
    25: {'name': '无妄卦', 'sequence': '☰☶', 'yao': '－－－－－－', 'meaning': '象征无妄、自然。'},
    26: {'name': '大畜卦', 'sequence': '☶☰', 'yao': '－－ －－ －－', 'meaning': '象征大有积蓄。'},
    27: {'name': '颐卦', 'sequence': '☷☶', 'yao': '－－ －－ －－', 'meaning': '象征养育、口实。'},
    28: {'name': '大过卦', 'sequence': '☱☷', 'yao': '－－ －－ －－ －', 'meaning': '象征超越、过度。'},
    29: {'name': '坎卦', 'sequence': '☵☵', 'yao': '－－ －－ －－', 'meaning': '象征险陷、坎坷。'},
    30: {'name': '离卦', 'sequence': '☲☲', 'yao': '－－ －－ －－', 'meaning': '象征光明、附着。'},
    31: {'name': '咸卦', 'sequence': '☱☶', 'yao': '－－ －－ －－', 'meaning': '象征感应、感应。'},
    32: {'name': '恒卦', 'sequence': '☴☴', 'yao': '－－ －－ －－ －', 'meaning': '象征恒久、稳定。'},
    33: {'name': '遯卦', 'sequence': '☷☱', 'yao': '－－ －－ －－ －', 'meaning': '象征退避、隐退。'},
    34: {'name': '大壮卦', 'sequence': '☷☰', 'yao': '－－ －－ －－', 'meaning': '象征壮大、强盛。'},
    35: {'name': '晋卦', 'sequence': '☲☷', 'yao': '－－ －－ －－ －', 'meaning': '象征前进、进步。'},
    36: {'name': '明夷卦', 'sequence': '☷☲', 'yao': '－－ －－ －－', 'meaning': '象征光明受损。'},
    37: {'name': '家人卦', 'sequence': '☳☷', 'yao': '－－ －－ －－ －', 'meaning': '象征家庭、家人。'},
    38: {'name': '睽卦', 'sequence': '☷☳', 'yao': '－－ －－ －－ －', 'meaning': '象征分离、对立。'},
    39: {'name': '蹇卦', 'sequence': '☵☷', 'yao': '－－ －－ －－ －', 'meaning': '象征艰难、困顿。'},
    40: {'name': '解卦', 'sequence': '☷☵', 'yao': '－－ －－ －－ －', 'meaning': '象征解除、解脱。'},
    41: {'name': '损卦', 'sequence': '☷☴', 'yao': '－－ －－ －－ －', 'meaning': '象征减少、损耗。'},
    42: {'name': '益卦', 'sequence': '☴☷', 'yao': '－－ －－ －－ －', 'meaning': '象征增加、收益。'},
    43: {'name': '夬卦', 'sequence': '☰☱', 'yao': '－－－－－－', 'meaning': '象征决断、果断。'},
    44: {'name': '姤卦', 'sequence': '☱☰', 'yao': '－－－－－－', 'meaning': '象征相遇、偶然。'},
    45: {'name': '萃卦', 'sequence': '☷☱', 'yao': '－－ －－ －－', 'meaning': '象征聚集、汇合。'},
    46: {'name': '升卦', 'sequence': '☴☷', 'yao': '－－ －－ －－', 'meaning': '象征上升、升高。'},
    47: {'name': '困卦', 'sequence': '☵☱', 'yao': '－－ －－ －－ －', 'meaning': '象征困境、困苦。'},
    48: {'name': '井卦', 'sequence': '☵☴', 'yao': '－－ －－ －－ －', 'meaning': '象征井井有条。'},
    49: {'name': '革卦', 'sequence': '☲☵', 'yao': '－－ －－ －－', 'meaning': '象征变革、改造。'},
    50: {'name': '鼎卦', 'sequence': '☴☲', 'yao': '－－ －－ －－ －', 'meaning': '象征稳定、安定。'},
    51: {'name': '震卦', 'sequence': '☳☳', 'yao': '－－ －－ －－ －', 'meaning': '象征雷动、变化。'},
    52: {'name': '艮卦', 'sequence': '☶☶', 'yao': '－－ －－ －－', 'meaning': '象征山岳、止息。'},
    53: {'name': '渐卦', 'sequence': '☴☶', 'yao': '－－ －－ －－', 'meaning': '象征渐进、逐步。'},
    54: {'name': '归妹卦', 'sequence': '☱☴', 'yao': '－－ －－ －－', 'meaning': '象征归嫁、回归。'},
    55: {'name': '丰卦', 'sequence': '☲☴', 'yao': '－－ －－ －－ －', 'meaning': '象征丰收、富足。'},
    56: {'name': '旅卦', 'sequence': '☲☶', 'yao': '－－ －－ －－ －', 'meaning': '象征旅行、漂泊。'},
    57: {'name': '巽卦', 'sequence': '☴☴', 'yao': '－－ －－ －－', 'meaning': '象征风、柔顺。'},
    58: {'name': '兑卦', 'sequence': '☱☱', 'yao': '－－ －－ －－', 'meaning': '象征喜悦、交流。'},
    59: {'name': '涣卦', 'sequence': '☵☴', 'yao': '－－ －－ －－', 'meaning': '象征散开、离散。'},
    60: {'name': '节卦', 'sequence': '☵☵', 'yao': '－－ －－ －－ －', 'meaning': '象征限制、节制。'},
    61: {'name': '中孚卦', 'sequence': '☴☱', 'yao': '－－ －－ －－', 'meaning': '象征诚信、信仰。'},
    62: {'name': '小过卦', 'sequence': '☶☱', 'yao': '－－ －－ －－', 'meaning': '象征小有过失。'},
    63: {'name': '既济卦', 'sequence': '☵☲', 'yao': '－－ －－ －－ －', 'meaning': '象征成功、完成。'},
    64: {'name': '未济卦', 'sequence': '☲☵', 'yao': '－－ －－ －－ －', 'meaning': '象征未完成。'}
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
    print("未获取到对应的卦像")