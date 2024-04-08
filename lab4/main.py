import requests
import matplotlib.pyplot as plt
import numpy as np
import json
import multiprocessing  # Just for opening both pyplot and tkinter apps at the same time
# Specifically for showing weather condition app
import tkinter as tk
from tkinter import ttk

coordinates = {
    'Gdynia': ('54.52', '18.53')
}
place = "Gdynia"

def show_temperature_plot(weather_data):
    """Shows temperature plot for given weather data"""
    # Preparing the data for plotting temperatures
    dates = weather_data['daily']['time']
    max_temperatures = np.array(weather_data['daily']['temperature_2m_max'])
    min_temperatures = np.array(weather_data['daily']['temperature_2m_min'])
    
    # Plotting temperatures
    plt.figure(figsize=(10, 6))

    # Color thresholds for temperatures
    thresholds = [0, 4, 8, 30]
    colors = ['lightblue', 'lightgreen', 'yellow']

    # Plotting temperature values and adding the temperature color effect
    for i in range(len(dates)):
        for j in range(len(thresholds) - 1):
            avg_temperature = (max_temperatures[i] + min_temperatures[i]) / 2.0
            if thresholds[j] <= avg_temperature <= thresholds[j + 1]:
                temperature_color = colors[j]
                break
        plt.fill_between([dates[i]], min_temperatures[i], max_temperatures[i], color=temperature_color, alpha=0.3, linewidth=10)

    plt.plot(dates, max_temperatures, 'r-', linewidth=0.5, label='Max Temperature')
    plt.plot(dates, min_temperatures, 'b-', linewidth=0.5, label='Min Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Weather Forecast for {place.capitalize()}')
    plt.xticks(rotation=45)  # For better date label representation
    plt.legend()
    plt.tight_layout()  # To make sure everything fits in the plot
    plt.show()

def format_weather_codes(weather_codes):
    """Formats weather codes returned from API to human readable outputs"""
    with open('weather_codes.json', 'r', encoding='utf-8') as file:
        weather_code_translation = json.load(file)
        formatted_codes = [weather_code_translation[str(code)] for code in weather_codes]
    return formatted_codes

def show_weather_condition_interface(dates, weather_codes):
    """Displays a window with given dates and weather_codes"""
    root = tk.Tk()
    root.title("Weather Information")

    num_items = len(dates)
    num_columns = 4
    num_rows = (num_items + num_columns - 1) // num_columns
    
    # Putting labels to grid.
    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            if index < num_items:
                date = dates[index]
                weather_code = weather_codes[index]
                
                date_label = ttk.Label(root, text=date)
                date_label.grid(row=i, column=j * 2, padx=10, pady=5, sticky="w")
                
                weather_code_label = ttk.Label(root, text=weather_code)
                weather_code_label.grid(row=i, column=j * 2 + 1, padx=10, pady=5, sticky="w")

    root.mainloop()

def show_weather_condition_window(weather_data):
    """Shows weather condition given weather data"""
    dates = weather_data['daily']['time']
    weather_codes = format_weather_codes(weather_data['daily']['weather_code'])
    show_weather_condition_interface(dates, weather_codes)

def show_weather_status(weather_data):
    """Opens up both temperature and weather condition apps"""
    # Creating processes for both tasks
    temperature_plot_process = multiprocessing.Process(target=show_temperature_plot, args=(weather_data,))
    weather_condition_window_process = multiprocessing.Process(target=show_weather_condition_window, args=(weather_data,))

    temperature_plot_process.start()
    weather_condition_window_process.start()
    
    # Waiting for both processes to finish
    temperature_plot_process.join()
    weather_condition_window_process.join()


if __name__ == '__main__':
    params = {
        "latitude": coordinates[place][0],
        "longitude": coordinates[place][1],
        "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code"],
        "start_date": "2024-03-01",
        "end_date": "2024-03-31"
    }
    
    # Getting the url for weather API
    weather_url = f'https://api.open-meteo.com/v1/forecast?'
    for key, value in params.items():
        # Handling multiple values for a given key
        if isinstance(value, list):
            weather_url += f'&{key}='
            for item in value:
                weather_url += f'{item},'
            weather_url = weather_url[:-1]
        else:
            weather_url += f'&{key}={value},'

    weather_url = weather_url[:-1]  # Remove the trailing comma
    weather_data = requests.get(weather_url).json()  # Getting weather data from API

    show_weather_status(weather_data)