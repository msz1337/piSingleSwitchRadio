#!/usr/bin/python3
import subprocess
import time
import threading
import json
import RPi.GPIO as GPIO


class ButtonThread(threading.Thread):

    press_start_time = 0.0
    button_action = 0  # 0 - no press or during press, 1 - short press, 2 - long press
    button_blocked = False  # is blocked by already interpreted >1sec press

    def run(self):
        ButtonThread.press_start_time = 0.0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
            if GPIO.input(18):  # not pressed
                ButtonThread.button_blocked = False
                if ButtonThread.press_start_time > 0 and 0 < time.time() - ButtonThread.press_start_time < 1:
                    ButtonThread.button_action = 1
                ButtonThread.press_start_time = 0
            elif not ButtonThread.button_blocked:  # pressed and not blocked
                if ButtonThread.press_start_time == 0:
                    ButtonThread.press_start_time = time.time()
                elif time.time() - ButtonThread.press_start_time > 1:
                    ButtonThread.button_action = 2
                    ButtonThread.press_start_time = 0
                    ButtonThread.button_blocked = True
            time.sleep(0.1)


    @staticmethod
    def get_button_action():
        returned_action = ButtonThread.button_action
        ButtonThread.button_action = 0  # to prevent reinterpreting
        return returned_action


if __name__ == '__main__':
    radio_index = -1
    espeak_process = False
    mpv_process = False
    button_thread = ButtonThread()
    button_thread.start()
    while True:
        button_action = ButtonThread.get_button_action()
        if button_action == 1:
            if espeak_process:
                espeak_process.kill()
            if mpv_process:
                mpv_process.kill()
            with open('piSingleSwithRadio.json', 'r') as config_file:
                radio_arr = json.loads(config_file.read())
            radio_index += 1
            if radio_index > len(radio_arr)-1:
                radio_index = 0
            espeak_process = subprocess.Popen(
                ['espeak', '-v', radio_arr[radio_index]['lang'], '"'+radio_arr[radio_index]['name']+'"'],
                shell=False,
                stdin=None,
                stdout=None,
                stderr=None
            )
            mpv_process = subprocess.Popen(
                ['mpv', '--no-video', '--ytdl=no', radio_arr[radio_index]['url']],
                shell=False,
                stdin=None,
                stdout=None,
                stderr=None
            )
        if button_action == 2:
            if espeak_process:
                espeak_process.kill()
            if mpv_process:
                mpv_process.kill()
            radio_index = -1
        time.sleep(0.2)