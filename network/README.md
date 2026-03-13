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

| Port         | Connection               | VLAN       |
| :----------- | :----------------------- | :--------- |
| LAN 1        | NETGEAR GS308Ev4 (trunk) | 10, 20, 30 |
| LAN 2        | -                        | -          |
| LAN 3        | -                        | -          |
| LAN 4        | -                        | -          |
| WiFi 2.4 GHz | -                        | -          |
| WiFi 5 GHz   | -                        | -          |

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

The Archer A7 has an internal switch chip that must be configured separately from the software VLAN interfaces. LAN 1 carries tagged traffic for all VLANs to the NETGEAR switch.

| VLAN | CPU    | LAN 1  | LAN 2 | LAN 3 | LAN 4 | WAN      |
| :--- | :----- | :----- | :---- | :---- | :---- | :------- |
| 1    | tagged | off    | off   | off   | off   | off      |
| 2    | tagged | off    | off   | off   | off   | untagged |
| 10   | tagged | tagged | off   | off   | off   | off      |
| 20   | tagged | tagged | off   | off   | off   | off      |
| 30   | tagged | tagged | off   | off   | off   | off      |

### OpenWRT — Interfaces

Three VLAN interfaces created under Network → Interfaces, each with a static IP and DHCP server enabled:

| Interface | Device  | IP Address      | DHCP Range                      |
| :-------- | :------ | :-------------- | :------------------------------ |
| trusted   | eth0.10 | 192.168.10.1/24 | 192.168.10.100 – 192.168.10.250 |
| lab       | eth0.20 | 192.168.20.1/24 | 192.168.20.100 – 192.168.20.250 |
| iot       | eth0.30 | 192.168.30.1/24 | 192.168.30.100 – 192.168.30.250 |

### OpenWRT — Firewall Zones

| Zone    | Input  | Output | Forward | Forwards To |
| :------ | :----- | :----- | :------ | :---------- |
| lan     | accept | accept | accept  | wan         |
| wan     | reject | accept | reject  | —           |
| trusted | accept | accept | reject  | wan, lab    |
| lab     | accept | accept | reject  | wan         |
| iot     | reject | accept | reject  | wan         |

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

## 🚀 Outcome

Successfully migrated the home network from a flat `192.168.1.x` layout to a fully segmented three-VLAN architecture. All devices are isolated into appropriate trust zones with firewall enforcement between them.

**Verified results:**

| Test                            | Result                 |
| :------------------------------ | :--------------------- |
| Citadel internet                | ✅ Working             |
| Pavilion internet               | ✅ Working             |
| Citadel → Pavilion (cross-VLAN) | ✅ Allowed             |
| Pavilion → Citadel (cross-VLAN) | ❌ Blocked as intended |

**Issues encountered during setup:**

The Archer A7 required configuration of both the software VLAN interfaces (Network → Devices/Interfaces) and the internal switch chip (Network → Switch). Configuring only the software VLANs was insufficient — devices could not get DHCP leases until the switch0 VLAN table was also configured with LAN 1 set to tagged for VLANs 10, 20, and 30.

The NETGEAR switch management interface became inaccessible during VLAN configuration because all ports were moved to tagged VLANs with no path back to the management subnet. This required two factory resets. The final solution was to leave ports 5–8 on VLAN 1 (default) to serve as a dedicated management access path — any device plugged into those ports can reach the switch management page directly.

Pavilion retained its v1 static IP (`192.168.0.XX`) hardcoded in Proxmox. Updated `/etc/network/interfaces` on the Proxmox host to reassign `vmbr0` to `192.168.20.XX/24` with gateway `192.168.20.1`.
