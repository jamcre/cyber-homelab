# Homelab — v3

This repo documents the third iteration of my homelab, building on [v1](./v1/README.md) & [v2](./v2/README.md). In this version, I focus on working with a stronger computer. The goal being to expand the scope of the lab, beyond just cybersecurity.

---

## 🖥️ Hardware

| Hostname | Type    | Role                | OS              | VLAN         | IP            |
| :------- | :------ | :------------------ | :-------------- | :----------- | :------------ |
| citadel  | Desktop | Workstation         | Windows 11 Home | 10 — Trusted | 192.168.10.XX |
| annex    | Laptop  | Workstation         | macOS Sequoia   | 10 — Trusted | 192.168.10.XX |
| optiplex | Desktop | Virtualization Host | Proxmox VE 8.4  | 20 — Lab     | 192.168.20.XX |
| inspiron | Laptop  | TBD                 | TBD             | TBD          | TBD           |

Full hardware specs: [`hardware/hardware-inventory.yaml`](./hardware/hardware-inventory.yaml)

---

## 🌐 Network

| VLAN | Name    | Subnet          | Purpose                |
| :--- | :------ | :-------------- | :--------------------- |
| 10   | Trusted | 192.168.10.0/24 | Personal devices       |
| 20   | Lab     | 192.168.20.0/24 | Homelab infrastructure |
| 30   | IoT     | 192.168.30.0/24 | Smart devices & NVR    |

VLAN segmentation is live, along with Firewall enforcements. For more details on network design: [`network/network.md`](./network/network.md)

---

## ⚙️ Infrastructure

Proxmox VE running on optiplex as the core virtualization host. For more details: [`infrastructure/optiplex.md`](./infrastructure/optiplex.md)

---

## 🛎️ Services

| Service             | Host           | Function                          | Details                                          |
| :------------------ | :------------- | :-------------------------------- | :----------------------------------------------- |
| Pi-hole             | optiplex (LXC) | Network-wide DNS filtering        | [`services/pihole.md`](./services/pihole.md)     |
| Nginx Proxy Manager | optiplex (LXC) | Reverse proxy and SSL termination | [`services/nginx.md`](./services/nginx.md)       |
| Homepage            | optiplex (LXC) | Central Homepage                  | [`services/homepage.md`](./services/homepage.md) |

---

## 📁 Repository Structure

```
cyber-homelab/
├── v1/                        # Archived first iteration
├── v2/                        # Archived second iteration
├── docs/
│   ├── conventions.md
│   └── hardware-inventory.yaml
├── infrastructure/
│   ├── optiplex.md
│   └── template-node.md
├── lab/
│   └── custom-detection-rules.md
├── network/
│   └── network.md
├── services/
│   ├── pihole.md
│   ├── nginx.md
│   └── homepage.md
├── .gitignore
└── README.md

```

---

_v1 archive available [here](./v1/README.md)._
_v2 archive available [here](./v2/README.md)._
