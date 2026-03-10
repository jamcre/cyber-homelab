# Cybersecurity Homelab — v2

This repository documents the second iteration of my cybersecurity homelab. Building on [v1](./v1/README.md), this version introduces a multi-node infrastructure, VLAN-segmented networking, and a more intentional service architecture.

---

## 🖥️ Hardware

| Hostname | Type    | Role                | OS              |
| :------- | :------ | :------------------ | :-------------- |
| citadel  | Desktop | Primary Workstation | Windows 11 Home |
| pavilion | Server  | Virtualization Host | Proxmox VE      |
| annex    | Laptop  | Mobile Workstation  | macOS Sequoia   |
| TBD      | Laptop  | TBD                 | TBD             |

Full hardware specs: [`hardware/hardware-inventory.yaml`](./hardware/hardware-inventory.yaml)

---

## 🌐 Network

| VLAN | Name    | Subnet          | Purpose                |
| :--- | :------ | :-------------- | :--------------------- |
| 10   | Trusted | 192.168.10.0/24 | Personal devices       |
| 20   | Lab     | 192.168.20.0/24 | Homelab infrastructure |
| 30   | IoT     | 192.168.30.0/24 | Smart devices & NVR    |

Full network design: [`network/README.md`](./network/README.md)

---

## ⚙️ Services

> _To be documented as services are deployed._

---

## 🔬 Security Lab

> _To be documented once lab environment is built._

---

## 📁 Repository Structure

```
cyber-homelab/
├── v1/                        # Archived first iteration
├── hardware/
│   └── hardware-inventory.yaml
├── network/
│   └── README.md
├── infrastructure/            # Proxmox setup & node configs
├── services/                  # Per-service deployment docs
├── lab/                       # Security lab environment & exercises
└── README.md
```

---

_v1 archive available [here](./v1/README.md)._
