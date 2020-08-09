"""
    文本颜色
    打印彩色字体方法: \033[{{显示方式}};{{字体色}};{{背景色}}m{{打印的内容}}\033[0m
    以下是对该方法的封装
"""


class RichPrint:
    @staticmethod
    def __make_head(ct: str = '', fg: str = '', bg: str = ''):
        __control = {'': 10, 'DEFAULT': 0, 'BOLD': 1, 'UNDERLINE': 4, 'FLASH': 5, 'SWAP': 7, 'HIDE': 8}
        __colors = {
            '': 10,
            'WHITE': 0, 'w': 0, 'RED': 1, 'r': 1, 'GREEN': 2, 'g': 2, 'YELLOW': 3, 'y': 3,
            'BLUE': 4, 'b': 4, 'PURPLE': 5, 'p': 5, 'CYAN': 6, 'c': 6, 'SHALLOW': 7, 's': 7
        }
        ct = str(__control[ct])
        fg = str(30 + __colors[fg])
        bg = str(40 + __colors[bg])
        return f'\033[{ct};{fg};{bg}m'

    @staticmethod
    def __make_tail():
        return '\033[0m'

    @staticmethod
    def p(content, foreground='', background='', control=''):
        """
        彩色不换行打印
        :param content: 内容
        :param foreground: 前景色
        :param background: 背景色
        :param control: 其它效果
        :return: None
        """
        print(f'{RichPrint.__make_head(control, foreground, background)}{content}{RichPrint.__make_tail()}', end='')

    @staticmethod
    def progress_bar(rate: float, length: int = 50, single_char1: str = '█', single_char2: str = '·'):
        rate = rate if rate < 1 else 1
        num_part_l = int(rate * length)
        num_part_r = length - num_part_l
        str_l = single_char1 * num_part_l
        str_r = single_char2 * num_part_r
        # print(f"\r[{str_l}>{str_r}] %.2f%% " % (rate * 100), end='')
        cy = RichPrint.__make_head(fg='y')
        cs = RichPrint.__make_head(fg='s')
        cb = RichPrint.__make_head(fg='b', ct='BOLD')
        _c = RichPrint.__make_tail()
        if 1 == rate:
            print(f"\r{cb}|{str_l}|{_c} {cy}100.00%{_c} ")
        else:
            print(
                f"\r{cb}|{str_l}{_c}{cs}{str_r}{_c}{cb}|{_c} {cy}%.2f%%{_c} "
                % (rate * 100), end=''
            )
