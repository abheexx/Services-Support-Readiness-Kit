# Handling SFTP Connectivity Issues with Firewalls

**Last Updated:** December 2024  
**Author:** Single Family Technology Services Team  
**Category:** File Transfer Support  
**Tags:** SFTP, Firewall, Connectivity, File Transfer, Network

---

## Overview

This guide addresses common SFTP connectivity issues encountered when transferring files through Fannie Mae's secure file transfer infrastructure, particularly those related to firewall configurations and network connectivity.

## Common SFTP Connectivity Issues

### Connection Timeouts

**Symptoms:**
- SFTP client hangs during connection attempt
- "Connection timed out" error messages
- Intermittent connection failures

**Root Causes:**
1. Firewall blocking SFTP port (22)
2. Network routing issues
3. Incorrect SFTP server hostname/IP
4. VPN or proxy configuration problems

**Troubleshooting Steps:**

1. **Verify SFTP Server Details**
   ```
   Hostname: sftp.fanniemae.com
   Port: 22 (default SFTP port)
   Protocol: SFTP over SSH
   Test Command: telnet sftp.fanniemae.com 22
   ```

2. **Check Firewall Configuration**
   ```
   Outbound Port: 22 (SSH/SFTP)
   Protocol: TCP
   Direction: Outbound from client to server
   Action: Allow (not block)
   ```

3. **Test Network Connectivity**
   ```
   Ping Test: ping sftp.fanniemae.com
   Port Test: telnet sftp.fanniemae.com 22
   Traceroute: traceroute sftp.fanniemae.com
   ```

### Authentication Failures

**Symptoms:**
- "Permission denied" errors
- "Authentication failed" messages
- Key-based authentication issues

**Troubleshooting Steps:**

1. **Verify Credentials**
   ```
   Username: Check with account administrator
   Password: Ensure correct case sensitivity
   Key File: Verify SSH key format and permissions
   ```

2. **Check SSH Key Configuration**
   ```
   Key Format: OpenSSH format (id_rsa, id_ed25519)
   Permissions: 600 for private key, 644 for public key
   Location: ~/.ssh/ directory
   ```

3. **Test Authentication Methods**
   ```
   Password Auth: sftp -o PreferredAuthentications=password user@sftp.fanniemae.com
   Key Auth: sftp -i ~/.ssh/id_rsa user@sftp.fanniemae.com
   ```

### File Transfer Errors

**Symptoms:**
- "Permission denied" during file upload/download
- "No such file or directory" errors
- Transfer interruptions

**Troubleshooting Steps:**

1. **Verify Directory Permissions**
   ```
   Check: User has read/write access to target directory
   Validate: Directory exists and is accessible
   Confirm: File permissions allow transfer
   ```

2. **Check File Size Limits**
   ```
   Maximum File Size: 2GB per file
   Maximum Directory Size: 10GB total
   Action: Split large files if necessary
   ```

3. **Validate File Naming**
   ```
   Avoid: Special characters, spaces, non-ASCII
   Use: Alphanumeric, hyphens, underscores
   Length: Maximum 255 characters
   ```

## Network Configuration Requirements

### Firewall Rules

**Required Outbound Rules:**
```
Port 22 (SSH/SFTP): TCP outbound to sftp.fanniemae.com
Port 443 (HTTPS): TCP outbound to api.fanniemae.com
Port 80 (HTTP): TCP outbound to api.fanniemae.com (redirects)
```

**Required Inbound Rules:**
```
Port 22: TCP inbound from Fannie Mae IP ranges
Port 443: TCP inbound from Fannie Mae IP ranges
```

### IP Address Whitelisting

**Fannie Mae IP Ranges:**
```
Primary: 198.51.100.0/24
Secondary: 203.0.113.0/24
Backup: 192.0.2.0/24
```

**Client IP Requirements:**
- Static IP address recommended
- IP must be whitelisted with Fannie Mae
- Contact support to add new IP addresses

## SFTP Client Configuration

### Command Line SFTP

**Basic Connection:**
```bash
sftp username@sftp.fanniemae.com
```

**With Key Authentication:**
```bash
sftp -i ~/.ssh/id_rsa username@sftp.fanniemae.com
```

**Batch Operations:**
```bash
sftp -b commands.txt username@sftp.fanniemae.com
```

### GUI SFTP Clients

**Recommended Clients:**
- WinSCP (Windows)
- FileZilla (Cross-platform)
- Cyberduck (Mac/Windows)

**Connection Settings:**
```
Protocol: SFTP
Host: sftp.fanniemae.com
Port: 22
Username: [your_username]
Authentication: Password or Key
```

## Troubleshooting Commands

### Network Diagnostics

```bash
# Test connectivity
ping sftp.fanniemae.com

# Test port accessibility
telnet sftp.fanniemae.com 22

# Trace network path
traceroute sftp.fanniemae.com

# Check DNS resolution
nslookup sftp.fanniemae.com
```

### SFTP Diagnostics

```bash
# Verbose connection test
sftp -v username@sftp.fanniemae.com

# Test with specific cipher
sftp -c aes256-ctr username@sftp.fanniemae.com

# Check supported algorithms
ssh -Q cipher sftp.fanniemae.com
```

## Common Error Messages and Solutions

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "Connection refused" | Port 22 blocked | Check firewall rules |
| "Host key verification failed" | Unknown host key | Add to known_hosts file |
| "Permission denied" | Invalid credentials | Verify username/password |
| "No such file or directory" | Wrong path | Check directory structure |
| "Connection timed out" | Network issue | Check connectivity and firewall |

## Escalation Procedures

**Level 1 Support:**
- Verify basic connectivity and credentials
- Check firewall configuration
- Test with different SFTP client

**Level 2 Support:**
- Review network logs and routing
- Check server-side firewall rules
- Validate user permissions and quotas

**Level 3 Support:**
- Deep dive into network infrastructure
- Coordinate with network operations team
- Review security policy changes

## Related Documentation

- [API Gateway Troubleshooting](api-gateway-troubleshooting.md)
- [RCA Process Guide](rca-process-guide.md)
- [ServiceNow Ticket Management](servicenow-ticket-management.md)

## Contact Information

**Primary Support:** Single Family Technology Services  
**Email:** sf-tech-support@fanniemae.com  
**Phone:** 1-800-FANNIE-1 (ext. 1234)  
**Hours:** Monday-Friday, 8:00 AM - 6:00 PM ET

---

*This article is part of the Single Family Technology Services Knowledge Base*
