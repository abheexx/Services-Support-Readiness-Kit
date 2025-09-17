# Jira Kanban Workflow Documentation

**Last Updated:** December 2024  
**Author:** Single Family Technology Services Team  
**Category:** Process Documentation  
**Tags:** Jira, Kanban, Workflow, Process Management, SDLC

---

## Overview

This document describes the Jira Kanban workflow designed specifically for Single Family Technology Services support operations. The workflow supports the complete ticket lifecycle from creation to closure, including Root Cause Analysis (RCA) and knowledge base updates.

## Workflow States

### 1. New
**Purpose:** Initial state for newly created tickets  
**Description:** Ticket has been created and is awaiting initial review and assignment  
**Key Actions:**
- Assign to appropriate team member
- Set priority and severity
- Add initial comments and context
- Start time tracking

**Entry Criteria:**
- Ticket created through ServiceNow integration
- Manual ticket creation by support team
- Escalated ticket from other teams

**Exit Criteria:**
- Ticket assigned to team member
- Priority and severity determined
- Initial assessment completed

### 2. In Progress
**Purpose:** Active work state for ticket resolution  
**Description:** Ticket is being actively worked on by assigned team member  
**Key Actions:**
- Investigate issue thoroughly
- Implement fixes or workarounds
- Communicate with users
- Update ticket with progress

**Entry Criteria:**
- Ticket assigned to team member
- Work has begun on resolution
- Returned from escalation

**Exit Criteria:**
- Issue resolved and ready for user confirmation
- Requires RCA due to recurring nature
- Needs escalation to higher level

### 3. RCA (Root Cause Analysis)
**Purpose:** Deep analysis of recurring or critical issues  
**Description:** Comprehensive analysis to identify root cause and prevent recurrence  
**Key Actions:**
- Conduct detailed investigation
- Analyze patterns and trends
- Identify contributing factors
- Develop prevention measures

**Entry Criteria:**
- Issue has occurred 3+ times in 30 days
- Critical or high-severity incident
- Management escalation request
- Complex technical issue

**Exit Criteria:**
- Root cause identified
- Prevention measures defined
- Analysis documented
- Ready for knowledge base update

### 4. KB Update (Knowledge Base Update)
**Purpose:** Documentation of resolution for future reference  
**Description:** Creating or updating knowledge base articles with resolution details  
**Key Actions:**
- Create new knowledge base article
- Update existing documentation
- Include troubleshooting steps
- Add prevention measures

**Entry Criteria:**
- RCA completed
- Resolution requires documentation
- New solution discovered
- Process improvement identified

**Exit Criteria:**
- Knowledge base article created/updated
- Documentation reviewed and approved
- Article linked to ticket
- Ready for resolution

### 5. Resolved
**Purpose:** Issue resolved, awaiting user confirmation  
**Description:** Ticket has been resolved and is waiting for user confirmation  
**Key Actions:**
- Notify user of resolution
- Provide resolution details
- Request user confirmation
- Monitor for recurrence

**Entry Criteria:**
- Issue has been fixed
- Workaround implemented
- User notified of resolution
- Resolution documented

**Exit Criteria:**
- User confirms resolution
- No further action required
- Ready for closure

### 6. Closed
**Purpose:** Final state for completed tickets  
**Description:** Ticket has been closed and archived  
**Key Actions:**
- Archive ticket data
- Update metrics and reporting
- Complete time tracking
- Final documentation

**Entry Criteria:**
- User confirmed resolution
- All documentation complete
- No further action required
- SLA compliance verified

**Exit Criteria:**
- Ticket archived
- Metrics updated
- Process complete

### 7. Escalated
**Purpose:** Tickets requiring higher level support  
**Description:** Ticket has been escalated to specialized teams or management  
**Key Actions:**
- Assign to escalation team
- Provide escalation context
- Monitor escalation progress
- Coordinate with escalation team

**Entry Criteria:**
- SLA breach imminent
- Complex technical issue
- Management escalation required
- Vendor support needed

**Exit Criteria:**
- Escalation team resolves issue
- Issue returned to original team
- Escalation context provided

## Transition Rules

### Automatic Transitions
1. **SLA Breach Escalation**
   - P1 tickets: Escalate after 4 hours in "In Progress"
   - P2 tickets: Escalate after 8 hours in "In Progress"
   - P3 tickets: Escalate after 24 hours in "In Progress"

2. **RCA Trigger**
   - Automatically transition to RCA when:
     - Same issue occurs 3+ times in 30 days
     - Critical severity incident
     - Management requests RCA

3. **KB Update Trigger**
   - Automatically transition to KB Update when:
     - Resolution type is "Fixed"
     - Category is API, File Transfer, or System Performance
     - New solution discovered

### Manual Transitions
- All transitions require appropriate permissions
- Required fields must be completed before transition
- Comments required for all transitions
- Time tracking automatically started/stopped

## Field Requirements

### Required Fields by State

**New:**
- Priority (P1-P4)
- Severity (Critical, High, Medium, Low)
- Category (API Issues, File Transfer, etc.)
- Description

**In Progress:**
- Assignee
- Time tracking started
- Regular progress updates

**RCA:**
- RCA Reason
- Investigation details
- Findings documentation

**KB Update:**
- KB Article Link
- Documentation details
- Review status

**Resolved:**
- Resolution details
- Resolution type
- User notification

**Escalated:**
- Escalation reason
- Escalation level
- Escalation team assignment

## SLA Compliance

### Response Times
- **P1 (Critical):** 1 hour response, 4 hour resolution
- **P2 (High):** 4 hour response, 8 hour resolution
- **P3 (Medium):** 8 hour response, 24 hour resolution
- **P4 (Low):** 24 hour response, 72 hour resolution

### Escalation Thresholds
- **Level 1:** SLA breach imminent
- **Level 2:** Multiple escalation attempts
- **Level 3:** Management involvement required
- **Level 4:** Vendor support needed

## Integration Points

### ServiceNow Integration
- Automatic ticket creation from ServiceNow
- Status synchronization between systems
- Time tracking integration
- Escalation notification

### Confluence Integration
- Knowledge base article creation
- Documentation linking
- Process updates
- Training material updates

### Monitoring Integration
- Automatic ticket creation from alerts
- Status updates from system health
- Performance correlation
- Trend analysis

## Best Practices

### Ticket Management
- Update tickets at least daily
- Include detailed progress comments
- Use appropriate priority levels
- Follow escalation procedures

### Documentation
- Create knowledge base articles for common issues
- Update existing documentation regularly
- Include step-by-step procedures
- Add screenshots and examples

### Communication
- Notify users of status changes
- Provide clear resolution details
- Escalate appropriately and timely
- Document all actions taken

### Quality Assurance
- Review resolved tickets for completeness
- Verify knowledge base updates
- Check SLA compliance
- Monitor escalation patterns

## Reporting and Analytics

### Key Metrics
- Average resolution time by priority
- SLA compliance rate
- Escalation frequency
- Knowledge base article creation rate
- Team performance metrics

### Dashboards
- Real-time ticket status
- SLA compliance monitoring
- Team workload distribution
- Trend analysis and forecasting

### Reports
- Daily ticket summary
- Weekly team performance
- Monthly SLA compliance
- Quarterly process improvement

## Troubleshooting

### Common Issues
- **Tickets stuck in state:** Check required fields and permissions
- **SLA breaches:** Review escalation procedures and team capacity
- **Missing transitions:** Verify workflow configuration and user permissions
- **Integration failures:** Check API connections and data mapping

### Support Resources
- Jira Administrator
- Single Family Technology Services Team
- Process Improvement Team
- IT Support

## Related Documentation

- [ServiceNow Ticket Management](../knowledge-base/servicenow-ticket-management.md)
- [RCA Process Guide](../knowledge-base/rca-process-guide.md)
- [API Gateway Troubleshooting](../knowledge-base/api-gateway-troubleshooting.md)

## Contact Information

**Primary Support:** Single Family Technology Services  
**Email:** sf-tech-support@fanniemae.com  
**Phone:** 1-800-FANNIE-1 (ext. 1234)  
**Hours:** Monday-Friday, 8:00 AM - 6:00 PM ET

---

*This article is part of the Single Family Technology Services Knowledge Base*
