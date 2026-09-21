import csv
from collections import defaultdict

def read_sales_data(filename):
    sales = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["price"] = float(row["price"])
            sales.append(row)
    return sales

def analyze_sales(sales):
    total_revenue = 0
    revenue_per_product = defaultdict(float)
    quantity_per_product = defaultdict(int)
    revenue_per_day = defaultdict(float)

    for row in sales:
        revenue = row["quantity"] * row["price"]
        total_revenue += revenue

        product = row["product"]
        date = row["date"]

        revenue_per_product[product] += revenue
        quantity_per_product[product] += row["quantity"]
        revenue_per_day[date] += revenue

    # Find day with highest revenue
    best_day = max(revenue_per_day, key=revenue_per_day.get)

    return {
        "total_revenue": total_revenue,
        "revenue_per_product": revenue_per_product,
        "quantity_per_product": quantity_per_product,
        "best_day": best_day,
        "revenue_per_day": revenue_per_day
    }

def write_text_report(analysis, filename):
    with open(filename, "w") as file:
        file.write("=== Sales Report ===\n\n")
        file.write(f"Total Revenue: ${analysis['total_revenue']:.2f}\n\n")

        file.write("Revenue Per Product:\n")
        for product, revenue in analysis["revenue_per_product"].items():
            file.write(f"  {product}: ${revenue:.2f}\n")
        file.write("\n")

        file.write("Total Quantity Sold Per Product:\n")
        for product, qty in analysis["quantity_per_product"].items():
            file.write(f"  {product}: {qty}\n")
        file.write("\n")

        file.write(f"Day With Highest Revenue: {analysis['best_day']}\n")

def write_product_summary_csv(analysis, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["product", "total_quantity", "total_revenue"])

        for product in analysis["revenue_per_product"]:
            writer.writerow([
                product,
                analysis["quantity_per_product"][product],
                f"{analysis['revenue_per_product'][product]:.2f}"
            ])

def main():
    sales = read_sales_data("sales_data.csv")
    analysis = analyze_sales(sales)

    write_text_report(analysis, "sales_report.txt")
    write_product_summary_csv(analysis, "product_summary.csv")

    print("Reports generated: sales_report.txt, product_summary.csv")

if __name__ == "__main__":
    main()





