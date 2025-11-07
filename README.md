



## 🌦️ Weather App (Python)

This is a simple command-line Weather App built using Python’s `requests` library and the [WeatherAPI](https://www.weatherapi.com/).
It allows you to fetch and display real-time weather information for any city entered by the user.

---

### 🧠 Features

* 🌍 Get current weather details for any city.
* ⚡ Uses live data from WeatherAPI.
* 🧾 Displays raw JSON weather information.
* 🐍 Written in simple, beginner-friendly Python code.

---

### 💻 Requirements

Before running the project, install the required dependency:

```bash
pip install requests
```

---

### 🚀 Usage

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Run the script:

```bash
python weather.py
```

4. Enter your city name when prompted:

```
Enter the city: London
```

5. The program will display the current weather details in JSON format.

---

### 🧩 Example Output

```
Enter the city: Delhi
{
  "location": {
    "name": "Delhi",
    "region": "Delhi",
    "country": "India",
    ...
  },
  "current": {
    "temp_c": 28.5,
    "condition": {
      "text": "Partly cloudy"
    },
    ...
  }
}
```

---

### 🔐 API Key Setup

Replace your actual API key in this line inside your code:

```python
url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
```

Or better — use an environment variable (for safety):

```python
import os
API_KEY = os.getenv("WEATHER_API_KEY")
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
```

Set it before running:

```bash
set WEATHER_API_KEY=your_api_key_here   # Windows
export WEATHER_API_KEY=your_api_key_here # Mac/Linux
```

---

### 🧰 Technologies Used

* **Python 3**
* **Requests Library**
* **WeatherAPI**

---

### 🧑‍💻 Author

**Muzammil Ahsan**
Tech Explorer | AI & ML Enthusiast | Data Science Learner

