# -*- coding: utf-8 -*-
"""输入一段文字, 编码成 GBK 之后再当作 UTF-8 读出来, 得到乱码, ASCII编码无效。

命令行运行:
    python kkk.py 输入
    python kkk.py 你好

其它文件引用:
    import kkk
    print(kkk.to_kkk("你好"))
"""

import sys


def to_kkk(text):
    gbk_bytes = text.encode("gbk", errors="replace")
    utf8_text = gbk_bytes.decode("utf-8", errors="replace")
    replacement_utf8_bytes = utf8_text.encode("utf-8", errors="replace")
    text_ = replacement_utf8_bytes.decode("gbk", errors="replace")
    return text_


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = str(input("请输入文本: "))
    print(to_kkk(text))
