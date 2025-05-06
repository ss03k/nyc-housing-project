# How to Run This Project

To run this project: 
Clone the repo and navigate into the folder:
git clone https://github.com/ss03k/nyc-housing-project.git
cd nyc-housing-project

2. Install the required Python packages:
pip install pandas numpy sodapy

3. Run the Python script:
python nyc_housing_analysis.py

The script will generate a file called `cleaned_data.csv` with the analysis results.
# NYC Housing Complaint Analysis/ 
Goal
- This project analyzes New York City's 311 housing complains using open data from the NYC Open Data portal.
- The goal of this project is to identify patterns in NYC housing complaints and use data to support stricter landlord accountability policies. By highlighting issues like heating and plumbing failures, the goal is to drive data-informed solutions that improve tenant living condition and reduce delays in addressing violations.
# What it Does 
- Pulls complaint data from January 2023 to December 2024 using the Socrata API
- Cleans and structures the data using pandas
- Analyzes patterns by borough, zip code, category, and time
- Calculates average time to close complaints
- Outputs data to a CVS file
# Tech Used
- Python
- Pandas
- NumPy
- Sodapy(Socrata API)
- NYC Open Data
# Results
- Bronx and Brooklyn have the most complaints
- No head/ hot water is the most reported issue
- Complaints rates spike duting winter, especially January
- The average time to close a complaint is approximately 20 days
  
