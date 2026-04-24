
"""
Program 1: Wind Direction Map
Reads gps_data.csv and plots the balloon's route with bold arrows
showing direction of travel. Arrows are colored by speed.
"""
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np


def load_gps(path):
   """
   Load GPS data from a CSV file.

   Reads the file and extracts the time_s, latitude, and longitude
   columns into separate lists.

   Args:
       path (str): Path to the GPS CSV file.

   Returns:
       times (list): List of timestamps in seconds.
       lats (list):  List of latitude values.
       lons (list):  List of longitude values.
   """
   times, lats, lons = [], [], []
   with open(path, mode="r", newline="") as f:
       reader = csv.DictReader(f)
       for row in reader:
           times.append(float(row["time_s"]))
           lats.append(float(row["latitude"]))
           lons.append(float(row["longitude"]))
   return times, lats, lons


def plot_wind_map(lats, lons, step, title, out_path):
   """
   Plot a wind direction map showing the balloon's route with arrows.

   This function should:
   1. Create a matplotlib figure and axis.
   2. Loop through the GPS data with a stride of (2 * step) to create
      non-overlapping arrow segments. For each segment from index i to
      i + step, compute:

      - du = longitude difference (lons[i+step] - lons[i])
      - dv = latitude difference (lats[i+step] - lats[i])
      - speed = magnitude of (du, dv) using math.sqrt
   3. Normalize the speed values and use a colormap (e.g. "viridis")
      to assign a color to each arrow based on its speed.
   4. Draw each arrow using matplotlib.patches.FancyArrowPatch with
      the computed start point, end point, and color.
   5. Add a colorbar, axis labels, title, and grid.
   6. Save the figure to out_path.

   Args:
       lats (list):    List of latitude values from GPS data.
       lons (list):    List of longitude values from GPS data.
       step (int):     Number of rows between arrow start and end.
       title (str):    Title for the plot.
       out_path (str): File path to save the output figure.
   """
   # TODO: Create a figure and axis using plt.subplots()
   fig, axis = plt.subplots(figsize = (9, 7))

   # TODO: Loop through the data to build arrow segments
   #       Use range(0, len(lats) - step, 2 * step) so arrows
   #       don't share start/end points
   #       For each segment, compute du, dv, and speed
   speeds = []

   for i in range(0, len(lats) - step, 2 * step):
       du = lons[i + step] - lons[i]
       dv = lats[i + step] - lats[i]
       speed = math.sqrt(du ** 2 + dv ** 2)
       speeds.append(speed)

   # TODO: Normalize speeds using mcolors.Normalize and get a
   #       colormap using cm.get_cmap("viridis")
   norm = mcolors.Normalize(vmin = min(speeds), vmax = max(speeds))
   cmap = plt.get_cmap("viridis")

   # TODO: Draw each arrow using mpatches.FancyArrowPatch
   #        Set arrowstyle, linewidth, color from colormap
   index = 0
   for i in range(0, len(lats) - step, 2 * step):
       start = (lons[i], lats[i])
       end = (lons[i + step], lats[i + step])

       arrow = mpatches.FancyArrowPatch(
           start,
           end,
           arrowstyle = "- >",
           mutation_scale = 25,
           linewidth = 2,
           color = cmap(norm(speeds[index]))
       )
       axis.add_patch(arrow)
       index += 1

   # TODO: Add a colorbar using cm.ScalarMappable
   scalmap = cm.ScalarMappable(norm=norm, cmap=cmap)
   scalmap.set_array([])
   cbar = plt.colorbar(scalmap, ax=axis, shrink=0.85)
   cbar.set_label("Step magnitude (deg) - proxy for wind speed")

   # TODO: Set axis labels, title, aspect ratio, and grid
   axis.set_xlabel("Longitude")
   axis.set_ylabel("Latitude")
   axis.set_title(f"{title} (step={step}, ~{len(speeds)} arrows)", fontsize = 10)
   axis.grid(True, linestyle = "--", alpha = 0.4)

   lon_min, lon_max = min(lons), max(lons)
   lat_min, lat_max = min(lats), max(lats)

   lon_pad = (lon_max - lon_min) * 0.08
   lat_pad = (lat_max - lat_min) * 0.12

   axis.set_xlim(lon_min - lon_pad, lon_max + lon_pad)
   axis.set_ylim(lat_min - lat_pad, lat_max + lat_pad)

   # TODO: Save the figure using plt.savefig()
   plt.tight_layout()
   plt.savefig(out_path)
   plt.close()


def main():
   """
   Main function that loads GPS data and generates the wind map.
   """
   # Load GPS data from the provided CSV file
   times, lats, lons = load_gps("gps_data.csv")

   # Generate wind direction map
   plot_wind_map(
       lats,
       lons,
       step=10,
       title="Wind Direction Map",
       out_path="wind_map.png",
   )


if __name__ == "__main__":
    main()