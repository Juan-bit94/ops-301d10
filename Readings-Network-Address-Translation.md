# Network Address Translation
## Why this topic matters
- Its important to know about NATs since they enable packets to traverse between the local network and the external networks (the internet).
- Its also important to know about NATS because they allow multiple devices within a private network to share a single public IP address, thereby conserving public IP addresses.
## What is the main purpose for implementing NAT on a network?
- The main purpose for implementing NAT on a network is to conserve public IP addresses.
- NAT provides many benefits to a network such as security, load balancing, and even IP version translation.
- With all theses positives though, NAT's main purposes is to avoid addresses running out, if no addresses are left in the IP pool configuration, then packets will be dropped and the ICMP host will notify the destination. 
## At what layer of the OSI model does NAT happen?
- NATs operates at the Network Layer, but its also known as the third layer of OSI.
- The reason it takes place at layer 3 is because NATs are used with IP addresses. 
## What happens to packets when NAT runs out of addresses in the pool of available IPs?
- The packets will be dropped and an Internet Control Message Protocol (ICMP) host unreachable packet to the destination is sent. 
## What disadvantage does using NAT pose for routers?
- Disadvantage of NAT are the following:
- Translation results in switching path delays.
- Certain applications will not function while NAT is enabled.
- Complicates tunneling protocols such as IPsec.
- Also, the router being a network layer device, should not tamper with port numbers (transport layer) but it has to do so because of NAT.
## Things I want to know more about
- I would like to know more about some of the NAT support features such as hairpinning, loopback, and NAT 3.
- Also I'd like to know if NATs can be used for logging and auditing.
