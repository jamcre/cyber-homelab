# Homarr

Homelab dashboard and service hub deployed as an LXC container on pavilion. Provides a unified interface for accessing and monitoring all homelab services.

---

## 📋 Container Specs

| Property | Value                       |
| :------- | :-------------------------- |
| CT ID    | 103                         |
| Hostname | `homarr`                    |
| Template | Proxmox VE Helper Script    |
| VLAN     | 20 — Lab                    |
| IP       | 192.168.20.XX/24            |
| Gateway  | 192.168.20.1                |
| DNS      | 192.168.20.XX (Pi-hole)     |
| Web UI   | `https://homarr.jamcre.dev` |

---

## ⚙️ Installation

Installed using the Proxmox VE Helper Scripts from the Proxmox shell.

---

## 🔗 Integrations

| Integration | Method                      | Notes                                                                       |
| :---------- | :-------------------------- | :-------------------------------------------------------------------------- |
| Pi-hole     | API token                   | Connected via Pi-hole integration                                           |
| Proxmox     | API token (PVEAuditor role) | Uses `https://proxmox.jamcre.dev` — direct IP fails due to self-signed cert |

**Proxmox integration note:** Homarr must connect to Proxmox via `https://proxmox.jamcre.dev` rather than directly to `https://192.168.20.XX:8006`. The direct IP serves Proxmox's self-signed certificate which Homarr cannot verify. Routing through NPM resolves this since NPM terminates with the trusted `*.jamcre.dev` wildcard cert.

---

## 🔒 Access

| Method          | Address                     |
| :-------------- | :-------------------------- |
| HTTPS (via NPM) | `https://homarr.jamcre.dev` |
