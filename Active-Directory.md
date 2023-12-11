# Active Directory (AD)
## Why this topic matters
- As an IT professional it's important to understand AD since it serves as the backbone for centralized management, security, and user authentication.
## What exactly is “Active Directory” and are the key services it provides?
- Active Directory (AD) is Microsoft's directory and identity management service for Windows domain networks.
- AD offers a number of different directory services such as:
- 1. Active Directory Domain Services (AD DS)
  2. Active Directory Lightweight Directory Services (AD LDS)
  3. Active Directory Certificate Services (AD CS)
  4. Active Directory Federation Services (AD FS)
  5. Active Directory Rights MAnagement Services (AD RMS)
## What are the differences between a domain, forest, and tree in Active Directory?
- The main difference between a domain, tree, and forest in Active directory is scope.
- A domain is a collection of objects such as users and devices. These objects share the same AD database. A domain is identified by a DNS name, company.com for example.
- A tree is a collection of one or more domains with a namespace that have a common DNS root name. An example of this is marketing.company.com and sales.company.com.
- A forest is a collection of one or more trees that share a common schema, global catalog, and directory configuration. They typically serve as the security boundary for an enterprise network.
## How can objects (e.g. users, devices) within a domain be grouped?
- Objects can be grouped into organizational units (OUs) to simplify administration and policy management.
- Administrators can create arbitrary organizational units to mirror functional, geographical, or business structures, and then apply group policies to OUs to simplify administration.
## Explain the benefits of Active Directory, as you would to a family member.
- I would tell a family member that Active Directory benefits are many, it keeps things organized by keeping track of everyone who uses the computer and what they can do. You also do not have to remember multiple login information, it's essentially one key for all the rooms. Lastly I would say that AD acts as a remote control for the computer since AD lets you manage and change settings on the computer remotely.
## Things I want to know more about.
- I would like to know more about the backup and recovery aspects of AD. Since AD stores a lot of data such as objects, it might be interesting to know how to prepare for disaster recovery.
- I would also like to know what a standard AD topology looks like. 
