"""
In this program we are going to design an alarm so that a function executes when the user wants the function to execute
The Alarm function would take 3 argumments alarm time, alarm sound and message
"""
import sched
import time
import winsound as ws


def alarm_settings(alarm_time, alarm_sound, alarm_message):
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enterabs(alarm_time,1,print,argument=(alarm_message,))
    schedule.enterabs(alarm_time,1,ws.PlaySound, argument=(alarm_sound, ws.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    schedule.run()


if __name__ == '__main__':
    alarm_settings(time.time()+2, 'beep-03.wav', 'wake-up')


