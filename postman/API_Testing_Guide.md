# Fannie Mae API Testing Guide

## Overview
This guide explains how to use the Postman collection for testing Fannie Mae Single Family APIs and troubleshooting common issues.

## Collection Structure

### REST APIs
- **Authentication**: Login endpoints with valid/invalid credential testing
- **Single Family Data APIs**: Loan data retrieval with various error scenarios
- **API Gateway Health Checks**: Gateway monitoring and timeout testing

### SOAP APIs
- **Loan Processing Service**: SOAP-based loan processing with schema validation

## Pre-configured Test Scenarios

### 1. Authentication Tests
- **Valid Authentication**: Tests successful login and token retrieval
- **401 Unauthorized**: Tests invalid credentials handling
- **Response Time Validation**: Ensures authentication completes within 5 seconds

### 2. API Error Handling
- **403 Forbidden**: Tests insufficient permissions with invalid tokens
- **500 Internal Server Error**: Tests server error handling and response structure
- **Schema Validation**: Tests SOAP request validation and fault handling

### 3. Performance Testing
- **Response Time Monitoring**: Tracks API response times
- **Timeout Testing**: Tests gateway timeout scenarios (30+ seconds)
- **Health Check Validation**: Monitors API gateway availability

## Environment Variables

Set these variables in your Postman environment:

```json
{
  "base_url": "https://api.fanniemae.com",
  "soap_base_url": "https://services.fanniemae.com",
  "username": "your_fannie_mae_username",
  "password": "your_fannie_mae_password",
  "loan_id": "123456789"
}
```

## Troubleshooting Common Issues

### 401 Unauthorized Errors
1. Verify username/password in environment variables
2. Check if account is locked or expired
3. Validate API endpoint URL is correct
4. Ensure proper authentication headers are set

### 403 Forbidden Errors
1. Verify access token is valid and not expired
2. Check user permissions for the requested resource
3. Validate API key has correct scopes
4. Ensure proper authorization headers

### 500 Internal Server Error
1. Check server logs for detailed error information
2. Verify request payload format and required fields
3. Test with different data sets to isolate the issue
4. Check API gateway configuration

### SOAP Schema Validation Errors
1. Verify XML structure matches WSDL specification
2. Check required fields are present and properly formatted
3. Validate SOAP envelope structure
4. Ensure proper namespaces are declared

### Timeout Issues
1. Check network connectivity and firewall settings
2. Verify API gateway timeout configurations
3. Test with smaller payloads to isolate performance issues
4. Check for rate limiting or throttling

## Running the Collection

1. Import the `Fannie_Mae_API_Runbook.json` file into Postman
2. Set up environment variables
3. Run individual requests or the entire collection
4. Review test results in the Test Results tab
5. Use the Console for detailed debugging information

## Best Practices

- Always run health checks before testing business logic
- Use environment variables for sensitive data
- Monitor response times and set appropriate thresholds
- Test both positive and negative scenarios
- Document any custom test modifications
- Regularly update the collection with new endpoints

## Integration with Fannie Mae Support

These tests directly map to common Fannie Mae partner API issues:

- **Authentication failures** → Check partner credentials and account status
- **Permission errors** → Validate partner access levels and API subscriptions
- **Server errors** → Escalate to backend team with detailed error logs
- **Timeout issues** → Check network connectivity and API gateway health
- **Schema validation** → Verify partner integration follows API specifications

---
*For additional support, contact the Single Family Technology Services team*
