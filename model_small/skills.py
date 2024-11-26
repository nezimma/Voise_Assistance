import json
import os, webbrowser, sys, requests, subprocess
from tkinter import Tk, Label, CENTER

import voice
from tkinter_window import *
import time
import pyautogui
import time
import psutil
import g4f
import queue
import sounddevice as sd
import vosk
import keyboard

def translate_to_english_keyboard_layout(word):
    translation_map = {
        'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i',
        'щ': 'o', 'з': 'p', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h',
        'о': 'j', 'л': 'k', 'д': 'l', 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v',
        'и': 'b', 'т': 'n', 'ь': 'm', 'б':',', 'ю':'.',
        'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U',
        'Ш': 'I', 'Щ': 'O', 'З': 'P',  'Ф': "A",  "Ы": "S",  "В": "D",  "А": "F",
        "П": "G",  "Р": "H",  "О": "J",  "Л": "K",  "Д": "L",  "Я": "Z",  "Ч": "X",
        "С": "C",  "М": "V",  "И": "B",  "Т": "N",  "Ь": "M"
    }
    translated_word = ''
    for letter in word:
        if letter in translation_map:
            translated_word += translation_map[letter]
        else:
            translated_word += letter
    return translated_word

def heh():
    print()

def weather():
    try:
        params = {'q': 'Minsk', 'units': 'metric', 'lang': 'ru', 'appid': 'c6aae79ad54f4c7446fffcdf9669be72'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')

def utube():
    webbrowser.open('https://www.youtube.com', new=0)

def hi():

    def finish():
        root.destroy()
    root = Tk()
    root.title('Приветствие от булки')

    root.geometry('300x250+600+300')
    label = Label(text="Здраствуйте, я Булка☺")
    label.pack()

    label.anchor(anchor=CENTER)
    root.after(3000, finish)
    root.mainloop()

def spoti():
    os.startfile(r'C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe')
    time.sleep(1)
    pyautogui.press('space')

def next():
    os.startfile(r'C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'right')

def back():
    os.startfile(r'C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'left')

def stop():
    os.startfile(r'C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe')
    time.sleep(1)
    pyautogui.press('space')

def GPT():
    question = ''
    q = queue.Queue()
    model = vosk.Model('model_small')

    device = sd.default.device = 1, 4
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16', channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while question == '':
            data = q.get()
            if rec.AcceptWaveform(data):
                question = rec.Result()


    out = ''
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    for message in response:
        out += message
    out = out.replace("*", '')
    out = out.replace('#', '')
    print(out)

    voice.speaker(out)

def tg():
    os.startfile(r"D:\progr\Telegram Desktop\Telegram.exe")
    personazh = ''
    q = queue.Queue()
    model = vosk.Model('model_small')

    device = sd.default.device = 2, 4
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16', channels=1,
                           callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while personazh == '':
            data = q.get()
            if rec.AcceptWaveform(data):
                personazh = json.loads(rec.Result())['text']

    pyautogui.press('esc')   
    time.sleep(3)
    print(personazh)
    if personazh == 'никита':
        print()
        keyboard.write('hhx232')
    if personazh == 'ульяна':
        print()
        keyboard.write('ul')
    if personazh == 'катя' :
        print()
        keyboard.write('kkkatkka')
    time.sleep(2)
    pyautogui.press('enter')



    voice.speaker('продиктуйте текст')

    personazh = ''
    q = queue.Queue()
    model = vosk.Model('model_small')

    device = sd.default.device = 2, 4
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16', channels=1,
                           callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while personazh == '':
            data = q.get()
            if rec.AcceptWaveform(data):
                personazh = json.loads(rec.Result())['text']

    personazh = translate_to_english_keyboard_layout(personazh)
    time.sleep(2)
    pyautogui.write(personazh)
    pyautogui.press('enter')
    print(personazh)
