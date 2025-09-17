# Troubleshooting 401/403 API Gateway Errors

**Last Updated:** December 2024  
**Author:** Single Family Technology Services Team  
**Category:** API Support  
**Tags:** API Gateway, Authentication, Authorization, 401, 403

---

## Overview

This article provides step-by-step troubleshooting procedures for common 401 Unauthorized and 403 Forbidden errors encountered with Fannie Mae Single Family APIs through the API Gateway.

## Common Error Scenarios

### 401 Unauthorized Errors

**Symptoms:**
- HTTP 401 status code
- "Unauthorized" or "Invalid credentials" error messages
- Authentication failures in API calls

**Root Causes:**
1. Invalid or expired API credentials
2. Missing or malformed authentication headers
3. Account locked or suspended
4. Incorrect API endpoint URL

**Troubleshooting Steps:**

1. **Verify Credentials**
   ```
   Check: Username and password are correct
   Action: Test with Postman collection authentication endpoint
   Validation: Confirm 200 response with valid access token
   ```

2. **Check Authentication Headers**
   ```
   Required Header: Authorization: Bearer {access_token}
   Format: Must include "Bearer " prefix
   Case: Sensitive to case (Authorization, not authorization)
   ```

3. **Validate Token Expiration**
   ```
   Check: Token creation timestamp
   Default TTL: 1 hour for access tokens
   Action: Refresh token if expired
   ```

4. **Account Status Verification**
   ```
   Check: User account is active and not locked
   Verify: API subscription is current
   Confirm: No security policy violations
   ```

### 403 Forbidden Errors

**Symptoms:**
- HTTP 403 status code
- "Forbidden" or "Insufficient permissions" messages
- Valid authentication but denied access

**Root Causes:**
1. Insufficient API permissions or scopes
2. Resource-specific access restrictions
3. IP address not whitelisted
4. API rate limiting exceeded

**Troubleshooting Steps:**

1. **Verify API Permissions**
   ```
   Check: User has required API scopes
   Validate: Resource-specific permissions
   Confirm: API subscription includes requested endpoints
   ```

2. **Check IP Whitelisting**
   ```
   Verify: Client IP is in allowed range
   Check: Firewall rules permit API Gateway access
   Confirm: No VPN or proxy restrictions
   ```

3. **Review Rate Limiting**
   ```
   Check: API call frequency within limits
   Default: 1000 requests per hour per user
   Action: Implement exponential backoff if needed
   ```

## Quick Resolution Checklist

- [ ] Credentials are valid and not expired
- [ ] Authentication header format is correct
- [ ] User account is active and unlocked
- [ ] API subscription includes required endpoints
- [ ] Client IP is whitelisted
- [ ] Rate limits are not exceeded
- [ ] API endpoint URL is correct

## Escalation Procedures

**Level 1 Support:**
- Verify credentials and basic connectivity
- Check account status and permissions
- Validate request format and headers

**Level 2 Support:**
- Review API Gateway logs
- Check backend service health
- Validate security policy configurations

**Level 3 Support:**
- Deep dive into authentication service logs
- Review security policy changes
- Coordinate with platform team for infrastructure issues

## Related Documentation

- [API Authentication Guide](../postman/API_Testing_Guide.md)
- [ServiceNow Ticket Management](servicenow-ticket-management.md)
- [SFTP Firewall Connectivity](sftp-firewall-connectivity.md)

## Contact Information

**Primary Support:** Single Family Technology Services  
**Email:** sf-tech-support@fanniemae.com  
**Phone:** 1-800-FANNIE-1 (ext. 1234)  
**Hours:** Monday-Friday, 8:00 AM - 6:00 PM ET

---

*This article is part of the Single Family Technology Services Knowledge Base*
