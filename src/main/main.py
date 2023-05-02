import time, keyboard, sys, playsound
"""
Возможности для улучшение.
1) Добавить исключения
2) Добавить многопоточность для корректной работы stop_count"""

# def stop_count():
#     tag = False
#     if keyboard.hook(any(),):
#         return tag = True

def sound_beep():
    file = "../../data/static/bell.wav"
    playsound.playsound(file)

def time_count(period):
    while 0 < period:
        if not keyboard.is_pressed("space"):
            time.sleep(1)
            period -= 1
            print(period)
        else:
            print("Завершение работы программы.")
            sys.exit()


def main():
    work_time_min = int(input("Введите первый интервал времени в минутах: "))
    rest_time_min = int(input("Введите второй интервал времени в минутах: "))
    work_time_sec = work_time_min * 60
    rest_time_sec = rest_time_min * 60

    print("Для остановки таймера зажмите пробел.")
    while True:
        print("Отсчет времени работы.")
        sound_beep()
        time_count(work_time_sec)  # for work
        print("Отсчет времени отдыха.")
        sound_beep()
        time_count(rest_time_sec)  # for rest


main()
