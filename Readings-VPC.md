# Virtual Private Cloud (VPC)
## Why this topic matters
- Its important to be aware of the cloud computer offerings, since it may cut costs and improve efficiency.
## How can one host within a VPC any services that need to be public?
- Cloudflare can provide organizations a Virtual Private Cloud hosted within the public cloud. This isolates your data and network on Cloudflare's global network.
- You can configure network and security settings to have your services within your VPC to be accessed publicly.
-  Cloudflare documentation offers the most up to date detailed instructions on how to setup services to be accessed from outside the VPC.
## What are examples of services that would live in the publicly-accessible part of the VPC? The privately-accessible part?
- In a Cloudflare's VPC, a user can organize the services into publicly-accessible and privately-accessible parts based on their intended accessibility.
- Some services that would live in publicly-accessible are web servers, API endpoints, and content delivery networks to name a few.
- Some privately accessible services are database servers, internal APIs, and management interfaces to name a few.
## What are the trade-offs of using a VPC vs traditional infrastructure?
- The advantages of VPC are scalability, cost efficiency, and managed services.
- trade-offs of VPC are provider dependency, cost management complexity, and security and compliance concerns.
## Things I want to know more about
- I would like to know the level of responsibility I have and the provider has. I understand that in AWS for example, AWS is responsible for the underlying infrastructure for the virtualization. Clients are responsible for their data and how they use the tools depending on (SaaS or PaaS).
