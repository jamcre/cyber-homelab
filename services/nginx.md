# Nginx Proxy Manager

Reverse proxy with SSL termination deployed as an LXC container on pavilion. Provides a single ingress point for all internal services, centralizing SSL certificate management, enabling clean hostnames instead of IP:port access, and keeping backend services unexposed directly to the network.

---

## 📋 Container Specs

| Property | Value                                   |
| :------- | :-------------------------------------- |
| CT ID    | 101                                     |
| Hostname | `nginx`                                 |
| Template | Proxmox VE Helper Script (Debian-based) |
| VLAN     | 20 — Lab                                |
| IP       | 192.168.20.XX/24                        |
| Gateway  | 192.168.20.1                            |
| DNS      | 192.168.20.XX (Pi-hole)                 |
| Web UI   | `https://nginx.jamcre.dev`              |

---

## ⚙️ Installation

Installed using the [Proxmox VE Helper Scripts](https://community-scripts.github.io/ProxmoxVE/scripts?id=nginxproxymanager) NPM script, run from the Proxmox shell. Default settings were used.

---

## 🔒 SSL Certificate

A wildcard Let's Encrypt certificate was generated for `*.jamcre.dev` using the Cloudflare DNS challenge. This covers all subdomains without needing individual certificates per service.

**Steps:**

1. Created a Cloudflare API token with **Edit zone DNS** permissions scoped to `jamcre.dev`
2. In NPM → SSL Certificates → Add SSL Certificate → Let's Encrypt
3. Domain: `*.jamcre.dev`
4. DNS Provider: Cloudflare
5. Credentials file: `dns_cloudflare_api_token=<token>`
6. Propagation seconds: 0

The certificate auto-renews via NPM's built-in renewal process.

**Note:** Let's Encrypt requires a valid email address for account registration. The default `admin@lab.local` set by the helper script will fail — update the NPM admin account email to a real address before requesting the certificate.

---

## 🌐 Proxy Hosts

| Source               | Destination                  | SSL           | Notes                                  |
| :------------------- | :--------------------------- | :------------ | :------------------------------------- |
| `proxmox.jamcre.dev` | `https://192.168.20.XX:8006` | \*.jamcre.dev | Websockets enabled, Block exploits off |
| `pihole.jamcre.dev`  | `http://192.168.20.XX:80`    | \*.jamcre.dev |                                        |
| `nginx.jamcre.dev`   | `http://192.168.20.XX:81`    | \*.jamcre.dev | NPM proxying itself                    |

All proxy hosts have Force SSL and HSTS enabled. HTTP/2 is enabled. HSTS Sub-domains is off.

---

## 🔒 Access

NPM admin panel is accessible from VLAN 10 (Trusted) and VLAN 20 (Lab) only.

| Method            | Address                    |
| :---------------- | :------------------------- |
| HTTPS (via NPM)   | `https://nginx.jamcre.dev` |
| Direct (fallback) | `http://192.168.20.XX:81`  |

---

## 📝 Notes

Proxmox behind a reverse proxy shows a brief **401 No ticket** error on page load — this is a known Proxmox behavior caused by its ticket-based authentication system. Clicking OK dismisses it and the UI loads normally. Direct access at `https://192.168.20.XX:8006` is always available as a fallback and does not show this error.
