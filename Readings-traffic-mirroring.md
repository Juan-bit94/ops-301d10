# Traffic Mirroring
## Why this topic matters
- This topic matters because knowing about network monitoring methods such as SPAN and TAP will be useful for a future in IT and cybersecurity. Monitoring the network traffic is one of the main responsibilities and skills that employers look for.
## What are the differences between SPAN and TAP?
- In order to know the differences, we must define SPAN and TAP
- SPAN: This is port mirroring (also called roving analysis) is a method of monitoring network traffic which forwards a copy of each incoming and outgoing packet from one (or several) ports of a switch to another port where the analysis device is connected.
- TAP: A network terminal access point (TAP) is a hardware device which can passively capture traffic on a network. It is commonly used to monitor the traffic between two points in the network. The network TAP has a least three ports: A, B, and a monitor port. The TAP passes all traffic between the two network points and copies the traffic to its monitor port, thus enabling an analysis device to listen.
- As we can see, SPAN and TAP differ in their approach and the way they capture traffic to monitoring devices. One differences is that SPAN and TAP operate on different levels of the OSI layer, TAP operates at the physical level and SPAN on the data link layer. Also, SPAN copies network traffic based on port mirroring configurations on the switch, TAP does not rely on switch configurations but it physically duplicates the traffic.
## What types of network devices can support network traffic mirroring?
- There are various devices that can support network traffic mirroring. Ethernet switches are commonly used, some high end routers also support traffic mirroring, and virtual switches may support traffic mirroring depending on the environment and configurations.
## How can network traffic mirroring be used for network security?
- Network traffic mirroring has a significant impact with network security due to various functionality it provides. Mirroring plays a vital role in network security since it offers real-time visibility, assists in threat detection, and enables analysis of network activity.
- With the capability to duplicate and forward network traffic to a monitoring device, administrators can detect potential security threats. 
## Are there any legal or ethical considerations when using network traffic mirroring?
- There are various legal and ethical considerations when monitoring the network traffic of an organization.
- There are some privacy laws and regulations that govern the monitoring of network traffic. Organizations for example have to comply with the GDPR in Europe and the HIPAA in the United States, if a company does not comply with those laws they will be liable for a lawsuit.
- There is some ethics involved with employee consent. In some areas, employees may have an expectation of privacy regarding their communications, employers may need to obtain consent from employees before implementing network traffic mirroring.
## Things I want to know more about
- I would like to know how audits are conducted to make sure that companies are compliant with certain laws about network monitoring and data retention.
