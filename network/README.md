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
| 20   | Lab     | 192.168.20.0/24 | Homelab nodes — pavilion, dell, VMs, Containers       |
| 30   | IoT     | 192.168.30.0/24 | Smart devices — NVR, cameras, appliances, ac splits   |

---

## 🔌 Physical Layout

### Router — TP-Link Archer A7 (OpenWRT)

| Port         | Connection               | VLAN         |
| :----------- | :----------------------- | :----------- |
| LAN 1        | NETGEAR GS308Ev4 (trunk) | 10, 20, 30   |
| LAN 2        | NVR (basement)           | 30 — IoT     |
| WiFi 2.4 GHz | IoT devices              | 30 — IoT     |
| WiFi 5 GHz   | Trusted devices          | 10 — Trusted |

### Switch — NETGEAR GS308Ev4

| Port | Device     | VLAN         | Type   |
| :--- | :--------- | :----------- | :----- |
| 1    | Router     | 10, 20, 30   | Trunk  |
| 2    | Dell       | 20 — Lab     | Access |
| 3    | Pavilion   | 20 — Lab     | Access |
| 4    | Citadel    | 10 — Trusted | Access |
| 5–8  | Unassigned | —            | —      |

---

## ⚙️ Configuration

> _Configurations to be added._

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

> _Summary of what was achieved, any issues encountered and how they were resolved._
