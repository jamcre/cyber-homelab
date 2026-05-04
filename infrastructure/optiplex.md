# optiplex

Proxmox VE for homelab v3 on node optiplex. Builds on v2 by moving to a stronger, smaller, and frankly better looking machine to serve as my main hypervisor node.

---

## 📋 Overview

| Property | Value                        |
| :------- | :--------------------------- |
| Hostname | `optiplex`                   |
| Role     | Virtualization Host          |
| OS       | Proxmox VE 8.4               |
| CPU      | Intel Core i7-8700T (6c/12t) |
| RAM      | 32 GB DDR4                   |
| Storage  | 1 TB SATA SSD (PNY CS900)    |

---

## 🌐 Network

| Property  | Value                   |
| :-------- | :---------------------- |
| Interface | eno2 (Intel e1000e)     |
| Bridge    | vmbr0                   |
| VLAN      | 20 - Lab                |
| IP        | 192.168.20.XX           |
| Gateway   | 192.168.20.1            |
| DNS       | 192.168.20.XX (Pi-hole) |

---

## ⚙️ Config

Tweaks made during setup:

- Disabling enterprise repo
- Enabling no-enterprise repo
- Disabling the subscription nag in WebUI
- Replace Proxmox `apt` sources with official Debian CDN mirrors (deb.debian.org)
- Run system updates

---

## 🖥️ Workload

| Type | Name     | Function                                            |
| :--- | :------- | :-------------------------------------------------- |
| LXC  | pihole   | Network-wide DNS filtering — see `services/`        |
| LXC  | nginx    | Reverse proxy and SSL termination — see `services/` |
| LXC  | homepage | Central Homepage — see `services/`                  |

---

## 🔒 Access

| Method | Address                       |
| :----- | :---------------------------- |
| WebUI  | `https://optiplex.jamcre.dev` |
| Direct | `https://192.168.20.XX:8006`  |
| SSH    | `ssh root@192.168.20.XX`      |
