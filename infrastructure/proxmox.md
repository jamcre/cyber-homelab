# Proxmox VE — pavilion

Clean v2 installation of Proxmox VE on pavilion. Replaces the v1 install which ran on a flat network with leftover VM configs and no VLAN awareness.

---

## 📋 Node Specs

| Property           | Value                        |
| :----------------- | :--------------------------- |
| Hostname           | `pavilion.lan`               |
| Proxmox VE version | 8.x                          |
| Host CPU           | Intel Core i5-4590T (4c/4t)  |
| Host RAM           | 16 GB DDR3L                  |
| Storage            | 1 TB SATA SSD (PNY CS900)    |
| Network interface  | enp3s0 (Realtek RTL8111)     |
| Bridge             | vmbr0                        |
| VLAN               | 20 — Lab                     |
| IP                 | 192.168.20.XX/24             |
| Gateway            | 192.168.20.1                 |
| DNS                | 192.168.20.XX (Pi-hole)      |
| Web UI             | `https://proxmox.jamcre.dev` |

---

## ⚙️ Installation Notes

Installed via USB from the official Proxmox VE ISO. Network was configured during installation with a static IP on VLAN 20. The FQDN was set to `pavilion.lan` matching the OpenWRT domain.

After installation, the enterprise repository was disabled and the community (no-subscription) repository was enabled to allow package updates without a paid subscription:

```bash
# Disable enterprise repo
echo "# disabled" > /etc/apt/sources.list.d/pve-enterprise.list

# Enable community repo
echo "deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription" \
  > /etc/apt/sources.list.d/pve-no-subscription.list

apt update && apt dist-upgrade -y
```

The subscription nag screen in the web UI was removed:

```bash
sed -i "s/data.status !== 'Active'/false/" \
  /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js
systemctl restart pveproxy
```

---

## 🌐 Network Configuration

Pavilion uses a static IP configured directly in `/etc/network/interfaces` on the Proxmox host. The `vmbr0` bridge is the primary interface for both host management and VM/container networking.

```
auto vmbr0
iface vmbr0 inet static
    address 192.168.20.XX/24
    gateway 192.168.20.1
    bridge-ports enp3s0
    bridge-stp off
    bridge-fd 0
```

DNS resolves `proxmox.jamcre.dev` to Nginx Proxy Manager (`192.168.20.XX`) via Pi-hole local DNS records. NPM forwards the request to Proxmox at `192.168.20.XX:8006` with a valid wildcard SSL certificate.

---

## 🖥️ Workloads

| Type | Name   | Function                                                    |
| :--- | :----- | :---------------------------------------------------------- |
| LXC  | pihole | Network-wide DNS filtering — see `services/pihole.md`       |
| LXC  | nginx  | Reverse proxy and SSL termination — see `services/nginx.md` |
| VM   | wazuh  | SIEM and endpoint detection — see `services/wazuh.md`       |

---

## 🔒 Access

The Proxmox web UI is accessible from VLAN 10 (Trusted) and VLAN 20 (Lab). IoT devices have no path to the management interface.

| Method            | Address                      |
| :---------------- | :--------------------------- |
| HTTPS (via NPM)   | `https://proxmox.jamcre.dev` |
| Direct (fallback) | `https://192.168.20.XX:8006` |

SSH access is available from citadel:

```bash
ssh root@192.168.20.XX
```
