from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import requests
from io import BytesIO
from random import randint


def hamster_to(message):
    message = message.replace('а', 'a')
    message = message.replace('б', 'b')
    message = message.replace('в', 'v')
    message = message.replace('г', 'g')
    message = message.replace('д', 'd')
    message = message.replace('е', 'e')
    message = message.replace('ё', 'qo')
    message = message.replace('ж', 'j')
    message = message.replace('з', 'z')
    message = message.replace('и', 'y')
    message = message.replace('й', 'q')
    message = message.replace('к', 'k')
    message = message.replace('л', 'l')
    message = message.replace('м', 'm')
    message = message.replace('н', 'n')
    message = message.replace('о', 'o')
    message = message.replace('п', 'p')
    message = message.replace('р', 'r')
    message = message.replace('с', 's')
    message = message.replace('т', 't')
    message = message.replace('у', 'u')
    message = message.replace('ф', 'f')
    message = message.replace('х', 'h')
    message = message.replace('ц', 'c')
    message = message.replace('ч', 'x')
    message = message.replace('ш', 'w')
    message = message.replace('щ', 'wx')
    message = message.replace('ы', '#')
    message = message.replace('ь', "'")
    message = message.replace('ъ', '"')
    message = message.replace('э', 'ai')
    message = message.replace('ю', 'qu')
    message = message.replace('я', 'qa')
    return message


def hamster_from(message):
    message = message.replace('a', 'а')
    message = message.replace('b', 'б')
    message = message.replace('v', 'в')
    message = message.replace('g', 'г')
    message = message.replace('d', 'д')
    message = message.replace('e', 'е')
    message = message.replace('qo', 'ё')
    message = message.replace('j', 'ж')
    message = message.replace('z', 'з')
    message = message.replace('y', 'и')
    message = message.replace('q', 'й')
    message = message.replace('k', 'к')
    message = message.replace('l', 'л')
    message = message.replace('m', 'м')
    message = message.replace('n', 'н')
    message = message.replace('o', 'о')
    message = message.replace('p', 'п')
    message = message.replace('r', 'р')
    message = message.replace('s', 'с')
    message = message.replace('t', 'т')
    message = message.replace('u', 'у')
    message = message.replace('f', 'ф')
    message = message.replace('h', 'х')
    message = message.replace('c', 'ц')
    message = message.replace('x', 'ч')
    message = message.replace('w', 'ш')
    message = message.replace('wx', 'щ')
    message = message.replace('#', 'ы')
    message = message.replace("'", 'ь')
    message = message.replace('"', 'ъ')
    message = message.replace('ai', 'э')
    message = message.replace('qu', 'ю')
    message = message.replace('qa', 'я')
    return message


def enter_decoder_code(enter_value, combobox_value, key):
    result = ""
    if combobox_value == "true" and enter_value != "":
        for i in range(len(enter_value)):
            char = enter_value[i]
            if char.isupper():
                result += chr((ord(char) - int(key[i]) - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - int(key[i]) - 97) % 26 + 97)
            else:
                result += char
    elif combobox_value == "false" and enter_value != "":
        for i in range(len(enter_value)):
            char = enter_value[i]
            if char.isupper():
                result += chr((ord(char) + int(key[i]) - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + int(key[i]) - 97) % 26 + 97)
            else:
                result += char
    return result


def combobox_decoder_code(enter_value, combobox_value):
    if combobox_value == "true":
        file_key = open("Key", "r")
        key = file_key.read()
        file_key.close()
        final_text = enter_decoder_code(enter_value, combobox_value, key)
        result_text = hamster_from(final_text)
        messagebox.showinfo("Final A", result_text)
    else:
        final_text = hamster_to(enter_value)
        file_key = open("Key", "w+")
        for i in range(len(final_text)):
            file_key.write(str(randint(1, 9)))
        file_key.close()
        file_key = open("Key", "r")
        key = file_key.read()
        file_key.close()
        result_text = enter_decoder_code(final_text, combobox_value, key)
        messagebox.showinfo("Final B", result_text)


def start_program():
    enter_value = enter_secret_words.get().lower()
    combobox_value = combobox_list_bool_language.get().lower()
    if enter_value == "" and combobox_value == "":
        messagebox.showerror("Ошибка", "Пожалуйста, введите все данные!")

    elif enter_value == "" or (combobox_value != "true" and combobox_value != "false"):
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные данные!")

    else:
        messagebox.showinfo("Успех", "Процесс декодирования запущен.")
        combobox_decoder_code(enter_value, combobox_value)


# program
program = tk.Tk()  # create window program
program.title("Hamster language")
# send get request
response = requests.get(
    "https://avatars.mds.yandex.net/i?id=501088d665acccd8a7ba6764ce1af6230ce1e897-4865125-images-thumbs&n=13")
image_data = response.content  # Получает содержимое ответа (байтовые данные)
image_back = Image.open(BytesIO(image_data))
icon_program = ImageTk.PhotoImage(image_back)  # view pictures
program.iconphoto(False, icon_program)
program.geometry("450x500+310+80")
program.minsize(420, 70)
program.config(bg="#1C2023")
n = tk.StringVar()
n1 = tk.StringVar()

greetings = Label(program, text="Welcome in language decoder", font=("Roboto", 14, "bold"),
                  fg="#D18B22", padx=20, pady=20, bg="#1C2023")
greetings.place(x=30, y=20, width=390, height=20)
# enter
label_secret_words = Label(program, text="Enter text: ", font=("Roboto", 14, "normal"), fg="#D18B22", bg="#1C2023")
label_secret_words.place(x=50, y=70)
enter_secret_words = Entry(program, font=("Roboto", 14, "normal"), fg="white", relief=RAISED, bd=1, bg="#1C2023")
enter_secret_words.place(x=180, y=72)
# combobox 1
label_decoder_words = Label(program, text="Is it hamster language? ", font=("Roboto", 14, "normal"), fg="#D18B22",
                            bg="#1C2023")
label_decoder_words.place(x=50, y=120)
list_bool_language = ["true", "false"]  # list
combobox_list_bool_language = ttk.Combobox(program, values=list_bool_language, font=("Roboto", 12), height=10,
                                           style="TCombobox", textvariable=n, width=12)
combobox_list_bool_language.place(x=270, y=120)

# button
button_decoder = Button(program, text="Result", command=lambda: (start_program()), bg="#1C2023", cursor="hand2",
                        font=("Roboto", 14, "bold"), fg="#D18B22", activebackground='#D18B22')
button_decoder.place(x=200, y=180)
program.mainloop()
