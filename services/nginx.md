# Nginx Proxy Manager

_Role:_ Reverse proxy and SSL termination point. Centralizes ingress for `*.jamcre.dev` services.

---

## 📋 Container Specs

| Property | Value                                               |
| :------- | :-------------------------------------------------- |
| CT ID    | 101                                                 |
| Hostname | `nginx`                                             |
| Template | Proxmox VE Helper Script                            |
| IP/VLAN  | 192.168.20.XX/24 (VLAN 20)                          |
| DNS      | 192.168.20.XX (Pi-hole)                             |
| Web UI   | `https://nginx.jamcre.dev`                          |
| SSL      | Let's Encrypt Wildcare via Cloudflare DNS Challenge |

---

## ⚙️ Deployment and Config

- _Installation:_ Deployed via Proxmox Helper Script (Advanced Install)
- _SSL Note:_ Must update the default admin email from `admin@lab.local` to valid address before requesting certificates, or else Let's Encrypt will fail

---

## 🌐 Proxy Hosts

| Source                | Destination                  | Details                                                 |
| :-------------------- | :--------------------------- | :------------------------------------------------------ |
| `optiplex.jamcre.dev` | `https://192.168.20.XX:8006` | Webscokets, Force SSL, HSTS                             |
| `pihole.jamcre.dev`   | `http://192.168.20.XX:80`    | Force SSL, HSTS                                         |
| `nginx.jamcre.dev`    | `http://192.168.20.XX:81`    | Self-proxying admin panel                               |
| `homepage.jamcre.dev` | `https://192.168.20.XX:3000` | Host Validation error, requires ENV in homepage.service |

---
