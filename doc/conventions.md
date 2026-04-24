# Lab Conventions

Reference document for IPs and CT/VM ID conventions. All assignments in my homenet and homelab will try to follow these rules.

---

## Thought Process

**Low number = higher importance.**

- Network infra at the bottom of every subnet.
- Dynamic and transient devices float to the top.
- Makes purpose of any IP clear.

---

## Universal IP Convention

The same structure applies to every VLAN. Once you know the pattern, easy to determine what's what.

| Range       | Category               | Notes                                              |
| :---------- | :--------------------- | :------------------------------------------------- |
| .1          | Gateway                | Router interface for this VLAN                     |
| .2 — .9     | Network infrastructure | Switches, APs, managed network devices             |
| .10 — .19   | Physical nodes         | Servers, workstations, laptops (Physical machines) |
| .20 — .49   | LXC containers         | Lightweight containers (Proxmox)                   |
| .50 — .74   | Virtual machines       | Full VMs (Proxmox)                                 |
| .75 — .99   | Reserved               | Future expansion (aka idk yet)                     |
| .100 — .254 | DHCP pool              | All dynamic clients (phones, tablets, etc.)        |

---

## VLAN Assignments

| VLAN | Name    | Subnet          | Purpose                                           |
| :--- | :------ | :-------------- | :------------------------------------------------ |
| 10   | Trusted | 192.168.10.0/24 | Personal devices — workstations, laptops, phones  |
| 20   | Lab     | 192.168.20.0/24 | Homelab infrastructure — servers, VMs, containers |
| 30   | IoT     | 192.168.30.0/24 | Smart home devices — appliances, ACs, robot       |
| 40   | Cams    | 192.168.40.0/24 | Surveillance — NVR and cameras (WIP)              |

---

## Proxmox CT/VM ID Convention

**Rule:** First digit encodes the type. Last two digits are order of deployment

| ID Range | Type              | Examples                         |
| :------- | :---------------- | :------------------------------- |
| 1XX      | LXC container     | Pi-hole, NPM, Homarr, monitoring |
| 2XX      | Security VM       | Wazuh, TheHive, SOC tooling      |
| 3XX      | Application VM    | Crafty, Ghost, web apps          |
| 4XX      | Infrastructure VM | Network or system-level full VMs |
| 5XX      | Dev / Lab VM      | Kali, targets, scratch boxes     |
| 9XX      | Templates         | Base images, reusable installs   |

---

_Follow this document when adding any new device, container, or VM to the lab._
