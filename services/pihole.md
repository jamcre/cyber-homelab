# Pi-hole

_Role:_ Network-wide DNS filtering and internal record management.

---

## 📋 Container Specs

| Property | Value                                        |
| :------- | :------------------------------------------- |
| CT ID    | 100                                          |
| Hostname | `pihole`                                     |
| Template | Proxmox VE Helper Script                     |
| IP/VLAN  | 192.168.20.XX/24 (VLAN 20)                   |
| DNS      | 192.168.20.XX (Pi-hole)                      |
| Web UI   | `https://pihole.jamcre.dev`                  |
| NOTE     | LXC Nesting must be enabled for Pi-hole FTL. |

---

## ⚙️ Deployment and Config

### 🌐 Cross-VLAN DNS

- By default, Pi-hole v6 rejects queireis from non-local subnets (e.g., VLAN 10)
- _Fix:_ Navigate to Settings -> DNS -> Interface settings and set to Permit all origins
- Backend: This updates `listeningMode = 'all'` in `/etc/pihole/pihole.toml`

### 📡 DHCP Integration (OpenWRT)

- Pushed via `dnsmaaq` on the Archer A7
  - Primary: `192.168.20.XX` (Pi-hole)
  - Secondary: `1.1.1.1` (Cloudflare fallback)

## 🗺️ Local DNS Records

| Hostname              | IP            | Description                 |
| :-------------------- | :------------ | :-------------------------- |
| `optiplex.jamcre.dev` | 192.168.20.XX | Routes to Proxmox via NPM   |
| `pihole.jamcre.dev`   | 192.168.20.XX | Routes to Pi-hole via NPM   |
| `nginx.jamcre.dev`    | 192.168.20.XX | Routes to NPM admin via NPM |
| `homepage.jamcre.dev` | 192.168.20.XX | Routes to Homepage via NPM  |

---
