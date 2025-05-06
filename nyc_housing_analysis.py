from sodapy import Socrata
import pandas as pd
import numpy as np

client = Socrata("data.cityofnewyork.us", "KSH9p9FmEU0UEiS7RA4C1D2qR")

query = "received_date >= '2023-01-01T00:00:00' AND received_date <= 
'2024-12-12T23:59:59'"
raw_data = client.get("ygpa-z7cr", where=query, limit=2000)

df = pd.DataFrame.from_records(raw_data)
df.drop_duplicates(inplace=True)

df.rename(columns={
    "received_date": "date_received",
    "complaint_status": "status",
    "complaint_status_date": "status_date",
    "problem_status": "problem_status",
    "problem_status_date": "problem_date"
}, inplace=True)

df["date_received"] = pd.to_datetime(df["date_received"], errors="coerce")
df["status_date"] = pd.to_datetime(df["status_date"], errors="coerce")
df.dropna(subset=["date_received", "status_date"], inplace=True)

df["time_to_close"] = (df["status_date"] - df["date_received"]).dt.days
df["month"] = df["date_received"].dt.month
df["day_of_week"] = df["date_received"].dt.day_name()

print("Top Issues by Borough:")
print(df.groupby("borough")["major_category"].value_counts())

print("\nTop Issues by Zip Code:")
print(df.groupby("post_code")["major_category"].value_counts())

print("\nMonthly Complaint Distribution:")
print(df["month"].value_counts())

print("\nComplaints by Weekday:")
print(df["day_of_week"].value_counts())

print("\nViolation Frequency:")
print(df["problem_code"].value_counts())

print("\nComplaint Type Summary:")
print(df.groupby("type")["major_category"].value_counts())

print("\nAvg Time to Close by Year:")
print(df.groupby(df["date_received"].dt.year)["time_to_close"].mean())

selected_cols = ["date_received", "status", "borough", "major_category", 
"minor_category", "problem_status", "problem_code", "post_code", "type", 
"time_to_close"]
df[selected_cols].to_csv("cleaned_data.csv", index=False)
print("\n✔️ File saved as cleaned_data.csv")


