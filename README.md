# Cybersecurity Homelab

This repository documents my journey building a cybersecurity homelab on a repurposed 2015 HP Pavilion All-in-One. The project demonstrates hands-on experience with hardware, virtualization, networking, defensive security, and offensive security tools in a self-hosted environment.

---

## 🌐 Current Lab Services

| Service                                             | Type          | Purpose                                           | IP Address   |
| :-------------------------------------------------- | :------------ | :------------------------------------------------ | :----------- |
| [Proxmox VE](https://www.proxmox.com/)              | Hypervisor    | Host platform for virtual machines and containers | 192.168.0.50 |
| [Pi-hole](https://pi-hole.net/)                     | LXC Container | Network-wide DNS sinkhole and ad-blocker          | 192.168.0.53 |
| [Kali Linux](https://www.kali.org/)                 | VM            | Penetration testing "attack" machine              | DHCP         |
| [Ubuntu Server](https://ubuntu.com/download/server) | VM            | Intentionally vulnerable "target" machine         | DHCP         |

---

## 🗺️ Project Phases

| Phase | Title                             | Description                                                                        | Status      |
| :---- | :-------------------------------- | :--------------------------------------------------------------------------------- | :---------- |
| 1     | **Hardware Assessment & Upgrade** | Repurposed old hardware by upgrading to an SSD and 16GB RAM.                       | ✅ Complete |
| 2     | **Proxmox VE Installation**       | Installed the Proxmox hypervisor, troubleshooting UEFI/Legacy boot issues.         | ✅ Complete |
| 3     | **Network Services: Pi-hole**     | Deployed Pi-hole in an LXC container as a network-wide DNS filter.                 | ✅ Complete |
| 4     | **Building a Pentest Lab**        | Created Kali Linux (attacker) and Ubuntu Server (target) VMs for security testing. | ✅ Complete |
| 5     | _TBD_                             | _TBD_                                                                              | ⌛ Planned  |

---

## 📖 Phase Overview & Documentation

### Phase 1: Hardware Assessment & Upgrade

- **Objective:** Repurpose old hardware into a viable lab host.
- **Actions:** Assessed an HP Pavilion (2015), upgraded the HDD to a 1TB SSD, and added a second 8GB RAM stick for a total of 16GB DDR3L.
- **Evidence:** [Hardware Specs, Images, and Notes](./phase1-hardware)

### Phase 2: Proxmox VE Installation

- **Objective:** Install the Proxmox VE hypervisor.
- **Actions & Troubleshooting:**
  - **Issue 1:** USB drive not detected in boot menu. **Solution:** Disabled Secure Boot and enabled Legacy Support in BIOS.
  - **Issue 2:** Proxmox ISO failed to boot. **Solution:** Used Ventoy instead of Rufus/Etcher to handle the hybrid ISO correctly.
  - **Issue 3:** BIOS could not find the Proxmox boot drive post-installation. **Solution:** Re-enabled pure UEFI mode in BIOS.
- **Evidence:** [Installation Notes and Images](./phase2-proxmox-install)

### Phase 3: Network Configuration & Pi-hole Deployment

- **Objective**: Implement network-wide DNS filtering and ad-blocking.
- **Actions**:
  - Reserved static IP (192.168.0.50) for Proxmox host
  - Created Debian 12 LXC container with Pi-hole resources (1 core, 512MB RAM, 8GB storage)
  - Reserved static IP (192.168.0.53) for Pi-hole container
  - Installed and configured Pi-hole.
  - Configured router to use Pi-hole as primary DNS server, with cloudflare as a backup DNS.
  - Monitored DNS queries for network activity analysis
- **Evidence:** [Pi-hole Configuration and Setup](./phase3-pihole-deployment)

### Phase 4: Building a Penetration Testing Lab

- **Objective:** Create a self-contained environment for practicing security assessment techniques.
- **Actions:**
  - **Attack Machine:** Built a Kali Linux VM for offensive security tools.
  - **Target Machine:** Built an Ubuntu Server VM and installed the Damn Vulnerable Web Application (DVWA).
- **Testing:** Performed network reconnaissance (`nmap`) and vulnerability scanning (`nikto`) from the Kali VM against the target.
- **Evidence:** [Lab Setup, Configuration, and Scan Results](./phase4-pentest-lab)

---

## 💼 Demonstrated Skills

- **Hardware Proficiency**: Hardware assessment, upgrading, and optimization
- **Troubleshooting**: BIOS/UEFI configuration, bootloader issues, hardware compatibility
- **Virtualization**: Proxmox VE deployment, LXC containers, KVM virtual machines
- **Networking**: Static IP configuration, DNS management, network services
- **Defensive Security:** Implement defensive measures like DNS sinkholing (Pi-hole) for network-wide ad-blocking and malware protection.
- **Offensive Security:** Set up a penetration testing lab and perform initial reconnaissance and vulnerability scanning with tools like `nmap` and `nikto`.
- **Documentation**: Detailed process documentation and problem-solving analysis

---

## 📁 Repository Structure

```
cyber-homelab/
├── phase1-hardware/           # Hardware specifications and upgrade documentation
├── phase2-proxmox-install/    # Proxmox installation notes and troubleshooting
├── phase3-pihole-deployment/  # Pi-hole configuration and setup
├── phase4-pentest-lab/        # Kali & Ubuntu VM setup + security testing results
├── docs/                      # Network and architecture diagrams & documents
├── images/                    # Pictures and screenshots
└── README.md
```

---

_This lab is a work in progress. Check back for updates!_
