import unittest
import os
import pandas as pd


class TestMLJobPostings(unittest.TestCase):
    def setUp(self):
        # Common setup for all tests
        file_path = os.path.join('dataset', '1000_ml_jobs_us.csv')
        self.df = pd.read_csv(file_path)
        self.df['job_posted_date'] = pd.to_datetime(self.df['job_posted_date'], errors='coerce')

    def test_total_jobs(self):
        """Check total number of job records"""
        self.assertGreater(self.df.shape[0], 900)  # adjust as per your real dataset

    def test_unique_companies(self):
        """Check number of unique companies"""
        unique_companies = self.df['company_name'].nunique()
        self.assertGreater(unique_companies, 50)

    def test_top_company(self):
        """Check the most frequent company in postings"""
        top_company = self.df['company_name'].value_counts().idxmax()
        self.assertIsInstance(top_company, str)

    def test_region_distribution(self):
        """Check job distribution across regions"""
        region_counts = self.df['company_address_region'].value_counts().to_dict()
        self.assertTrue(all(isinstance(val, int) for val in region_counts.values()))

    def test_seniority_levels(self):
        """Check all jobs have valid seniority levels (non-null)"""
        null_count = self.df['seniority_level'].isnull().sum()
        self.assertLess(null_count, self.df.shape[0] // 2)

    def test_job_posting_date_range(self):
        """Check job dates are within valid range"""
        self.assertTrue(self.df['job_posted_date'].min().year >= 2000)
        self.assertTrue(self.df['job_posted_date'].max().year <= 2025)


if __name__ == '__main__':
    unittest.main()
