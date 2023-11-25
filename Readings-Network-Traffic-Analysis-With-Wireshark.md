# Network Traffic Analysis with Wireshark
## Why this topic matters
- This topic matters because OSI is the foundation of networking. This framwork is what allows devices to communicate with each other locally and remotely. In addition, knowing about wireshark will be an introduction to the various tools that IT professionals will use in order to troubleshoot and keep devices secured. 
 1. What does "OSI' stand for?
    - OSI stands for Open Systems Interconnection   
 2. List the 7 layers of the OSI model and what each one is responsible for.
    - Application layer
    - Presentation layer
    - Session layer
    - Transport layer
    - Network layer
    - Data link layer
    - Physical layer
 3. Distinguish which layers are the "hardware layers", and which layers are the "software layers". What does that even mean?
    - The hardware layers of the OSI model are the following: Physical layer, Data link layer.
    - The software layers of the OSI model are the following: Application layer, Presentation layer, Session layer.
    - Hardware layers are focused on the physical aspects of communication, the lower part of the Data Link Layer (MAC sub-layer) is involved in managing hardware addresses and access to the physical medium. All in all, both layers handle hardware-related aspects of network communication in the OSI model.
    - Software layers are responsible for managing and facilitating communication between software applications. The layers are focused on the aspect of network communication that involve software applications and the presentation of data. In the end, software layers are created to provide services to end-user applications and ensuring that data is presented, formatted, and communicated in a way that is effective for users. 
 4. How can the OSI model be used in troubleshooting?
    - The OSI model can be used in troubleshooting because the model provides a structured framework for understanding and addressing network issues. If a user is aware of the layers, then they can analyze each layer to identify and isolate the problem. 
# How to use Wireshark
1. What is Wireshark?
    - Wireshark is a network protocol analyzer, an application that captures packets from a network connection. 
2. What is a packet?
    - A packet is the name given to a discrete unit of data in a typical Ethernet network.
3. What 3 high-level things does Wireshark accomplish? How could these be used for nefarious purposes? For benevolent purposes?
    - Packet capture:
        - Wireshark can be used for bad purposes within the wrong hands. For example, it can be used in man-in-the-middle attacks, a hacker can use wireshark to capture and analyze traffic passing through. It can also be used for network reconnaissance to map out a network and identify hosts.
        - For good intentions, an IT professional can use wireshark for network troubleshooting in order to diagnose network issues. In addition, wireshark can be used for forensic investigations, it provides a detailed record for network activities helping investigators reconstruct events of the breach. 
    - Filtering:
        - For filtering, hackers can use wireshark for bad purposes such as surveillance. Filters can be employed to monitor and intercept communication, such as capturing sensitive data without the knowledge or consent.
        - For good intentions, an IT professional can use wireshark for network performance optimization. It professionals can ensure that critical applications and services receive sufficient bandwidth and resources for optimal performance.  
    - Visualization:
        - For visualization, a hacker can use it to manipulate data. A hacker can use visualization to forge graphical representations of data, leading to msinformation, confusion, or exploitation fo vulnerabilities.
        -  It professionals can use visualization tools such as wireshark for the good of the company. In a proper context, visualization tools can be used for network monitoring and security analysis. Visualizations can be used to identify and respond to potential threats. 
## Things I want to know more about
- I would like to know about other tools beyond wireshark. Since I know that wireshark has its limitations, I would like to know what other tools I can use in an IT context. 
