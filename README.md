# Cybersecurity Homelab — v2

This repository documents the second iteration of my cybersecurity homelab. Building on [v1](./v1/README.md), this version introduces a multi-node infrastructure, VLAN-segmented networking, and a more intentional service architecture.

---

## 🖥️ Hardware

| Hostname | Type    | Role                | OS                  | VLAN         | IP            |
| :------- | :------ | :------------------ | :------------------ | :----------- | :------------ |
| citadel  | Desktop | Primary Workstation | Windows 11 Home     | 10 — Trusted | 192.168.10.XX |
| pavilion | Desktop | Virtualization Host | Proxmox VE 8.4      | 20 — Lab     | 192.168.20.XX |
| annex    | Laptop  | Mobile Workstation  | macOS Sequoia       | 10 — Trusted | DHCP          |
| inspiron | Laptop  | Docker Host         | Ubuntu Server 24.04 | 20 — Lab     | 192.168.20.XX |

Full hardware specs: [`hardware/hardware-inventory.yaml`](./hardware/hardware-inventory.yaml)

---

## 🌐 Network

| VLAN | Name    | Subnet          | Purpose                |
| :--- | :------ | :-------------- | :--------------------- |
| 10   | Trusted | 192.168.10.0/24 | Personal devices       |
| 20   | Lab     | 192.168.20.0/24 | Homelab infrastructure |
| 30   | IoT     | 192.168.30.0/24 | Smart devices & NVR    |

VLAN segmentation is live and verified. Firewall enforces zone isolation — Trusted can reach Lab, Lab cannot reach Trusted, IoT is fully isolated from internal networks.

Full network design: [`network/README.md`](./network/network.md)

---

## ⚙️ Infrastructure

Proxmox VE running on pavilion as the core virtualization host.
Ubuntu Server running on inspiron as the Docker host for self-hosted services.

Full details: [`infrastructure/proxmox.md`](./infrastructure/proxmox.md) · [`infrastructure/inspiron.md`](./infrastructure/inspiron.md)

---

## ⚙️ Services

| Service             | Host           | Function                          |
| :------------------ | :------------- | :-------------------------------- |
| Pi-hole             | pavilion (LXC) | Network-wide DNS filtering        |
| Nginx Proxy Manager | pavilion (LXC) | Reverse proxy and SSL termination |
| Wazuh               | pavilion (VM)  | SIEM and endpoint detection       |
| Portainer           | inspiron       | Docker container management       |
| MySpeed             | pavilion (LXC) | Network speed testing             |
| Homarr              | pavilion (LXC) | Homelab dashboard and service hub |

Full details: [`services/pihole.md`](./services/pihole.md) · [`services/nginx.md`](./services/nginx.md) · [`services/wazuh.md`](./services/wazuh.md)

---

## 🔬 Security Lab

| Exercise               | Description                                                                                                      | Status      |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------- | :---------- |
| Custom Detection Rules | SSH brute force, Windows logon spike, unauthorized sudo — four custom Wazuh rules written, tested, and validated | ✅ Complete |

Full write-up: [`lab/custom-detection-rules.md`](./lab/custom-detection-rules.md)

---

## 📁 Repository Structure

```
cyber-homelab/
├── v1/                        # Archived first iteration
├── hardware/
│   └── hardware-inventory.yaml
├── infrastructure/
│   ├── proxmox.md
│   └── inspiron.md
├── lab/
│   └── custom-detection-rules.md
├── network/
│   └── README.md
├── services/
│   ├── pihole.md
│   ├── nginx.md
│   ├── wazuh.md
│   ├── myspeed.md
|   └── homarr.md
└── README.md
```

---

_v1 archive available [here](./v1/README.md)._
