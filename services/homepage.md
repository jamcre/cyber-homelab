# Homepage

_Role:_ Homepage/Dashboard for central view of all `*.jamcre.dev` services.

---

## 📋 Container Specs

| Property | Value                                               |
| :------- | :-------------------------------------------------- |
| CT ID    | 102                                                 |
| Hostname | `homepage`                                          |
| Template | Proxmox VE Helper Script                            |
| IP/VLAN  | 192.168.20.XX/24 (VLAN 20)                          |
| DNS      | 192.168.20.XX (Pi-hole)                             |
| Web UI   | `http://homepage.jamcre.dev`                        |
| SSL      | Let's Encrypt Wildcare via Cloudflare DNS Challenge |

---

## ⚙️ Deployment and Config

- _Installation:_ Deployed via Proxmox Helper Script (Advanced Install)
- _Deployment Issues:_
  - Typical Deployment:
    - Deployment (DHCP)
    - Set Static Lease in OpenWRT
    - Reboot LXC and access at set IP
    - Test/Verify Service
  - Accessing the _Homepage_, the WebUI gave the following error:
    - `Error: Host validation failed. See logs for more details`
- _Solution_:
  - Running the following:
    - `journalctl -u homepage -n 100 --no-pager`
  - Gave the following:
    - `May 04 15:53:26 homepage pnpm[303]: [2026-05-04T19:53:26.823Z] error: Host validation failed for: homepage.jamcre.dev. Hint: Set the HOMEPAGE_ALLOWED_HOSTS environment variable to allow requests from this host / port.`
  - Add the following:
    - `HOMEPAGE_ALLOWED_HOSTS=homepage.jamcre.dev`
  - To this file:
    - `nano /etc/systemd/system/homepage.service`
  - Ran the following:
    - `systemctl daemon-reexec`
    - `systemctl daemon-reload`
    - `systemctl restart homepage`
  - Verify, now working Homepage (YAY!)

---
