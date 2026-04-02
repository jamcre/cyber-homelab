# Ubuntu Server — inspiron

Ubuntu Server 24.04 LTS running on the Dell Inspiron 3505, serving as the homelab's Docker host for self-hosted services.

---

## 📋 Node Specs

| Property          | Value                         |
| :---------------- | :---------------------------- |
| Hostname          | `inspiron`                    |
| OS                | Ubuntu Server 24.04.4 LTS     |
| CPU               | AMD Ryzen 5 3450U (4c/8t)     |
| RAM               | 12 GB DDR4                    |
| Storage           | 256 GB NVMe + 1 TB HDD        |
| Network interface | USB Gigabit adapter (primary) |
| VLAN              | 20 — Lab                      |
| IP                | 192.168.20.XX/24              |
| Gateway           | 192.168.20.1                  |
| DNS               | 192.168.20.XX (Pi-hole)       |
| User              | `jamcre`                      |

---

## ⚙️ Post-Install Configuration

- Timezone set to `America/New_York`
- Root SSH login disabled
- UFW enabled with SSH allowed
- Lid close sleep disabled via `/etc/systemd/logind.conf` — all `HandleLidSwitch` values set to `ignore`
- Docker installed via official install script
- User `jamcre` added to docker group

---

## 🐳 Docker

Docker is the primary workload runtime on this node. Portainer is deployed for web-based container management.

| Container | Function      | Port         |
| :-------- | :------------ | :----------- |
| portainer | Docker web UI | 9443 (HTTPS) |

---

## 🔒 Access

SSH access from citadel:

```bash
ssh jamcre@192.168.20.XX
```

Portainer web UI:

```
https://192.168.20.XX:9443
```

---

## 📝 Notes

The built-in 100 Mbps ethernet limitation addressed with USB Gigabit adapter, used as primary network interface for lab use.

This node runs Ubuntu Server directly without a hypervisor to minimize overhead and maximize available resources for Docker workloads. Proxmox experience is already documented via pavilion.
