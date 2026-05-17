# Lab Conventions

Reference document for IPs and CT/VM ID conventions. All assignments in my homenet/homelab will try to follow these rules.

---

## Thought Process

**Low number = higher importance.**

Priority-Based Addressing:

- Static (.1–.99): Core infrastructure and fixed nodes.
- Dynamic (.100–.254): Transient/DHCP clients.

---

## IP & VLAN Schema

| Range       | Category               | Notes                                              |
| :---------- | :--------------------- | :------------------------------------------------- |
| .1          | Gateway                | Router interface for this VLAN                     |
| .2 — .9     | Network infrastructure | Switches, APs, managed network devices             |
| .10 — .19   | Physical nodes         | Servers, workstations, laptops (Physical machines) |
| .20 — .49   | LXC containers         | Lightweight containers (Proxmox)                   |
| .50 — .74   | Virtual machines       | Full VMs (Proxmox)                                 |
| .75 — .99   | Reserved               | Future expansion (aka idk yet)                     |
| .100 — .254 | DHCP pool              | All dynamic clients (phones, tablets, etc.)        |

---

## VLAN Assignments

| VLAN | Name    | Subnet          | Purpose                                            |
| :--- | :------ | :-------------- | :------------------------------------------------- |
| 10   | Trusted | 192.168.10.0/24 | Personal devices (Phones, PC)                      |
| 20   | Lab     | 192.168.20.0/24 | Homelab infrastructure (Servers, VMs, LXCs)        |
| 30   | IoT     | 192.168.30.0/24 | Smart home devices (Fridge, Robo-Vacuum, AC units) |
| 40   | Cams    | 192.168.40.0/24 | Surveillance (NVR/cameras)                         |

The same structure applies to every VLAN. Once you know the pattern, easy to determine what's what.

---

## Proxmox CT/VM ID Convention

**Format:** [Category][Deployment Order] (eg: 101, -> LXC container, 2nd deployed)

| ID Range | Category              | Examples                         |
| :------- | :---------------- | :------------------------------- |
| 1XX      | Core Infrastructure     | Pi-hole, NPM, Homepage           |
| 2XX      | Applications & Self-hosted Services       | Jellyfin, Crafty, Ghost, web apps               |
| 3XX      | Monitoring & Security   | Wazuh, Grafana, Prometheus, SOC tooling         |
| 4XX      | Network & System Infrastructure| TrueNAS, Proxmox Backup Server, utility VMs |
| 5XX      | Development & Lab      | Kali, targets, scratch boxes     |
| 9XX      | Templates & Base Images         | Base images, reusable installs   |

---

_Follow this document when adding any new device, container, or VM to the lab._
