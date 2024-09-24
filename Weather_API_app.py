#Weather_API_App
# author : Revanth Kumar Paidi

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city Name: ",self)
        self.city_input =QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label =QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox= QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")


        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family:calibri;
            }
                
            QLabel#city_label{
                font-size:40px;
                font-style:italic;
            }
                           
            QLineEdit#city_input{
                font-size:40px;
            }
                           
            QPushButton#get_weather_button{
                font-size:30px;
                font-weight:bold;
            }
                           
            QLabel#temperature_label{
                font-size:75px;
            }
                           
            QLabel#emoji_label{
                font-size:100px;
                font-family:Segoe UI emoji;
            }
                           
            QLabel#description_label{
                font-size:50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

        
    def get_weather(self):
        
        api_key = "3ca8acf375178b0a820dc483d91e3161"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity Not Found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInavalid Response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is Down")
                case 504:
                    self.display_error("GateWay Timeout:\nNo Response from the server")
                case _:
                    self.display_error(f"HTTP error Occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe Request is Timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("TooManyRedirects:\nCheck the entered URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_K = data["main"]["temp"]
        temperature_C = temperature_K-273.15

        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature_C:.2f}°C")
        self.emoji_label.setText(self.get_Weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    
    @staticmethod
    def get_Weather_emoji(w_id):
        
        if 200 <= w_id <=232:
            return "⛈️"
        elif 300 <= w_id <=321:
            return "🌧"
        elif 500 <= w_id <=531:
            return "🌧️"
        elif 600 <= w_id <=622:
            return "🌨️"
        elif 700 <= w_id <=741:
            return "🌫️"
        elif w_id ==762:
            return "🌋"
        elif w_id ==771:
            return "💨"
        elif w_id ==781:
            return "🌪️"
        elif w_id ==800:
            return "☀️"
        elif 801 <= w_id <=804:
            return "☁️"
        else:
            return "emoji Not Loaded"



if __name__ =="__main__":
    app = QApplication(sys.argv)
    weather_app= WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
