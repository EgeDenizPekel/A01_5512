from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import pandas as pd

housing = fetch_california_housing(as_frame=True)
df = housing.frame

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(df["MedHouseVal"], vert=True, patch_artist=True,
           boxprops=dict(facecolor="steelblue", color="navy"),
           medianprops=dict(color="red", linewidth=2))

ax.set_title("California Housing - Median House Value Distribution")
ax.set_ylabel("Median House Value ($100,000s)")
ax.set_xticklabels(["MedHouseVal"])

plt.tight_layout()
plt.savefig("figs/boxplot.png", dpi=150)
print("Saved figs/boxplot.png")
