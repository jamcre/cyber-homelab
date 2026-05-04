# Network Design

Transitioned from flat network to VLAN-segmeneted network using isolated trust zones.

---

## 🔧 Hardware

| Component | Model                       | Role                                  |
| :-------- | :-------------------------- | :------------------------------------ |
| Router    | TP-Link Archer A7 (OpenWRT) | Gateway, DHCP, Firewall, VLAN routing |
| Switch    | NETGEAR GS308Ev4            | Managed 8-port, 802.1Q tagging        |

---

## 🌐 VLANs

| VLAN | Name    | Subnet          | Purpose                                   |
| :--- | :------ | :-------------- | :---------------------------------------- |
| 10   | Trusted | 192.168.10.0/24 | Workstations, Laptops, Phones (5GHz WiFi) |
| 20   | Lab     | 192.168.20.0/24 | Homelab nodes, VMs, Containers            |
| 30   | IoT     | 192.168.30.0/24 | Smart devices (2.4GHz WiFi)               |

---

## 🔌 Physical Layouts

### Router Ports (Archer A7)

- LAN 1: Trunk to NETGEAR Switch (VLANs 10, 20, 30)
- LAN 2: Dedicated to NVR (VLAN 30)

### Switch Ports (GS308Ev4)

- Port 1: Trunk from Router
- Port 2 & 3: optiplex (VLAN 20)
- Port 4: citadel (VLAN 10)
- Port 5-8: empty (VLAN 1, Management Access)

---

## ⚙️ Configuration

### OpenWRT Implementation

- Switch Logic: Uses the `swconfig` model; the internal switch chip (switch0) is configured separately from software interfaces.
- Bridging: `trusted` and `iot` use anonymous bridge blocks (`br-trusted`, `br-iot`) to unite wired and wireless segments.
- DNS: Distributed via `dnsmasq` with Pi-hole (`192.168.20.XX`) as primary and `1.1.1.1` as fallback

### Firewall Matrix

| Source  | Destination   | Policy                           |
| :------ | :------------ | :------------------------------- |
| Trusted | Lab/Internet  | allow                            |
| Lab     | Internet      | allow                            |
| IoT     | Internet      | allow                            |
| IoT     | Internal(Any) | deny (except DHCP/DNS to Router) |
| IoT     | Trusted       | deny                             |

---

## 📝 Other Notes

- IoT Connectivity: Required explicit input rules for DHCP (Port 67) and DNS (Port 53) because of the `input reject` policy
- Management Access: Keeping Ports 5-8 open for default VLAN access to switch web ui

---

> _Network diagram to be added._

---
