import os
import time


pomodoros = 0


def pomodoro_timer(pomodoro_length=25):
    seconds = 0
    minutes = 0
    global pomodoros
    while True:
        if seconds > 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == pomodoro_length:
            pomodoros = pomodoros + 1
            os.system('clear')
            if pomodoros == 1:
                print('You have completed 1 pomodoro.')
            else:
                print(f'You have completed {pomodoros} pomodoros.')
            break
        os.system('clear')
        seconds = seconds + 1
        if minutes == 1:
            print(f'1 Minute {seconds} Seconds\n')
        else:
            print(f'{minutes} Minutes {seconds} Seconds\n')
        time.sleep(1)


def break_between_pomodoros(break_length=5):
    seconds = 0
    minutes = 0
    while True:
        if seconds > 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == break_length:
            os.system('clear')
            print(f'{break_length} minute break is over!')
            break
        os.system('clear')
        seconds = seconds + 1
        if minutes == 1:
            print(f'{minutes} Minute {seconds} Seconds\n')
        else:
            print(f'{minutes} Minutes {seconds} Seconds\n')
        time.sleep(1)


def main():
    start = input('Enter "s" to start pomodoro timer: ')
    if start.lower() == 's':
        pomodoro_timer()
    short_break = input('Enter "b" to start short break: ')
    if short_break.lower() == 'b':
        break_between_pomodoros()


if __name__ == '__main__':
    main()
