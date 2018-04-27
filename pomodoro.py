import os
import time


pomodoros = 0


def pomodoro_timer(pomodoro_length=5):
    seconds = 0
    minutes = 0
    global pomodoros
    while True:
        if seconds >= 59:
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
            print(f'Pomodoros Completed: {pomodoros}\n')
            print(f'1 Min {seconds} Secs')
        else:
            print(f'Pomodoros Completed: {pomodoros}\n')
            print(f'{minutes} Mins {seconds} Secs')
        time.sleep(1)


def break_between_pomodoros(break_length=3):
    seconds = 0
    minutes = 0
    while True:
        if seconds >= 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == break_length:
            os.system('clear')
            print(f'{break_length} minute break is over!')
            break
        os.system('clear')
        seconds = seconds + 1
        if minutes == 1:
            print(f'{break_length} Minute Break: {minutes} Min {seconds} '
                  f'Secs')
        else:
            print(f'{break_length} Minute Break: {minutes} Mins {seconds} '
                  f'Secs')
        time.sleep(1)


def main():
    start = input('Enter S to start your first pomodoro or E to exit: ')
    if start.lower() == 's':
        while True:
            global pomodoros
            pomodoro_timer()
            if pomodoros < 4:
                short_break = input('Enter B to start a SHORT break: ')
                if short_break.lower() == 'b':
                    break_between_pomodoros()
            if pomodoros == 4:
                long_break = input('Enter B to start a LONG break: ')
                if long_break.lower() == 'b':
                    break_between_pomodoros(4)
            con = input('\n1) Enter S to start your next pomodoro.\n'
                        '2) Enter R to reset your pomodoro count\n'
                        '   and start a new set of pomodoros.\n'
                        '3) Enter E to exit.\n\n'
                        'Choose one of the above options: ')
            if con.lower() == 's':
                continue
            elif con.lower() == 'r':
                pomodoros = 0
                continue
            else:
                return
    else:
        return


if __name__ == '__main__':
    main()
