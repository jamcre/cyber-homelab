# Pi-hole

Network-wide DNS filtering and ad blocking deployed as an LXC container on pavilion.

---

## 📋 Container Specs

| Property        | Value                       |
| :-------------- | :-------------------------- |
| CT ID           | 100                         |
| Hostname        | `pihole`                    |
| Template        | ubuntu-22.04-standard       |
| VLAN            | 20 — Lab                    |
| IP              | 192.168.20.XX/24            |
| Gateway         | 192.168.20.1                |
| CPU             | 1 core                      |
| RAM             | 512 MB                      |
| Swap            | 512 MB                      |
| Disk            | 8 GB (local-lvm)            |
| Pi-hole version | v6.x                        |
| Web UI          | `https://pihole.jamcre.dev` |

LXC nesting is enabled — required for Pi-hole FTL to run correctly inside a container.

---

## ⚙️ Installation

Pi-hole was installed using the official one-line installer:

```bash
curl -sSL https://install.pi-hole.net | bash
```

Upstream DNS set to Cloudflare (1.1.1.1) during installation. Default blocklist (StevenBlack) was kept.

---

## 🌐 Cross-VLAN DNS

Pi-hole serves DNS for VLAN 10 (Trusted) and VLAN 20 (Lab). By default Pi-hole v6 rejects queries from non-local subnets — queries from `192.168.10.x` were rejected with `ignoring query from non-local network`.

**Fix:** Set listening mode to **Permit all origins** in Pi-hole admin → Settings → DNS → Interface settings. This is safe because Pi-hole is on a firewalled internal network and port 53 is not exposed externally.

In Pi-hole v6 the config file is `/etc/pihole/pihole.toml` — the v5 `setupVars.conf` file is ignored. The `listeningMode` setting in `pihole.toml` must be set to `all` for cross-VLAN DNS to work. The web UI setting above handles this automatically.

IoT devices (VLAN 30) do not use Pi-hole. They receive Pi-hole's IP via DHCP but cannot reach it — the firewall blocks IoT → Lab traffic. DNS falls back to Cloudflare (1.1.1.1) automatically.

---

## 📡 DHCP DNS Push

Pi-hole is pushed as the primary DNS server to all DHCP clients via OpenWRT dnsmasq:

```
dhcp-option=6,192.168.20.XX,1.1.1.1
```

This applies globally to all interfaces. Cloudflare (`1.1.1.1`) is the fallback if Pi-hole is unreachable.

---

## 🗺️ Local DNS Records

| Hostname             | IP            | Description         |
| :------------------- | :------------ | :------------------ |
| `proxmox.jamcre.dev` | 192.168.20.XX | Nginx Proxy Manager |
| `pihole.jamcre.dev`  | 192.168.20.XX | Nginx Proxy Manager |
| `nginx.jamcre.dev`   | 192.168.20.XX | Nginx Proxy Manager |

All three hostnames resolve to Nginx Proxy Manager, which routes each request to the correct backend service based on the hostname.

Managed in Pi-hole admin → Settings → Local DNS → DNS Records.

---

## 🔒 Notes

Pi-hole v6 is a significant rewrite from v5. Key differences encountered during setup:

- Config file changed from `setupVars.conf` to `pihole.toml`
- CLI command changed: `pihole restartdns` no longer exists, use `pihole reloaddns`
- Default listening mode is `LOCAL` — rejects queries from outside the local subnet
- Cross-VLAN setups require changing listening mode to `all` via the web UI
