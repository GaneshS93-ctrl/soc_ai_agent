# Log analyzer Guide

## Purpose

This guide helps to analyze cyber security logs. A strong cybersecurity log analysis is built around understanding attack behaviors, log sources, indicators of compromise (IOCs), detection logic, and investigation workflows

## Common logs

### log 1: Brute-Force Attack Detection

Symptoms:

* Attacker attempts many passwords until one succeeds.
* Authentication Failures Spike
   -  Multiple failed logins
   -  Same username
   -  Same source IP
   -  Short time window

Resolution:

1. Disable the account to prevent further attack
2. Block the originating ip address.
3. Block IOCs.

### log 2: Password spraying

Symptoms:

*  Instead of logging in with one username and different passwords
   the attacker logs with multiple usernames with same password
*  Observe for Many usernames from same IP address in small interval    

Resolution:
1. Block the originating ip address.
2. Block IOCs.


### log 3: Distributed Brute Force

Symptoms:

*  Attack spread across many IPs
   -  Same account targeted
   -  logins from Numerous countries
   -  logins from multiple IP addresses
*  Observe for same usernames from multiple IP addresses and multiple locations
*  Observe for more than 10 login failures within 5 min.    

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.
3. Block hashes

### log 4: Privilege Escalation

Symptoms:

*  Attacker gains higher permissions.
*  Vertical Escalation - User -> Administrator permissions
*  Horizontal Escalation - User A -> User B permissions.
*  Observe for special privileges like debug privilege.
*  Observe for special privileges like set backup privilege.
*  Observe for unknown machine login.
*  Group membership changes.
*  Observe for creating of services or run daemons.
*  Observe for creating of services or run daemons.

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.
3. Block hashes
4. Disable user account
4. Time-limit admin rights
5. Remove Unnecessary Privileges
6. Block persistence mechanisms

### log 5: Suspicious Login Pattern

Symptoms:

*  Observe for logins from multiple locations simultaneously.
*  Observe for logins from different device IDs.
*  Observe for login from unknown country.
*  Observe for login during odd hours.
*  Observe for multiple concurrent sessions.
*  Observe for MFA (Multi Factor Authentication) anomalies.
*  Observe for inactive account be used to login.

Resolution:
1. Disable user account
2. Block IOCs.
3. Block hashes

### log 6: Lateral Movement Detection

Symptoms:

*  Observe for logins move between multiple hosts and systems after compromise.
*  Observe for Remote Service Creation.
*  Observe for Remote Desktop login.
*  Observe for WMI Execution.
*  Observe for PowerShell remote executions with encoded commands.
*  Observe for SMB Enumerations like net view by the user.

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.

### log 7: Persistence Detection

Symptoms:

*  Observe for multiple tasks scheduled in short span.
*  Observe for access and modification of registry files.
*  Observe for unexpected services being run.

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.

### log 8: Reconnaissance Detection

Symptoms:

*  Attackers gather information before moving.
*  Observe for running account enumeration commands like net user, whoami, quser.
*  Observe for running domain enumeration commands like nltest, dsquery.
*  Observe for running network enumeration commands like "arp -a", ipconfig, netstat, "ping sweep".

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.


### log 9: Malware and Execution Detection

Symptoms:

*  Observe for suspicious process chains like winword.exe -> powershell.exe -> cmd.exe
*  Observe for running encoded powershell.
*  Observe for suspicious process like certutil.exe, rundll32.exe, regsvr32.exe, mshta.exe, bitsadmin.exe.
*  Observe for suspicious process like bitsadmin.exe or wmic.exe.

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.

### log 10: Data Exfiltration Detection

Symptoms:

*  Observe for large data transfers
*  Observe for unusual large uploads to Dropbox, Google drive, OneDrive.
*  Observe for archive creations like 7zip, rar, tar before transfers.
*  Observe for long DNS queries or high DNS volume.

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.

### log 11: Ransomware Detection

Symptoms:

*  Observe for mass file modifications
*  Observe for run of encryption tools like cipher.exe or openssl.
*  Observe for network share encryption.

Resolution:
1. Block the incoming IP addresses
2. Block IOCs.

