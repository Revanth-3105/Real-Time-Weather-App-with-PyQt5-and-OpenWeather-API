# Real-Time-Weather-App-with-PyQt5-and-OpenWeather-API
Real-Time Weather App with PyQt5 and OpenWeather API

**Real-Time Weather App with PyQt5 and OpenWeather API:**

**Project Overview:**
This project is a user-friendly desktop application built using PyQt5 that fetches real-time weather data from the OpenWeather API. It provides users with an intuitive graphical interface to view current temperature, weather conditions, and relevant weather icons based on the city name entered. The application is designed to handle a variety of HTTP and network errors to ensure smooth functionality even during connectivity issues.

**Key Features:**

Real-Time Weather Data: The application retrieves up-to-date weather information from the OpenWeather API by allowing users to input any city name.
Temperature Display: The app converts temperature from Kelvin (as provided by the API) to Celsius, offering a clear and concise display.

Dynamic Weather Icons: The app includes weather icons (such as ☀️, 🌧️, ⛈️, 🌪️, etc.) based on the weather condition codes returned by the API. These icons make the weather information visually engaging.

Error Handling: Comprehensive error handling is implemented for various HTTP response codes (e.g., 400 Bad Request, 404 City Not Found) and network issues such as connection errors or timeouts. This ensures the app remains reliable and informative during server or connection failures.

Responsive Design: The application window is designed with well-aligned widgets using PyQt5’s layout system, ensuring a visually appealing and responsive interface on different screen sizes.


**Technical Details:**

API Integration: Utilizes the OpenWeather API to fetch current weather data based on the city name entered by the user. The API key is required for making requests, and error messages are displayed if the city is not found or there is an issue with the API.

PyQt5 for GUI: The graphical user interface is created with PyQt5, a comprehensive Python binding for the Qt toolkit. The interface includes text input fields, buttons, and dynamic labels that update based on API responses.

Error Handling: Robust exception handling for potential issues such as bad requests, unauthorized access (invalid API key), connection errors, and other HTTP-related errors ensures the app doesn’t crash and instead provides clear feedback to users.

**How to Use:**

Clone the repository and install the required dependencies using pip install -r requirements.txt.

Replace the api_key in the script with your OpenWeather API key.

Run the application, and input the city name in the text field.

Click the "Get Weather" button to display real-time weather data, including temperature in Celsius, weather description, and a corresponding icon.


**System Requirements:**

Python 3.x

PyQt5

Requests

**Interface:**

![image](https://github.com/user-attachments/assets/c59855a5-be5c-4ed6-9513-241c811cd821)



**Future Improvements:**

Add support for multiple units of temperature (e.g., Fahrenheit).

Implement 5-day weather forecast functionality.

Add localization for multiple languages.
