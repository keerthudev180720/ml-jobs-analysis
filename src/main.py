import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Load the CSV as-is
df = pd.read_csv("dataset/1000_ml_jobs_us.csv")

# Optional: Drop unnamed index column if present
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Check and display the available columns
print("Columns loaded:", df.columns.tolist())

# Convert job_posted_date to datetime safely
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'], errors='coerce')
df['month_posted'] = df['job_posted_date'].dt.to_period('M')

# Drop rows with missing values in key fields
df.dropna(subset=['company_name', 'job_title', 'seniority_level'], inplace=True)

# -------------------
# Plot 1: Top 10 Companies Hiring
top_companies = df['company_name'].value_counts().head(10).reset_index()
top_companies.columns = ['company_name', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=top_companies, x='company_name', y='count', palette='viridis')
plt.title("Top 10 Companies Hiring")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/top_companies.png")
plt.close()

# -------------------
# Plot 2: Top 5 Job Titles by Region
region_title_counts = (
    df.groupby(['company_address_region', 'job_title'])
      .size()
      .reset_index(name='count')
      .sort_values(['company_address_region', 'count'], ascending=[True, False])
)

top_titles_each_region = region_title_counts.groupby('company_address_region').head(5)

plt.figure(figsize=(14, 7))
sns.barplot(data=top_titles_each_region, x='company_address_region', y='count', hue='job_title')
plt.title("Top 5 Job Titles by Region")
plt.xticks(rotation=45)
plt.legend(title='Job Title', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("output/top_titles_by_region.png")
plt.close()

# -------------------
# Plot 3: Seniority Level Distribution
seniority_counts = df['seniority_level'].value_counts().reset_index()
seniority_counts.columns = ['seniority_level', 'count']

plt.figure(figsize=(8, 6))
sns.barplot(data=seniority_counts, x='seniority_level', y='count', palette='cubehelix')
plt.title("Distribution of Job Seniority Levels")
plt.xlabel("Seniority Level")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("output/seniority_distribution.png")
plt.close()

# -------------------
# Plot 4: Jobs Over Time
monthly_postings = df['month_posted'].value_counts().sort_index()

plt.figure(figsize=(12, 5))
monthly_postings.plot(kind='line', marker='o')
plt.title("ML Job Postings Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/jobs_over_time.png")
plt.close()

# -------------------
# Plot 5: Top Companies Hiring for Senior Roles
senior_roles = df[df['seniority_level'].str.contains("Senior|Lead|Director", case=False, na=False)]
top_senior_hiring = senior_roles['company_name'].value_counts().head(10).reset_index()
top_senior_hiring.columns = ['company_name', 'senior_job_count']

plt.figure(figsize=(10, 6))
sns.barplot(data=top_senior_hiring, x='company_name', y='senior_job_count', palette='magma')
plt.title("Top Companies Hiring for Senior-Level ML Roles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/top_senior_hiring.png")
plt.close()

print("✅ All plots saved to 'output/' folder.")