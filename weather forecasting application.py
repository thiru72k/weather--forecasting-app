import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.config(bg="#d0e7f9")  # Slightly darker light blue background
        
        # Define styles
        label_font = ("Helvetica", 14)
        entry_font = ("Helvetica", 12)
        btn_font = ("Helvetica", 12, "bold")
        weather_font = ("Arial", 14, "italic")
        detail_font = ("Arial", 14)
        
        self.label_city = tk.Label(root, text="Enter city:", font=label_font, bg="#d0e7f9")
        self.label_city.pack(pady=10)
        
        self.entry_city = tk.Entry(root, width=30, font=entry_font)
        self.entry_city.pack(pady=5)
        
        self.btn_get_weather = tk.Button(root, text="Get Weather", command=self.get_weather, font=btn_font, bg="#357ab7", fg="white")
        self.btn_get_weather.pack(pady=10)
        
        self.frame_weather_details = tk.Frame(root, bg="#d0e7f9")
        self.frame_weather_details.pack(pady=20)
        
        self.label_result = tk.Label(self.frame_weather_details, text="", font=weather_font, bg="#d0e7f9")
        self.label_result.pack()
        
        self.label_weather = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="blue")
        self.label_weather.pack(pady=5)
        
        self.label_temperature = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="red")
        self.label_temperature.pack(pady=5)
        
        self.label_humidity = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="green")
        self.label_humidity.pack(pady=5)
        
        self.label_wind_speed = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="purple")
        self.label_wind_speed.pack(pady=5)
        
        self.label_pressure = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="orange")
        self.label_pressure.pack(pady=5)
        
        self.label_sunrise = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="goldenrod")
        self.label_sunset = tk.Label(self.frame_weather_details, text="", font=detail_font, bg="#d0e7f9", fg="darkorange")
        self.label_sunrise.pack(pady=5)
        self.label_sunset.pack(pady=5)
        
        self.weather_data = None
        
    def get_weather(self):
        city = self.entry_city.get()
        weather_data = self.fetch_weather(city)
        
        if weather_data:
            self.weather_data = weather_data
            weather, temperature, humidity, wind_speed, pressure, sunrise, sunset = weather_data
            self.label_result.config(text=f"Weather data for {city}:")
            self.label_weather.config(text=f"Description: {weather}")
            self.label_temperature.config(text=f"Temperature: {temperature}°C")
            self.label_humidity.config(text=f"Humidity: {humidity}%")
            self.label_wind_speed.config(text=f"Wind Speed: {wind_speed} m/s")
            self.label_pressure.config(text=f"Pressure: {pressure} hPa")
            self.label_sunrise.config(text=f"Sunrise: {sunrise}")
            self.label_sunset.config(text=f"Sunset: {sunset}")
        else:
            messagebox.showerror("Error", "Cannot retrieve weather data.")
    
    def fetch_weather(self, city):
        api_key = '3055057a1e7e848e4c348bac7a2d6744'
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(api_url)
            data = response.json()
            if data["cod"] == 200:
                weather = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                pressure = data["main"]["pressure"]
                sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
                sunset = datetime.utcfromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
                return weather, temperature, humidity, wind_speed, pressure, sunrise, sunset
            else:
                return None
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return None

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()








