#!/usr/bin/env python3
"""
ServiceNow Ticket Analysis Script
Generates summary statistics and visualizations for ticket data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

def load_ticket_data(csv_file):
    """Load and preprocess ticket data from CSV"""
    df = pd.read_csv(csv_file)
    df['Created_Date'] = pd.to_datetime(df['Created_Date'])
    return df

def generate_summary_stats(df):
    """Generate summary statistics for ticket data"""
    print("=== SERVICENOW TICKET ANALYSIS SUMMARY ===\n")
    
    # Basic metrics
    total_tickets = len(df)
    resolved_tickets = len(df[df['Status'].isin(['Resolved', 'Closed'])])
    avg_resolution_time = df['Resolution_Time_Hours'].mean()
    
    print(f"Total Tickets: {total_tickets}")
    print(f"Resolved Tickets: {resolved_tickets}")
    print(f"Resolution Rate: {(resolved_tickets/total_tickets)*100:.1f}%")
    print(f"Average Resolution Time: {avg_resolution_time:.2f} hours")
    print(f"Median Resolution Time: {df['Resolution_Time_Hours'].median():.2f} hours\n")
    
    # Backlog analysis
    backlog_tickets = len(df[df['Status'].isin(['New', 'In Progress', 'Escalated'])])
    print(f"Current Backlog: {backlog_tickets} tickets")
    print(f"Backlog Percentage: {(backlog_tickets/total_tickets)*100:.1f}%\n")
    
    # Category analysis
    print("=== TOP ERROR CATEGORIES ===")
    category_counts = df['Category'].value_counts()
    for category, count in category_counts.head(5).items():
        percentage = (count/total_tickets)*100
        print(f"{category}: {count} tickets ({percentage:.1f}%)")
    
    print("\n=== SEVERITY DISTRIBUTION ===")
    severity_counts = df['Severity'].value_counts()
    for severity, count in severity_counts.items():
        percentage = (count/total_tickets)*100
        print(f"{severity}: {count} tickets ({percentage:.1f}%)")
    
    print("\n=== RESOLUTION TIME BY SEVERITY ===")
    severity_resolution = df.groupby('Severity')['Resolution_Time_Hours'].agg(['mean', 'median', 'count'])
    for severity in ['P1', 'P2', 'P3', 'P4']:
        if severity in severity_resolution.index:
            mean_time = severity_resolution.loc[severity, 'mean']
            median_time = severity_resolution.loc[severity, 'median']
            count = severity_resolution.loc[severity, 'count']
            print(f"{severity}: {count} tickets, Avg: {mean_time:.2f}h, Median: {median_time:.2f}h")

def create_visualizations(df):
    """Create visualizations for ticket data"""
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('ServiceNow Ticket Analysis Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Tickets by Category
    category_counts = df['Category'].value_counts()
    axes[0, 0].pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%')
    axes[0, 0].set_title('Tickets by Category')
    
    # 2. Resolution Time by Severity
    severity_data = df.groupby('Severity')['Resolution_Time_Hours'].mean()
    axes[0, 1].bar(severity_data.index, severity_data.values, color=['red', 'orange', 'yellow', 'green'])
    axes[0, 1].set_title('Average Resolution Time by Severity')
    axes[0, 1].set_ylabel('Hours')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # 3. Status Distribution
    status_counts = df['Status'].value_counts()
    axes[1, 0].bar(status_counts.index, status_counts.values, color='skyblue')
    axes[1, 0].set_title('Tickets by Status')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # 4. Resolution Time Distribution
    axes[1, 1].hist(df['Resolution_Time_Hours'], bins=20, color='lightcoral', alpha=0.7)
    axes[1, 1].set_title('Resolution Time Distribution')
    axes[1, 1].set_xlabel('Hours')
    axes[1, 1].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig('/Users/abheeshtavemuri/Kit/data-analysis/ticket_analysis_dashboard.png', dpi=300, bbox_inches='tight')
    print("\nDashboard saved as: ticket_analysis_dashboard.png")

def generate_excel_report(df):
    """Generate Excel report with pivot tables"""
    with pd.ExcelWriter('/Users/abheeshtavemuri/Kit/data-analysis/ticket_analysis_report.xlsx', engine='openpyxl') as writer:
        # Summary sheet
        summary_data = {
            'Metric': ['Total Tickets', 'Resolved Tickets', 'Backlog Tickets', 'Avg Resolution Time (hrs)', 'Median Resolution Time (hrs)'],
            'Value': [
                len(df),
                len(df[df['Status'].isin(['Resolved', 'Closed'])]),
                len(df[df['Status'].isin(['New', 'In Progress', 'Escalated'])]),
                round(df['Resolution_Time_Hours'].mean(), 2),
                round(df['Resolution_Time_Hours'].median(), 2)
            ]
        }
        pd.DataFrame(summary_data).to_excel(writer, sheet_name='Summary', index=False)
        
        # Category analysis
        category_analysis = df.groupby('Category').agg({
            'Resolution_Time_Hours': ['count', 'mean', 'median'],
            'Severity': lambda x: x.value_counts().to_dict()
        }).round(2)
        category_analysis.to_excel(writer, sheet_name='Category_Analysis')
        
        # Severity analysis
        severity_analysis = df.groupby('Severity').agg({
            'Resolution_Time_Hours': ['count', 'mean', 'median'],
            'Status': lambda x: x.value_counts().to_dict()
        }).round(2)
        severity_analysis.to_excel(writer, sheet_name='Severity_Analysis')
        
        # Raw data
        df.to_excel(writer, sheet_name='Raw_Data', index=False)
    
    print("Excel report saved as: ticket_analysis_report.xlsx")

def main():
    """Main analysis function"""
    try:
        # Load data
        df = load_ticket_data('/Users/abheeshtavemuri/Kit/data-analysis/servicenow_tickets.csv')
        
        # Generate summary statistics
        generate_summary_stats(df)
        
        # Create visualizations
        create_visualizations(df)
        
        # Generate Excel report
        generate_excel_report(df)
        
        print("\n=== ANALYSIS COMPLETE ===")
        print("Files generated:")
        print("- ticket_analysis_dashboard.png")
        print("- ticket_analysis_report.xlsx")
        
    except FileNotFoundError:
        print("Error: servicenow_tickets.csv not found. Please ensure the file exists.")
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()
