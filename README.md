# Uber Ride Bookings Dashboard

This project looks at 150,000 Uber bookings from 2024. The dashboard was built in Power BI to understand completed rides, cancellations, revenue, vehicle types, and ratings.

## 🎬 Project Showcase

<p align="center">
  <img src="Project%20Showcase/Dasboard.gif" alt="Dashboard Demo" width="600">
</p>

## Dashboard Overview

The dashboard covers booking patterns, vehicle performance, payment methods, cancellation reasons, and customer and driver ratings.

### Key Metrics Summary (2024)
- **Total Bookings**: 150K
- **Success Rate**: 62% (93K completed rides)
- **Cancellation Rate**: 25% (37.5K cancelled bookings)
- **Customer Cancellations**: 7% (10.5K)
- **Driver Cancellations**: 18% (27K)
- **Incomplete Rides**: 6% (9K)
- **No Driver Found**: 7% (10.5K)


## Questions Answered in Power BI

The report is split into five pages, each focused on a different operational question.

### 1. Overall Performance
- Ride volume over time, shown by month and day.
- Booking status breakdown for completed, cancelled, incomplete, and unassigned rides.

### 2. Vehicle Types
- Completed rides and distance by vehicle type.
- A comparison of the vehicle categories used in the dataset.

### 3. Revenue
- Booking value by payment method.
- The five customers with the highest total booking value.
- Daily ride-distance distribution.

### 4. Cancellations
- Reasons customers cancelled their bookings.
- Reasons drivers cancelled their bookings.

### 5. Ratings
- Average driver rating by vehicle type, between 4.23 and 4.24.
- Average customer rating by vehicle type, between 4.40 and 4.41.


## Vehicle Fleet Analysis

| Vehicle Type | Completed Rides | Avg Distance | Total Distance | Booking Value |
|--------------|-----------------|--------------|----------------|---------------|
| Auto         | 23,155          | 25.99 km     | 601.79K km     | 11.73M        |
| Go Mini      | 18,549          | 25.99 km     | 482.09K km     | 9.41M         |
| Go Sedan     | 16,676          | 25.98 km     | 433.20K km     | 8.54M         |
| Bike         | 14,034          | 26.00 km     | 364.87K km     | 7.14M         |
| Premier Sedan| 11,252          | 25.95 km     | 291.95K km     | 5.73M         |
| eBike        | 6,551           | 26.34 km     | 172.57K km     | 3.30M         |
| Uber XL      | 2,783           | 25.72 km     | 71.59K km      | 1.41M         |

The table reports completed rides only. `Total Distance` is shown in kilometers and `Booking Value` is the sum of completed booking values.


## Dashboard Findings

### 1. Overall Performance
- **Ride Volume Over Time**: Monthly trend analysis showing seasonal patterns
- **Booking Status Breakdown**: Pie chart visualization of booking outcomes
- Peak performance observed in July-August period
- Notable dip in February followed by steady growth

### 2. Vehicle Type Analysis
- Breakdown of all vehicle categories
- Completed rides, distance, and booking value by vehicle type
- Auto rickshaws leading in completed rides (23.16K)

### 3. Revenue Analytics
- **Revenue by Payment Method**: 
  - UPI: Highest revenue contributor (~2.0M)
  - Cash: Second highest (~1.1M)
  - Uber Wallet, Credit Card, Debit Card: Lower contributions
- **Top 5 Customers**: High-value customer identification
- **Daily Distance Distribution**: Consistent 6K-8K km range per day

### 4. Cancellation Analysis
#### Customer Cancellations (10.5K total)
- Wrong Address: 2,362
- Change of Plans: 2,353
- Driver is not moving towards pickup location: 2,335
- Driver asked to cancel: 2,295
- AC is not working: 1,155

#### Driver Cancellations (27K total)
- Customer related issue: 6,837
- The customer was coughing/sick: 6,751
- Personal & Car related issues: 6,726
- More than permitted people in there: 6,686

### 5. Rating System
#### Customer Ratings by Vehicle Type
- Consistent high ratings across all vehicle types: 4.40-4.41
- Go Sedan leading with 4.41 rating
- All other categories maintaining 4.40 rating

#### Driver Ratings by Vehicle Type
- Slightly lower than customer ratings: 4.23-4.24
- UberXL showing marginally higher driver satisfaction (4.24)
- Consistent performance across all vehicle categories


## 🔧 Data Schema

The dashboard is built using the following data columns:

```
- Date, Time
- Booking ID, Booking Status
- Customer ID, Vehicle Type
- Pickup Location, Drop Location
- Avg VTAT, Avg CTAT
- Cancelled Rides by Customer, Reason for cancelling by Customer
- Cancelled Rides by Driver, Driver Cancellation Reason
- Incomplete Rides, Incomplete Rides Reason
- Booking Value, Ride Distance
- Driver Ratings, Customer Rating
- Payment Method
```


## Visualizations

1. **Time Series Analysis**: Monthly ride volume trends
2. **Pie Charts**: Booking status and cancellation reason distributions
3. **Bar Charts**: Revenue by payment method, top customers
4. **Tables**: Vehicle type performance metrics
5. **Histograms**: Daily distance distribution patterns

## Running the Analysis Script

The Python script checks the figures used in this README and prints a few extra summaries.

```bash
pip install -r requirements.txt
python analysis/uber_analysis.py
```

It loads the CSV, converts dates and numeric columns, treats `null` as missing data, and groups the results by month, vehicle type, and cancellation reason.

## Data Quality

- The source contains 150,000 rows covering January 1 through December 30, 2024.
- There are 1,233 duplicate `Booking ID` values and an overall missing-value rate of approximately 30%.
- The vehicle table uses completed rides. The cancellation counts use all rows with the relevant cancellation status.


## Business Takeaways

### Strengths
- Strong customer satisfaction (4.40+ ratings)
- Diverse vehicle portfolio catering to different needs
- UPI adoption driving digital payments
- Consistent daily operations (6K-8K km coverage)

### Areas for Improvement
- 25% cancellation rate needs attention
- Driver satisfaction slightly lower than customer satisfaction
- Seasonal variations in ride volume
- Customer retention strategies for top spenders

<!-- 
<h2></h2>
<div align="center">
<strong>Thank you for exploring this dashboard! </strong>
<h3>If this project helped you, please consider giving it a ⭐️</h3>
</div> -->
