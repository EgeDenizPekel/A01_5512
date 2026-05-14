# A01 - California Housing Boxplot

Generates a boxplot of median house values from the California Housing dataset and saves it as a PNG figure.

## Data

California Housing dataset from `scikit-learn` (`fetch_california_housing`). No manual download needed - the library fetches it automatically.

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

From the repo root, run:

```bash
python src/boxplot.py
```

## Expected output

A file saved at `figs/boxplot.png` showing the distribution of `MedHouseVal` (median house value in $100,000s) across California districts.
