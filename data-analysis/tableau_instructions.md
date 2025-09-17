# Tableau Dashboard Setup Instructions

**Last Updated:** December 2024  
**Author:** Single Family Technology Services Team  
**Category:** Analytics and Reporting  
**Tags:** Tableau, Dashboard, ServiceNow, Analytics, Reporting

---

## Overview

This guide provides step-by-step instructions for creating Tableau dashboards using the ServiceNow ticket data CSV file. The dashboard will provide real-time insights into ticket trends, resolution times, and team performance.

## Data Source Setup

### 1. Connect to CSV Data
```
1. Open Tableau Desktop
2. Click "Connect to Data" → "Text file"
3. Navigate to: /data-analysis/servicenow_tickets.csv
4. Click "Open"
5. Verify data preview shows all columns correctly
```

### 2. Data Preparation
```
Required Fields:
- Ticket_ID (String)
- Category (String)
- Severity (String)
- Priority (String)
- Status (String)
- Resolution_Time_Hours (Number)
- Created_Date (Date)
- Assignment_Group (Number)
- Assigned_To (String)
- Platform (String)
```

## Dashboard Creation

### Dashboard 1: Executive Summary

**Layout:**
- 2x2 grid layout
- Filters: Date range, Category, Severity

**Visualizations:**

1. **Total Tickets KPI**
   ```
   Calculation: COUNT([Ticket_ID])
   Format: Number with comma separator
   Color: Blue
   ```

2. **Average Resolution Time KPI**
   ```
   Calculation: AVG([Resolution_Time_Hours])
   Format: Number with 2 decimal places
   Color: Green (if < 24), Orange (if 24-48), Red (if > 48)
   ```

3. **Backlog Count KPI**
   ```
   Calculation: COUNT(IF [Status] IN ['New', 'In Progress', 'Escalated'] THEN [Ticket_ID] END)
   Format: Number with comma separator
   Color: Red
   ```

4. **Resolution Rate KPI**
   ```
   Calculation: COUNT(IF [Status] IN ['Resolved', 'Closed'] THEN [Ticket_ID] END) / COUNT([Ticket_ID])
   Format: Percentage with 1 decimal place
   Color: Green (if > 90%), Orange (if 80-90%), Red (if < 80%)
   ```

### Dashboard 2: Category Analysis

**Layout:**
- 1x3 grid layout

**Visualizations:**

1. **Tickets by Category (Pie Chart)**
   ```
   Rows: Category
   Columns: COUNT([Ticket_ID])
   Chart Type: Pie
   Color: Category (automatic)
   ```

2. **Resolution Time by Category (Bar Chart)**
   ```
   Rows: Category
   Columns: AVG([Resolution_Time_Hours])
   Chart Type: Horizontal Bar
   Color: AVG([Resolution_Time_Hours]) (gradient)
   ```

3. **Category Trend Over Time (Line Chart)**
   ```
   Rows: COUNT([Ticket_ID])
   Columns: Created_Date (Month)
   Color: Category
   Chart Type: Line
   ```

### Dashboard 3: Severity Analysis

**Layout:**
- 2x2 grid layout

**Visualizations:**

1. **Severity Distribution (Donut Chart)**
   ```
   Rows: Severity
   Columns: COUNT([Ticket_ID])
   Chart Type: Donut
   Color: Severity (P1=Red, P2=Orange, P3=Yellow, P4=Green)
   ```

2. **Resolution Time by Severity (Box Plot)**
   ```
   Rows: Resolution_Time_Hours
   Columns: Severity
   Chart Type: Box Plot
   Color: Severity
   ```

3. **SLA Compliance by Severity (Gauge)**
   ```
   Calculation: COUNT(IF [Severity] = 'P1' AND [Resolution_Time_Hours] <= 4 THEN [Ticket_ID] END) / COUNT(IF [Severity] = 'P1' THEN [Ticket_ID] END)
   Format: Percentage
   Chart Type: Gauge
   Range: 0-100%
   ```

4. **Severity Trend (Area Chart)**
   ```
   Rows: COUNT([Ticket_ID])
   Columns: Created_Date (Week)
   Color: Severity
   Chart Type: Area
   ```

### Dashboard 4: Team Performance

**Layout:**
- 1x3 grid layout

**Visualizations:**

1. **Tickets by Assignment Group (Bar Chart)**
   ```
   Rows: Assignment_Group
   Columns: COUNT([Ticket_ID])
   Chart Type: Horizontal Bar
   Color: AVG([Resolution_Time_Hours]) (gradient)
   ```

2. **Resolution Time by Assigned To (Scatter Plot)**
   ```
   Rows: AVG([Resolution_Time_Hours])
   Columns: COUNT([Ticket_ID])
   Color: Severity
   Size: COUNT([Ticket_ID])
   Chart Type: Scatter Plot
   ```

3. **Team Workload (Heatmap)**
   ```
   Rows: Assigned_To
   Columns: Created_Date (Day of Week)
   Color: COUNT([Ticket_ID])
   Chart Type: Heatmap
   ```

## Advanced Calculations

### Custom Fields

1. **SLA Status**
   ```
   IF [Severity] = 'P1' AND [Resolution_Time_Hours] <= 4 THEN 'Met'
   ELSEIF [Severity] = 'P2' AND [Resolution_Time_Hours] <= 8 THEN 'Met'
   ELSEIF [Severity] = 'P3' AND [Resolution_Time_Hours] <= 24 THEN 'Met'
   ELSEIF [Severity] = 'P4' AND [Resolution_Time_Hours] <= 72 THEN 'Met'
   ELSE 'Missed'
   END
   ```

2. **Age in Days**
   ```
   DATEDIFF('day', [Created_Date], TODAY())
   ```

3. **Resolution Time Category**
   ```
   IF [Resolution_Time_Hours] <= 4 THEN '0-4 Hours'
   ELSEIF [Resolution_Time_Hours] <= 24 THEN '4-24 Hours'
   ELSEIF [Resolution_Time_Hours] <= 72 THEN '1-3 Days'
   ELSE '3+ Days'
   END
   ```

## Filters and Parameters

### Global Filters
- **Date Range**: Created_Date
- **Category**: Category
- **Severity**: Severity
- **Status**: Status
- **Assignment Group**: Assignment_Group

### Parameters
- **SLA Threshold**: Numeric parameter for custom SLA limits
- **Date Granularity**: List parameter (Day, Week, Month, Quarter)

## Dashboard Actions

### Filter Actions
- Click on category in pie chart to filter other visualizations
- Click on severity to show detailed breakdown
- Click on date to show trend analysis

### Highlight Actions
- Hover over bars to highlight related data
- Click on data points to show detailed information

## Publishing and Sharing

### Tableau Server/Online
1. Save workbook as .twbx file
2. Upload to Tableau Server/Online
3. Set permissions for Single Family Technology Services team
4. Schedule data refresh (daily)
5. Create subscriptions for key stakeholders

### Export Options
- **PDF**: For executive reports
- **Image**: For presentations
- **Data**: For further analysis
- **Web**: For embedding in web pages

## Best Practices

### Performance Optimization
- Use data extracts instead of live connections
- Limit data to last 12 months for better performance
- Use calculated fields sparingly
- Optimize filters and parameters

### Design Guidelines
- Use consistent color schemes
- Include clear titles and labels
- Add tooltips with relevant information
- Ensure mobile responsiveness

### Maintenance
- Update data connections regularly
- Review and update calculations quarterly
- Gather user feedback for improvements
- Document dashboard changes

## Troubleshooting

### Common Issues
- **Data not refreshing**: Check data source connections
- **Calculations not working**: Verify field types and syntax
- **Performance issues**: Use data extracts and optimize filters
- **Visualization errors**: Check for null values and data types

### Support Resources
- Tableau Community Forums
- Tableau Knowledge Base
- Single Family Technology Services Team
- Tableau Administrator

## Related Documentation

- [ServiceNow Ticket Management](../knowledge-base/servicenow-ticket-management.md)
- [RCA Process Guide](../knowledge-base/rca-process-guide.md)
- [Python Analysis Script](ticket_analysis.py)

## Contact Information

**Primary Support:** Single Family Technology Services  
**Email:** sf-tech-support@fanniemae.com  
**Phone:** 1-800-FANNIE-1 (ext. 1234)  
**Hours:** Monday-Friday, 8:00 AM - 6:00 PM ET

---

*This article is part of the Single Family Technology Services Knowledge Base*
