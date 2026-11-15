
import csv
import random
from pathlib import Path

# Make the dataset reproducible.
# The same seed generates the same dataset every time.
random.seed(42)

# Define sample locations.
locations = ["Hyderabad", "Bangalore", "Chennai", "Pune", "Mumbai"]

# Output CSV file.
output_file = Path("data/raw/house_prices.csv")
output_file.parent.mkdir(parents=True, exist_ok=True)

# Generate 1,000 sample house records.
with output_file.open("w", newline="") as csvfile:
    fieldnames = [
        "area_sqft",
        "bedrooms",
        "bathrooms",
        "age_years",
        "location",
        "price",
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(1000):
        area = random.randint(500, 4000)
        bedrooms = random.randint(1, 5)
        bathrooms = random.randint(1, 4)
        age = random.randint(0, 30)
        location = random.choice(locations)

        # Sample price calculation in Indian rupees.
        location_factor = {
            "Hyderabad": 1.0,
            "Bangalore": 1.2,
            "Chennai": 1.1,
            "Pune": 1.05,
            "Mumbai": 1.5,
        }

        price = (
            area * 5000 * location_factor[location]
            + bedrooms * 150000
            + bathrooms * 100000
            - age * 20000
            + random.randint(-200000, 200000)
        )

        writer.writerow({
            "area_sqft": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "age_years": age,
            "location": location,
            "price": max(500000, round(price)),
        })

print(f"Dataset successfully generated: {output_file}")
print("Total records: 1000")
