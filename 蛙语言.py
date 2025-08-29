# -*- coding: utf-8 -*-


char_mapping: dict[str, str] = {
    'A': '蛙', 'B': '蝌', 'C': '蚪', 'D': '鼃', 'E': '鼈', 'F': '蝈',
    'G': '蜛', 'H': '蝦', 'I': '蚧', 'J': '蛭', 'K': '蛉', 'L': '蟇',
    'M': '蜻', 'N': '蜓', 'O': '螳', 'P': '螂', 'Q': '蟋', 'R': '蟀',
    'S': '蛾', 'T': '蝶', 'U': '蝇', 'V': '蚊', 'W': '蚋', 'X': '虻',
    'Y': '蚰', 'Z': '蜒',
    'a': '蚨', 'b': '蝉', 'c': '蝽', 'd': '蝾', 'e': '螈', 'f': '螭',
    'g': '虬', 'h': '蛟', 'i': '蟒', 'j': '蚺', 'k': '虺', 'l': '蜥',
    'm': '蜴', 'n': '蟾', 'o': '蜍', 'p': '蝎', 'q': '蚁', 'r': '蜂',
    's': '蚂', 't': '蚱', 'u': '蜢', 'v': '虱', 'w': '蚤', 'x': '蠹',
    'y': '螨', 'z': '蠓',
    '=': '蚬',
    '0': '蛤', '1': '蟆', '2': '蟌', '3': '蚣', '4': '蚓', '5': '螺',
    '6': '蚌', '7': '蛏', '8': '蚶', '9': '鱿',
    '/': '蜈', '+': '蛄'
}

from base64 import b64encode, b64decode


def encode(msg: str):
    msg_bytes = msg.encode('utf-8')
    b64_bytes = b64encode(msg_bytes)
    b64_str = b64_bytes.decode('utf-8')
    final_result = b64_str
    for char, replacement in char_mapping.items():
        final_result = final_result.replace(char, replacement)
    return '蛙曰:' + final_result


def decode(msg: str):
    # 删除开头的蛙曰:
    msg = msg.replace('蛙曰:', '')
    # 生成反向映射表
    reverse_mapping = {v: k for k, v in char_mapping.items()}
    # 将蛙语还原为base64字符串
    base64_str = msg
    for char, replacement in reverse_mapping.items():
        base64_str = base64_str.replace(char, replacement)
    base64_bytes = base64_str.encode('utf-8')
    msg_bytes = b64decode(base64_bytes)
    original_msg = msg_bytes.decode('utf-8')
    return original_msg


while True:
    print('>> 输入模式 1为编码 2为解码')
    mode = input('>> ')
    if mode == '1':
        print('>> 输入需要编码的内容')
        msg = input('>> ')
        print(encode(msg))
    elif mode == '2':
        print('>> 输入需要解码的内容')
        msg = input('>> ')
        print(decode(msg))
    else:
        print('>> 请输入正确的方式')