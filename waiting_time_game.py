"""
In this game we are going to check the exact time the player is able to count with respect to the computer time
As soon as you press enter the application tells you to wait some random amount of time and press enter after random seconds of wait time
if the user is able to count exact time and hit enter the application will let you know the user how much time has elapsed

"""
import time
import random


def waiting_time_game():
    target = random.randint(2, 8)
    print("----------welcome to waiting time game----------")
    print(f"\n target second for you is {target}seconds")
    input("\n------Press Enter to begin-------")
    timer_start = time.perf_counter()
    input(f"...press enter after {target} seconds")
    time_elapsed = time.perf_counter() - timer_start
    if time_elapsed == timer_start:
        print("Unbeliveable !! exact time")
    elif time_elapsed < target:
        print(f"{target-time_elapsed} seconds fast")
    else:
        print(f"{time_elapsed-target} seconds slow")


if __name__ == '__main__':
    waiting_time_game()