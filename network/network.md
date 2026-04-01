# Network Design

Redesigned the home network from a flat single-subnet layout to a VLAN-segmented architecture with isolated trust zones. Configured on a TP-Link Archer A7 running OpenWRT and a NETGEAR GS308Ev4 managed switch.

---

## 🔧 Hardware

| Device | Model                       | Role                                  |
| :----- | :-------------------------- | :------------------------------------ |
| Router | TP-Link Archer A7 (OpenWRT) | Gateway, VLAN routing, DHCP, firewall |
| Switch | NETGEAR GS308Ev4            | Managed 8-port, VLAN tagging          |

---

## 🌐 VLANs

| VLAN | Name    | Subnet          | Purpose                                               |
| :--- | :------ | :-------------- | :---------------------------------------------------- |
| 10   | Trusted | 192.168.10.0/24 | Personal devices — phones, tablets, laptops, desktops |
| 20   | Lab     | 192.168.20.0/24 | Homelab nodes — pavilion, dell, VMs, containers       |
| 30   | IoT     | 192.168.30.0/24 | Smart devices — NVR, cameras, appliances, AC splits   |

---

## 🔌 Physical Layout

### Router — TP-Link Archer A7 (OpenWRT)

| Port         | Connection               | VLAN         |
| :----------- | :----------------------- | :----------- |
| LAN 1        | NETGEAR GS308Ev4 (trunk) | 10, 20, 30   |
| LAN 2        | NVR                      | 30 — IoT     |
| LAN 3        | -                        | -            |
| LAN 4        | -                        | -            |
| WiFi 2.4 GHz | IoT devices              | 30 — IoT     |
| WiFi 5 GHz   | Trusted devices          | 10 — Trusted |

### Switch — NETGEAR GS308Ev4

| Port | Device     | VLAN         | Type                       |
| :--- | :--------- | :----------- | :------------------------- |
| 1    | Router     | 10, 20, 30   | Trunk                      |
| 2    | Dell       | 20 — Lab     | Access                     |
| 3    | Pavilion   | 20 — Lab     | Access                     |
| 4    | Citadel    | 10 — Trusted | Access                     |
| 5–8  | Unassigned | 1 — Default  | Access (management access) |

---

## ⚙️ Configuration

### OpenWRT — Internal Switch (switch0)

The Archer A7 uses the swconfig model (not DSA). The internal switch chip must be configured separately from the software VLAN interfaces. LAN 1 carries tagged traffic for all VLANs to the NETGEAR switch.

| VLAN | CPU    | LAN 1  | LAN 2  | LAN 3 | LAN 4 | WAN      |
| :--- | :----- | :----- | :----- | :---- | :---- | :------- |
| 1    | tagged | off    | off    | off   | off   | off      |
| 2    | tagged | off    | off    | off   | off   | untagged |
| 10   | tagged | tagged | off    | off   | off   | off      |
| 20   | tagged | tagged | off    | off   | off   | off      |
| 30   | tagged | tagged | tagged | off   | off   | off      |

### OpenWRT — Interfaces

| Interface | Device     | IP Address      | DHCP Range                      | Notes                          |
| :-------- | :--------- | :-------------- | :------------------------------ | :----------------------------- |
| trusted   | br-trusted | 192.168.10.1/24 | 192.168.10.100 – 192.168.10.199 | Bridge: eth0.10 + 5GHz radio   |
| lab       | eth0.20    | 192.168.20.1/24 | 192.168.20.100 – 192.168.20.199 | Wired only, no bridge needed   |
| iot       | br-iot     | 192.168.30.1/24 | 192.168.30.100 – 192.168.30.199 | Bridge: eth0.30 + 2.4GHz radio |

The `trusted` and `iot` interfaces use bridge devices (`br-trusted`, `br-iot`) so that both the wired VLAN and the wireless radio share the same network segment. The `lab` interface is wired only and uses the VLAN device directly.

### OpenWRT — Bridge Devices

Bridge devices are defined as anonymous blocks in `/etc/config/network`. Named blocks are silently ignored by netifd on swconfig-based platforms — anonymous blocks must be used.

```
config device
    option name 'br-trusted'
    option type 'bridge'
    list ports 'eth0.10'

config device
    option name 'br-iot'
    option type 'bridge'
    list ports 'eth0.30'
```

Wireless radios join the bridge automatically via `option network` in `/etc/config/wireless` — they do not need to be listed as bridge ports.

### OpenWRT — Firewall Zones

| Zone    | Input  | Output | Forward | Forwards To |
| :------ | :----- | :----- | :------ | :---------- |
| lan     | accept | accept | accept  | wan         |
| wan     | reject | accept | reject  | —           |
| trusted | accept | accept | reject  | wan, lab    |
| lab     | accept | accept | reject  | wan         |
| iot     | reject | accept | reject  | wan         |

The IoT zone uses `input reject` to block unsolicited inbound traffic to the router. Two additional rules allow DHCP and DNS through while preserving isolation:

```
config rule
    option name 'Allow-DHCP-IoT'
    option src 'iot'
    option proto 'udp'
    option dest_port '67'
    option target 'ACCEPT'

config rule
    option name 'Allow-DNS-IoT'
    option src 'iot'
    option proto 'tcp udp'
    option dest_port '53'
    option target 'ACCEPT'
```

IoT isolation is enforced at the forwarding layer — these rules only affect input to the router itself, not inter-VLAN traffic.

### OpenWRT — DNS

DNS is pushed to all DHCP clients via dnsmasq:

```
dhcp-option=6,192.168.20.XX,1.1.1.1
```

This sets Pi-hole (`192.168.20.XX`) as the primary DNS with Cloudflare (`1.1.1.1`) as fallback for all VLANs. IoT devices receive Pi-hole's IP via DHCP but cannot reach it — the firewall blocks IoT → Lab traffic. DNS falls back to Cloudflare (`1.1.1.1`) automatically.

### NETGEAR GS308Ev4 — VLAN Port Config

Operating in Basic 802.1Q VLAN mode. Port 1 is trunk carrying all VLANs tagged to the router. Ports 2–4 are access ports delivering untagged traffic to end devices. Ports 5–8 remain on VLAN 1 default for direct switch management access when needed.

---

## 🗺️ Topology Diagram

> _Network diagram to be added._

---

## 🔒 Firewall Policy

| Source  | Destination | Policy   |
| :------ | :---------- | :------- |
| Trusted | Lab         | ✅ Allow |
| Trusted | IoT         | ❌ Deny  |
| Lab     | Trusted     | ❌ Deny  |
| IoT     | Internal    | ❌ Deny  |
| IoT     | Internet    | ✅ Allow |

---

## ⚠️ Outstanding Items

> _None at the moment._

---

## 🔓 Firewall Exceptions

| Rule             | Source                    | Destination         | Port   | Reason                                  |
| :--------------- | :------------------------ | :------------------ | :----- | :-------------------------------------- |
| Allow-NPM-to-NVR | 192.168.20.XX (nginx LXC) | 192.168.30.XX (NVR) | TCP 80 | NVR web UI accessible via reverse proxy |

---

## 🚀 Outcome

Successfully migrated the home network from a flat `192.168.1.x` layout to a fully segmented three-VLAN architecture with wired and wireless enforcement.

**Verified results:**

| Test                            | Result                     |
| :------------------------------ | :------------------------- |
| Citadel internet (wired)        | ✅ Working                 |
| Pavilion internet (wired)       | ✅ Working                 |
| Citadel → Pavilion (cross-VLAN) | ✅ Allowed                 |
| Pavilion → Citadel (cross-VLAN) | ❌ Blocked as intended     |
| 5GHz devices on VLAN 10         | ✅ Working                 |
| 2.4GHz devices on VLAN 30       | ✅ Working                 |
| IoT apps functional             | ✅ Cloud-based, unaffected |

**Issues encountered during setup:**

The Archer A7 required configuration of both the software VLAN interfaces and the
internal switch chip (Network → Switch) — software VLANs alone were insufficient
for DHCP to work.

The NETGEAR switch management interface became inaccessible during VLAN configuration,
requiring two factory resets. Ports 5–8 were left on VLAN 1 as a dedicated management
access path.

WiFi VLAN assignment required bridge devices (`br-trusted`, `br-iot`). On swconfig-based
OpenWRT, bridge blocks must be anonymous in `/etc/config/network` — named blocks are
silently ignored by netifd.

The IoT firewall zone's `input reject` policy blocked DHCP and DNS. Two explicit allow
rules for ports 67 and 53 restored connectivity while maintaining isolation.
