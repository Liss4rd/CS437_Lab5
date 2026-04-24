import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_data.csv")

# Pressure
plt.figure(figsize=(12,4))
plt.plot(df["time_s"], df["pressure_hPa"], linewidth=2)
plt.title("Pressure vs Time", fontweight="bold")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (hPa)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Temperature
plt.figure(figsize=(12,4))
plt.plot(df["time_s"], df["temperature_C"], linewidth=2)
plt.title("Temperature vs Time", fontweight="bold")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Humidity
plt.figure(figsize=(12,4))
plt.plot(df["time_s"], df["humidity_percent"], linewidth=2)
plt.title("Humidity vs Time", fontweight="bold")
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Vertical Speed
plt.figure(figsize=(12,4))
plt.plot(df["time_s"], df["vertical_speed_mps"], linewidth=2)
plt.title("Vertical Speed vs Time", fontweight="bold")
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()