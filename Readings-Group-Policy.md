# Group Policy
## Why this topic matter
- Group policy matters because it's fundamental for managing Windows based networks.
- Group policy helps with maintaining a secure, consistent, and efficient computing environment for users within an enterprise.
- Also group policy can help with troubleshooting by allowing admin to identify and address configuration issues centrally. 
## What role does Group Policy play in Windows Active Directory?
- In order to understand the role group policy plays in Windows Active Directory (AD) we need to know what a group policy is.
- Group policy is a feature of Windows that allows a wide variety of advanced settings that network administrators can use to control the working environment of users and computer accounts in AD.
- For AD, it provides a centralized place for administrators to manage and configure operating systems, applications, and user settings. 
## Name and describe different ways GPOs can benefit security.
- Here are different ways GPOs can benefit security
- 1. GPOs could be used to determine the home page that a user sees when they launch their internet browsers after logging into a domain, so users avoid sketchy sites.
  2. Administrators can use GPOs to define which network-connected printers appear on the list of available printers after a user in a specific AD OU logs into the domain. That way you do not connect to a device that may have malicious intent such as man in the middle.
  3. Admins can also use GPOs to tweak a number of security protocols and practices, such as restricting internet connection options, programs, and even screen time. So devices can be secured if they are off the internet or even restricted on the types of programs you can download and have. 
## How can the acronym “LSDOU” help you figure out which policies are in effect?
- LSDOU stands for local, site, domain, and organizational unit. The local computer policy is the first to be processed, followed by the rest, site and ect.
## Things I want to know more about
- I would like to know more about group policy best practices since I imagine there are SOPs addressing design and implementation.
- Also I want to know, since it's Windows based, if a user can use PowerShell commands to manage group policy.

