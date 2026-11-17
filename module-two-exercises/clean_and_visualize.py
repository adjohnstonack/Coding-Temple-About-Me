import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

messy = pd.DataFrame({
    "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                "Widget A", " Widget C", "Widget D", None, "Widget A"],
    "sales": ["150", "200", "175", "300", "200",
              "180", "250", "abc", "100", "-50"],
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03",
             "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
    "region": ["North", "South", "north", "East", "South",
               "West", "east", "North", "South", "West"],
})

print("Original data:")
print(messy)

#clean product names
messy["product"] = (messy["product"] .str.strip() .str.title())


#clean region names
messy["region"] = (messy["region"] .str.strip() .str.title())

#covert sales to numeric
messy["sales"] = pd.to_numeric(messy["sales"],errors="coerce")

#convert date column
messy["date"] = pd.to_datetime(messy["date"])

#remove missing products
messy = messy.dropna(subset=["product"])

#remove negative sales
messy = messy[messy["sales"]>=0]

#remove duplicates
messy = messy.drop_duplicates()

print("\nCleaned Data:")
print(messy)

#ANALYSIS

#total salesby product
sales_by_product = (messy.groupby("product")["sales"] .sum() .sort_values(ascending=False))
print("\nSales by Product:")
print(sales_by_product)

#daily sales trend
daily_sales =(messy.groupby("date")["sales"] .sum())
print("\nDaily Sales:")
print(daily_sales)

#create visualizations
fig, axes = plt.subplots(
    3,
    1,
    figsize=(10, 15)
)

#bar chart
sales_by_product.plot(
    kind="bar",
    ax=axes[0],
    color="skyblue"
)

axes[0].set_title(
    "Total Sales by Product"
)
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Sales")

#line chart
daily_sales.plot(
    kind="line",
    marker="o",
    ax=axes[1],
    color="green"
)

axes[1].set_title(
    "Daily Sales Trend"
)

axes[1].set_xlabel("Date")
axes[1].set_ylabel("Sales")

#histogram
axes[2].hist(
    messy["sales"],
    bins=5,
    color="orange",
    edgecolor="black"
)

axes[2].set_title(
    "Sales Distribution"
)

axes[2].set_xlabel("Sales")
axes[2].set_ylabel("Frequency")

#FINAL LAYOUT

plt.tight_layout()

#SAVE PNG

plt.savefig(
    "sales_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nVisualization saved as:")
print("sales_dashboard.png")