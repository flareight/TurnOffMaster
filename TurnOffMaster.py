import os 
import json
import time
import customtkinter as ct
from CTkMessagebox import CTkMessagebox
from datetime import datetime
from datetime import timedelta
from config import ICON_PATH

quantity_seconds = 0

def shutdown_or_restart(seconds, mode):
  try:
    if seconds > 0:
      if mode == 'Выключение':
        os.system(f'shutdown -s -t {seconds}')
      elif mode == 'Перезагрузка':
        os.system(f'shutdown -r -t {seconds}')
    else:
      raise ValueError

  except ValueError:
    CTkMessagebox(title = 'Ошибка', message = 'Некорректное время!', icon = 'warning')

def turn_offTimer():
  global quantity_seconds
  quantity_seconds = 0

  try:
    hours = int(hours_entry.get()) if hours_entry.get() else 0
    minutes = int(minutes_entry.get()) if minutes_entry.get() else 0
    quantity_seconds = (hours * 3600) + (minutes * 60)

    if quantity_seconds <= 0 or quantity_seconds > 310360000:
      raise ValueError
    else:
       shutdown_or_restart(quantity_seconds, mode.get())

  except ValueError:
    CTkMessagebox(title = 'Ошибка', message = 'Введите корректное время!', icon = 'warning')

def turn_offPlan():
  global quantity_seconds
  quantity_seconds = 0

  try:
    entry_time = datetime(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()), 
                          int(h_entry.get()), int(m_entry.get()), int(s_entry.get()))
    current_time_date = datetime.now()

    if current_time_date > entry_time:
      raise ValueError

    quantity_seconds = int((entry_time - current_time_date).total_seconds())

    if quantity_seconds <= 0 or quantity_seconds > 310360000:
      raise ValueError
    else:
       shutdown_or_restart(quantity_seconds, mode.get())

  except ValueError:
    CTkMessagebox(title = 'Ошибка', message = 'Введите корректное время!', icon = 'warning')            

def change_turn_off_button(event):
    selected_option = mode.get()
    turn_off_button['text'] = selected_option

def change_turn_off_buttonPlan(event):
    selected_option = modePlan.get()
    turn_off_buttonPlan['text'] = selected_option

def timer_change():
    global quantity_seconds

    if quantity_seconds >= 0 and quantity_seconds <= 310360000:
        timer.configure(text = str(timedelta(seconds = quantity_seconds)))
        if quantity_seconds > 0:
            timer.pack()
        else:
            timer.pack_forget()

    if quantity_seconds > 0 and quantity_seconds <= 310360000:
        quantity_seconds -= 1
        timer.after(1000, timer_change)

def timer_changePlan():
    global quantity_seconds

    try:
      if quantity_seconds >= 0 and quantity_seconds <= 310360000:
          timerPlan.configure(text = str(timedelta(seconds = quantity_seconds)))
          if quantity_seconds > 0:
              timerPlan.pack()
          else:
              timerPlan.pack_forget()
      else:
          raise ValueError

    except ValueError:
       CTkMessagebox(title = 'Ошибка', message = 'Введите положительные числа!', icon = 'warning')

    if quantity_seconds > 0 and quantity_seconds <= 310360000:
        quantity_seconds -= 1
        timerPlan.after(1000, timer_changePlan)

def button_cancel():
    try:
      global quantity_seconds
      if quantity_seconds != 0:
        os.system('shutdown -a')
        quantity_seconds = 0
        timer.place_forget()
        timerPlan.place_forget()
      else:
          raise ValueError

    except ValueError:
       CTkMessagebox(title = 'Ошибка', message = 'Отмена не предусмотрена', icon = 'warning')

def default_date():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if day_entry.get() == '' and month_entry.get() == '' and year_entry.get() == '':
        day_entry.insert(0, current_date[8:10])
        month_entry.insert(0, current_date[5:7])
        year_entry.insert(0, current_date[0:4])

    if h_entry.get() == '' and m_entry.get() == '' and s_entry.get() == '':
        h_entry.insert(0, current_date[11:13])
        m_entry.insert(0, current_date[14:16])
        s_entry.insert(0, current_date[17:19])

def hours_EntryPlus():
    try:
      value = int(hours_entry.get())
      hours_entry.delete(0, ct.END)
      hours_entry.insert(0, value + 1)

    except ValueError:
      if hours_entry.get() == '':
        hours_entry.insert(0, 1)
      else:
        CTkMessagebox(title='Ошибка', message='Введите корректное значение часов!', icon='warning') 

def hours_Entry_minus():
    try:
      value = int(hours_entry.get())
      hours_entry.delete(0, ct.END)
      hours_entry.insert(0, value - 1)

    except ValueError:
      if hours_entry.get() == '':
        hours_entry.insert(0, -1) 
      else:
        CTkMessagebox(title='Ошибка', message='Введите корректное значение часов!', icon='warning')

def minutes_EntryPlus():
    try:
      value = int(minutes_entry.get())
      minutes_entry.delete(0, ct.END)
      minutes_entry.insert(0, value + 1)

    except ValueError:
      if minutes_entry.get() == '':
        minutes_entry.insert(0, 1)
      else:
        CTkMessagebox(title='Ошибка', message='Введите корректное значение минут!', icon='warning')

def minutes_Entry_minus():
    try:
      value = int(minutes_entry.get())
      minutes_entry.delete(0, ct.END)
      minutes_entry.insert(0, value - 1)

    except ValueError:
      if minutes_entry.get() == '':
        minutes_entry.insert(0, -1)
      else:
        CTkMessagebox(title='Ошибка', message='Введите корректное значение минут!', icon='warning')

def switch_theme(value):
    if int(value) == 0:
        ct.set_appearance_mode('Light')
    else:
        ct.set_appearance_mode('Dark')

def switch_colors(value):
    if int(value) == 0:
        modePlan.configure(dropdown_fg_color = '#FFA500', dropdown_text_color = '#FF0000', text_color = '#FF0000', dropdown_hover_color = '#FF8C00')
        mode.configure(dropdown_fg_color = '#FFA500', dropdown_text_color = '#FF0000', text_color = '#FF0000', dropdown_hover_color = '#FF8C00')
    else:
        modePlan.configure(text_color = '#FFFFFF', dropdown_text_color = '#FFFFFF', dropdown_hover_color = '#474747', dropdown_fg_color = '#333333')
        mode.configure(text_color = '#FFFFFF', dropdown_text_color = '#FFFFFF', dropdown_hover_color = '#474747', dropdown_fg_color = '#333333')

app = ct.CTk()
app.title('Turn off Master')
app.iconbitmap(ICON_PATH)
app.geometry('550x350')
app.resizable(False, False)
ct.set_appearance_mode('dark')

tabview = ct.CTkTabview(app, width=530, height=340, border_width=2, 
                        segmented_button_fg_color='#FF0000', 
                        segmented_button_unselected_hover_color='#FFFF00', 
                        segmented_button_selected_hover_color='#FFFF00', 
                        segmented_button_selected_color='#FFD700', 
                        segmented_button_unselected_color='#FFD700', 
                        border_color='#FF0000', 
                        text_color='#000000')
tabview.pack(pady=5)

tabTimer = tabview.add('Таймер отключения')
tabPlan = tabview.add('Запланированное отключение')
tabview.set('Таймер отключения')

Var = ct.IntVar()
combobox_var = ct.StringVar(value='Выключение')

combobox_frame = ct.CTkFrame(tabTimer)
combobox_frame.pack(pady=10)

mode = ct.CTkComboBox(combobox_frame, values=['Выключение', 'Перезагрузка'], width=120, justify='center', 
                      button_color='#FFA500', border_color='#FFA500', text_color='#FFFFFF', 
                      dropdown_text_color='#FFFFFF', state='readonly', variable=combobox_var)
mode.pack()

hours_frame = ct.CTkFrame(tabTimer)
hours_frame.pack(pady=5)

hoursPlusButton = ct.CTkButton(hours_frame, text='+', width=30, text_color='#FFFFFF', 
                              hover_color='#FF0000', fg_color='#FFA500', command=lambda: hours_EntryPlus())
hoursPlusButton.pack(side='left', padx=5)

hours_entry = ct.CTkEntry(hours_frame, fg_color='#FFA500', placeholder_text='Часы', 
                          placeholder_text_color='#FFFFFF', text_color='#FFFFFF', width=80, justify='center')
hours_entry.pack(side='left', padx=5)

hoursMinusButton = ct.CTkButton(hours_frame, text='-', width=30, text_color='#FFFFFF', 
                               hover_color='#FF0000', fg_color='#FFA500', command=lambda: hours_Entry_minus())
hoursMinusButton.pack(side='left', padx=5)

minutes_frame = ct.CTkFrame(tabTimer)
minutes_frame.pack(pady=5)

minutesPlusButton = ct.CTkButton(minutes_frame, text='+', width=30, text_color='#FFFFFF', 
                                hover_color='#FF0000', fg_color='#FFA500', command=lambda: minutes_EntryPlus())
minutesPlusButton.pack(side='left', padx=5)

minutes_entry = ct.CTkEntry(minutes_frame, placeholder_text='Минуты', placeholder_text_color='#FFFFFF', 
                            fg_color='#FFA500', text_color='#FFFFFF', width=80, justify='center')
minutes_entry.pack(side='left', padx=5)

minutesMinusButton = ct.CTkButton(minutes_frame, text='-', width=30, text_color='#FFFFFF', 
                                 hover_color='#FF0000', fg_color='#FFA500', command=lambda: minutes_Entry_minus())
minutesMinusButton.pack(side='left', padx=5)

button_frame = ct.CTkFrame(tabTimer)
button_frame.pack(pady=20)

turn_off_button = ct.CTkButton(button_frame, textvariable=combobox_var, text_color='#FFFFFF', 
                              hover_color='#FF0000', fg_color='#FFA500', 
                              command=lambda: (turn_offTimer(), timer_change()))
turn_off_button.pack(side='left', padx=10)

cancel_button = ct.CTkButton(button_frame, text='Отмена действия', text_color='#FFFFFF', 
                            hover_color='#FF0000', fg_color='#FFA500', command=lambda: button_cancel())
cancel_button.pack(side='left', padx=10)

default_date_frame = ct.CTkFrame(tabPlan)
default_date_frame.pack(pady=5)

default_date_buttonPlan = ct.CTkButton(default_date_frame, text='Заполнить текущим временем', 
                                      text_color='#FFFFFF', hover_color='#FF0000', fg_color='#FFA500', 
                                      command=lambda: default_date())
default_date_buttonPlan.pack()

time_frame = ct.CTkFrame(tabPlan)
time_frame.pack(pady=5)

h_entry = ct.CTkEntry(time_frame, text_color='#FF0000', fg_color='#FFA500', width=80, justify='center')
h_entry.pack(side='left', padx=5)

m_entry = ct.CTkEntry(time_frame, text_color='#FF0000', fg_color='#FFA500', width=80, justify='center')
m_entry.pack(side='left', padx=5)

s_entry = ct.CTkEntry(time_frame, text_color='#FF0000', fg_color='#FFA500', width=80, justify='center')
s_entry.pack(side='left', padx=5)

date_frame = ct.CTkFrame(tabPlan)
date_frame.pack(pady=5)

day_entry = ct.CTkEntry(date_frame, text_color='#FF0000', fg_color='#FFA500', width=80, justify='center')
day_entry.pack(side='left', padx=5)

month_entry = ct.CTkEntry(date_frame, text_color='#FF0000', fg_color='#FFA500', width=80, justify='center')
month_entry.pack(side='left', padx=5)

year_entry = ct.CTkEntry(date_frame, text_color='#FF0000', fg_color='#FFA500', width=80, justify='center')
year_entry.pack(side='left', padx=5)

combobox_plan_frame = ct.CTkFrame(tabPlan)
combobox_plan_frame.pack(pady=10)

modePlan = ct.CTkComboBox(combobox_plan_frame, values=['Выключение', 'Перезагрузка'], width=120, justify='center', 
                         button_color='#FFA500', border_color='#FFA500', text_color='#FFFFFF', 
                         dropdown_text_color='#FFFFFF', state='readonly', variable=combobox_var)
modePlan.pack()

theme_slider = ct.CTkSlider(app, from_ = 0, to = 1, number_of_steps = 1, width = 40, command = lambda value: (switch_theme(value), switch_colors(value)))
theme_slider.place(x = 35, y = 300)

initial_value = 0 if ct.get_appearance_mode() == 'Light' else 1
theme_slider.set(initial_value)

button_plan_frame = ct.CTkFrame(tabPlan)
button_plan_frame.pack(pady=10)

turn_off_buttonPlan = ct.CTkButton(button_plan_frame, textvariable=combobox_var, text_color='#FFFFFF', 
                                  hover_color='#FF0000', fg_color='#FFA500', 
                                  command=lambda: (turn_offPlan(), timer_changePlan()))
turn_off_buttonPlan.pack(side='left', padx=10)

cancel_buttonPlan = ct.CTkButton(button_plan_frame, text='Отмена действия', text_color='#FFFFFF', 
                                hover_color='#FF0000', fg_color='#FFA500', command=lambda: button_cancel())
cancel_buttonPlan.pack(side='left', padx=10)

timer = ct.CTkLabel(tabTimer, text='', font=('Tahoma', 38), text_color='#FF0000')
timer.pack()

timerPlan = ct.CTkLabel(tabPlan, text='', font=('Tahoma', 38), text_color='#FF0000')
timerPlan.pack()

mode.bind('<<ComboboxSelected>>', lambda event: change_turn_off_button(event))
modePlan.bind('<<ComboboxSelected>>', lambda event: change_turn_off_buttonPlan(event))

app.mainloop()