import os
import time


pomodoros = 0


def pomodoro_timer(pomodoro_length=1):
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
            print(f'1 Min {seconds} Secs\n')
        else:
            print(f'Pomodoros Completed: {pomodoros}\n')
            print(f'{minutes} Mins {seconds} Secs\n')
        time.sleep(1)


def break_between_pomodoros(break_length=2):
    seconds = 0
    minutes = 0
    while True:
        if seconds >= 59:
            seconds = 0
            minutes = minutes + 1
        if minutes == break_length:
            os.system('clear')
            print(f'{break_length} minute break is over!\n')
            break
        os.system('clear')
        seconds = seconds + 1
        if minutes == 1:
            print(f'{break_length} Minute Break: {minutes} Min {seconds} '
                  f'Secs\n')
        else:
            print(f'{break_length} Minute Break: {minutes} Mins {seconds} '
                  f'Secs\n')
        time.sleep(1)


def main():
    start = input('Enter S to start pomodoro timer: ')
    if start.lower() == 's':
        while True:
            pomodoro_timer()
            if pomodoros < 4:
                short_break = input('Enter B to start a short break: ')
                if short_break.lower() == 'b':
                    break_between_pomodoros()
            if pomodoros == 4:
                long_break = input('Enter B to start a long break: ')
                if long_break.lower() == 'b':
                    break_between_pomodoros(3)
                    # TODO: Need to reset the pomodoro counter back to zero
                    # after a long break...OR an option for the user to
                    # select whether to reset the counter and start a new
                    # set of pomodoros or continue incrementing the counter
                    # as is...
            con = input('Enter C to continue and start your next pomodoro: ')
            if con.lower() == 'c':
                continue


if __name__ == '__main__':
    main()
