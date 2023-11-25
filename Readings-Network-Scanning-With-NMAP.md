# Readings: Network scanning with NMAP
## Why this topic matters
- 
1. What is a port? Describe it with an analogy that would help a family member understand.
- A port is a virtual location where networking communication starts and ends. If I had to explaine it to a family member, I would tell them that a port is like a phone number or an address. It lets devices know who to communicate with. 
2. What does a port scanner send to a port to check the current status?
- A port scanner sends a network request to connect to a specific TCP or UDP port on a computer. The network request is a packet of network data that is sent to a port to check its current status.
3. When a port scanner sends a request to connect, what are the three possible responses? Describe them.
- When a port scanner sends a TCP or UDP network packet and asks the port about their current status. The three types of responses:
    - Open, Accepted: The computer responds and asks if there is anything it can do for you.
    - Closed, not listening: The computer responds that "This port is currently in use and unavailable at this time."
    - Filtered, Dropped, Blocked: The computer doesn't even bother to respond.  
4. What is the difference between TCP and UDP?
- TCP and UDP are the two most common protocols in use for Internet Protocol networks. The main difference is how they deliver information, TCP is more orderly with error checking, verification, and a 3 way handshake to confirm each packet is a success. UDP on the other hand is faster, but there is no error checking, and in effect UDP sends data but does not check to see if it was successful.
## Common Ports
1. List and describe the ports used for the following:
- Telnet:
- SSH:
- DNS:
- SMTP:
- HTTP:
- HTTPS:
- RDP:
- Ping:
