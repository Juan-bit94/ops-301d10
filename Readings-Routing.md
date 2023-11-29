## Why this topic matters
- This topic matters because in VirtualBox knowing about the routing and router settings is crucial for proper networking communication between vms, the host machine, and the internet.
- Having a proper routing configuration ensures that network packets are sent to the correct destination, which is important in any business setting. 
## Routing
1. Which network mode in VirtualBox can be used to emulate unplugging the Ethernet cable from the network?
- The network mode in VirtualBox can be used to emulate unplugging the Ethernet cabel is not attached.
2. Which network mode would be best if you wanted to run a server on a VM that could be fully accessible from your physical local area network?
- A bridged adapter mode can be used to run servers on VMs that must be fully accessible from a physical local area network. 
3. What are the three options of promiscuous mode and what does each do?
- Deny: Any traffic that is not intended to the virtual network adapter of the VM is hidden from the VM. This option is set by default.
- Allow VMs: All traffic is hidden from the VM network adapter except the traffic transmitted to and from other VMs.
- Allow All: There are no restrictions in this mode. A VM network adapter can see all incoming and outgoing traffic. 
4. What is Port Forwarding?
- Port forwarding is a process of intercepting traffic addressed to the appropriate IP address and port in addition to redirecting that traffic to a different IP address and or port.
## Things I want to know more about.
- I would like to know more about port forwarding, specifically, I want to know what specific services would a business want to expose on the external network. In addition, I would like to know how port forwarding is configured, I tired to do it on one of my VMs, but I don't think it worked properly. 
