"""Clean the Uber bookings data and print a few useful summaries."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "Dataset" / "ncr_ride_bookings.csv"


def load_and_clean(path: Path) -> pd.DataFrame:
    """Read the CSV and convert the fields used by the analysis."""
    data = pd.read_csv(path, na_values=["null", "", " "])

    text_columns = data.select_dtypes(include="object").columns
    for column in text_columns:
        data[column] = data[column].str.strip().str.strip('"')

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Time"] = pd.to_datetime(data["Time"], format="%H:%M:%S", errors="coerce").dt.time

    numeric_columns = [
        "Avg VTAT",
        "Avg CTAT",
        "Booking Value",
        "Ride Distance",
        "Driver Ratings",
        "Customer Rating",
    ]
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors="coerce")

    data["Month"] = data["Date"].dt.to_period("M").astype("string")
    data["Hour"] = pd.to_datetime(data["Time"].astype("string"), format="%H:%M:%S", errors="coerce").dt.hour
    data["Is Completed"] = data["Booking Status"].eq("Completed")
    data["Is Cancelled"] = data["Booking Status"].str.startswith("Cancelled", na=False)

    return data


def summarize(data: pd.DataFrame) -> None:
    """Print the main counts and a few breakdowns."""
    status_counts = data["Booking Status"].value_counts().sort_index()
    completed = data.loc[data["Is Completed"]]
    cancelled = data.loc[data["Is Cancelled"]]

    print("Dataset overview")
    print(f"Rows: {len(data):,}")
    print(f"Columns: {len(data.columns):,}")
    print(f"Date range: {data['Date'].min().date()} to {data['Date'].max().date()}")
    print(f"Duplicate booking IDs: {data['Booking ID'].duplicated().sum():,}")
    print(f"Missing-value rate: {data.isna().mean().mean():.2%}")

    print("\nBooking status")
    print(status_counts.to_string())

    print("\nHeadline metrics")
    print(f"Completed rides: {len(completed):,} ({len(completed) / len(data):.2%})")
    print(f"Cancelled rides: {len(cancelled):,} ({len(cancelled) / len(data):.2%})")
    print(
        "Customer cancellations: "
        f"{status_counts.get('Cancelled by Customer', 0):,} "
        f"({status_counts.get('Cancelled by Customer', 0) / len(data):.2%})"
    )
    print(
        "Driver cancellations: "
        f"{status_counts.get('Cancelled by Driver', 0):,} "
        f"({status_counts.get('Cancelled by Driver', 0) / len(data):.2%})"
    )
    print(f"Completed booking value: {completed['Booking Value'].sum():,.0f}")
    print(f"Average completed booking value: {completed['Booking Value'].mean():,.2f}")

    print("\nCompleted rides by month")
    print(completed.groupby("Month").size().to_string())

    print("\nCompleted rides by vehicle type")
    vehicle_summary = completed.groupby("Vehicle Type").agg(
        rides=("Booking ID", "size"),
        booking_value=("Booking Value", "sum"),
        average_distance_km=("Ride Distance", "mean"),
        average_customer_rating=("Customer Rating", "mean"),
    )
    print(vehicle_summary.sort_values("rides", ascending=False).round(2).to_string())

    print("\nCancellation reasons")
    customer_reasons = data["Reason for cancelling by Customer"].dropna().value_counts()
    driver_reasons = data["Driver Cancellation Reason"].dropna().value_counts()
    print("Customer:\n" + customer_reasons.to_string())
    print("Driver:\n" + driver_reasons.to_string())


if __name__ == "__main__":
    summarize(load_and_clean(DATA_PATH))
