# Network Segmentation
## Why this topic matter
-
1. What is CIDR notation? a CIDR block?
- A CIDR notation is a way of representing a CIDR block, which is a range of IP addresses.
2. How many octets are found in an IPv4 address?
- An IPv4 address is represented as four 8-bit decimal. 
3. Setting binary aside and using the decimal system, what is the range of numbers found in an octet?
- An 8-but number when represented in the decimal system as opposed to binary has a range of 0 - 255. 
4. What does the final digit after the "/" represent in an IPv4 address?
- In CIDR notation, the final digit after the "/" represents how many bits make up the mask in an IPv4 address? 
5. How many IP addresses are in the CIDR block 10.0.0.0/24?
- There are 256 IP addresses in the 10.0.0.0/24 CIDR block. The math works like this: 32-24 = 8. 2^8 = 256. That is how we find the amount of IP addresses we have available. 
## What is Network Segmentation and Why it Matters?
1. In your own words, describe network segmentation.
- Network segmentation is dividing a network into smaller segments. Kinda like islands, network segmentation are small isolated segments from a larger computer network. 
2. Network segmentation isn't important as long as the network is using a well configured firewall. Do you agree? Why or why not?
- I disagree, a well configured firewall and network segmentation are important to implement to secure a network. Both implementations server different purposes, and when used in combination will provide more security. These two components will prevent lateral movement, internal threat mitigation, and can be used in a defense in depth strategy. 
3. What is a screened subnet?
- This is a network architecture that provides an additional layer of security by using two firewalls to protect a network from an external threat. A firewall is placed between the internal network and the external network (internet), and another firewall is placed between a less secure network and the external network. 
4. Cameras, ID card scanners, locked doors and biometrics are just a few examples of what type of security?
- These implementations are used for physical security. Most of these examples are used to safeguard people, assets, and resources by controlling access to physical spaces and prevents unauthorized intrusion or damage. 
## Things I want to know more about
- I would like to know more about how CIDR notation information can be found. If I was an IT professional or a hacker, where would I look in order to see how the range of IP addresses are dispersed. Is there an application that contains the information such as a DHCP terminal, or is it written in documentation?
