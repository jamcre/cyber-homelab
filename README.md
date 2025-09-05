# Cybersecurity Homelab

This repository documents my journey building a cybersecurity homelab on a repurposed 2015 HP Pavilion All-in-One. The goal is to gain hands-on experience with new tools and technologies in a controlled, self-hosted environment!

## 🌐 Current Lab Services

| Service                                | Type          | Purpose                                           |
| :------------------------------------- | :------------ | :------------------------------------------------ |
| [Proxmox VE](https://www.proxmox.com/) | Hypervisor    | Host platform for virtual machines and containers |
| [Pi-hole](https://pi-hole.net/)        | LXC Container | Network-wide DNS sinkhole and ad-blocker          |

## 🗺️ Roadmap

- [x] Hardware upgrades (SSD + RAM)
- [x] Proxmox VE installation & network configuration
- [x] Deploy Pi-hole in an LXC container
- [ ] TBD...

## 📁 Repository Layout

```
cyber-homelab
├── docs/ # Detailed walkthroughs per phase
├── diagrams/ # Network and architecture diagrams
├── logs/ # Example output and metrics (e.g., Pi-hole logs)
└── README.md
```

## 💼 Portfolio Value

This homelab demonstrates my practical ability to:

- **Repurpose and optimize legacy hardware** into a modern lab environment.
- **Troubleshoot issues** related to BIOS, bootloaders, and networking.
- **Deploy and manage infrastructure** using virtualization and containerization (Proxmox, LXC).
- **Implement defensive security measures**, such as DNS sinkholing for network-wide ad-blocking and malware protection.
- **Document technical processes** clearly for knowledge sharing and reproducibility.
