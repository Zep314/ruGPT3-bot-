# Функционал работы с журналом

import time

# def add2log(text,direction = '>'): # пишем все в лог - файл
#     with open(settings.log_file, 'a', encoding='UTF-8') as f:
#         f.write(f'{time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))}:{direction} {text}\n')
#     return


def add2log(text):  # пишем все в лог - файл
    with open('tb.log', 'a', encoding='UTF-8') as f:
        f.write(
            f'{time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))},{text}\n')
