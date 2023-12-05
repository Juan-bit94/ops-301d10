# Authentication, Authorization and Accounting
## Why this topic matters
- This topic matters because as a cybersecurity and IT professional, knowing about the AAA framework is essential for allowing proper access to network resources. 

- The topic is also important because RADIUS servers are used hand in hand with AAA framework, therefore, knowing about RADIUS will enable individuals in the IT space to be more marketable.   
## Explain each of the three A’s as you would to a non-technical family member. Use an analogy or a story.
- Here is how I would explain the three A's to a family member.
  - Authentication: The process by which it can be identified that the user, that wants access, is valid. So I would tell a family member that authentication is like going to the bank, in order to access your bank account you need to know the PIN to your debit card. If you do not have the correct PIN, you may not access your account that way.
  
  - Authorization: It provides capabilities to enforce policies on network resources after the user has gained access to the network resources through authentication. I would explain it to my family members as so, just like the bank example, once you access your account after verifying who you are, the bank will only give you access to accounts that you own. You will not have access to other people's bank account because you are not authorized (aka not allowed).
  
  - Accounting: It provides a means of monitoring and capturing the events done by the user while accessing the network resources. I would tell my family members that accounting means that the actions you did are recorded. So if you take money out on Monday and deposits money Fridays, all that is recorded in the bank records.  
## What should the administrator do if the ACS server fails to authenticate a user during AAA implementation?
- If an ACS server fails to authenticate, the administrator should mention using the local database of the device as a backup, in the method list, to implement AAA.
## What is the role of the NAS in the AAA implementation using an ACS server? Use a diagram.
- Within the scope of AAA and ACS, the network access server facilitates communications between end devices (such as user devices) and the ACS server. Essentially, the NAS is responsible for controlling access to the network based on authentication and authorization decisions made by the ACS server.
- Diagram: ![image](https://github.com/Juan-bit94/ops-301d10/assets/77375345/1dbff3f1-8b40-42a1-b685-a98efb635fa8)
## What are the benefits of using RADIUS for authentication and authorization?
- The remote authentication dail-in user service (RADIUS) is a protocol used for centralized AAA services. There are many benefits such as scalability, security, centralized authentication and authorization to name a few.
## What is RADIUS and what does it stand for?
- RADIUS stands for remote authentication dail in user service and it is a client-server protocol and software that enables remote access servers to communicate with a central server to authenticate dial-in users and authorize their access to the requested system or service. 
## Research: What encryption algorithms does RADIUS use?
- RADIUS uses transport layer security and often implements the following:
  - Message Digest Algorithm: This includes message digest algorithm 5 (MD5) or secure hash algorithm 1 (SHA-1). While MD5 is common, SHA-1 is considered more secure and is recommended for stronger cryptographic protection.
  - Transport layer security (TLS): Some RADIUS implements TLS to encrypt the entire communication channel between the RADIUS client and server. TLS provides a higher level of security by encrypting the data in transit.
  - Advanced Encryption Standard (AES): Recently, RADIUS has been using AES for encryption. AES is a widely accepted symmetric encryption algorithm, providing strong security and performance.   
## What I want to know more about.
- I would like to know how scalability is implemented with RADIUS. Its been said that RADIUS is suitable for both small and large networks, so it would be cool to see how it scales up.
- I am interested to learn more about RADIUS dynamic authorization and in what situation should you implement this configuration?
- I would like to know how stable open source implementations of RADIUS server such as FreeRADIUS.
