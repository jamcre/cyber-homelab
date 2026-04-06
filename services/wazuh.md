# Wazuh

SIEM and endpoint detection platform deployed as a VM on pavilion. Provides log ingestion, threat detection, and security event monitoring across enrolled endpoints.

---

## 📋 VM Specs

| Property        | Value                                      |
| :-------------- | :----------------------------------------- |
| VM ID           | 200                                        |
| Hostname        | `wazuh`                                    |
| Deployment type | Single-node (server + indexer + dashboard) |
| OS              | Wazuh official OVA image                   |
| VLAN            | 20 — Lab                                   |
| IP              | 192.168.20.XX/24                           |
| Gateway         | 192.168.20.1                               |
| DNS             | 192.168.20.XX (Pi-hole)                    |
| CPU             | 3 cores                                    |
| RAM             | 8 GB                                       |
| Disk            | 25 GB                                      |
| Wazuh version   | 4.x                                        |
| Web UI          | `https://wazuh.jamcre.dev`                 |

---

## ⚙️ Installation

Deployed using the official Wazuh OVA image rather than the quickstart script. The image was downloaded directly to pavilion via `wget` and imported as a VM disk — no OS installation required.

```bash
wget https://packages.wazuh.com/4.x/vm/wazuh-4.x.ova
```

A VM was created in Proxmox with no OS and no storage, then the OVA disk was attached and the VM started. This produced a fully configured single-node Wazuh stack with the indexer, server, and dashboard pre-installed.

---

## 🌐 Enrolled Agents

| Agent    | OS             | Method              | Status    |
| :------- | :------------- | :------------------ | :-------- |
| citadel  | Windows        | MSI installer       | ✅ Active |
| pavilion | Linux          | DEB package (amd64) | ✅ Active |
| annex    | macOS          | PKG installer       | ✅ Active |
| inspiron | Linux (Ubuntu) | DEB package (amd64) | ✅ Active |

---

## 🔒 Access

| Method            | Address                     |
| :---------------- | :-------------------------- |
| HTTPS (via NPM)   | `https://wazuh.jamcre.dev`  |
| Direct (fallback) | `https://192.168.20.XX:443` |

NPM proxy requires `proxy_ssl_verify off` due to Wazuh's self-signed backend certificate.

---

## 🔍 Custom Detection Rules

Custom rules are stored in `/var/ossec/etc/rules/local_rules.xml` on the Wazuh manager. Custom rule IDs use the 100000–999999 range to avoid conflicts with built-in rules.

| Rule ID | Description                     | Base SID | Trigger                   | Level | MITRE     |
| :------ | :------------------------------ | :------- | :------------------------ | :---- | :-------- |
| 100001  | SSH brute force — invalid user  | 5710     | 5 attempts, same IP, 120s | 10    | T1110     |
| 100002  | SSH auth failure spike          | 5760     | 8 failures, same IP, 60s  | 12    | T1110     |
| 100003  | Linux unauthorized sudo attempt | 5405     | Single event              | 12    | T1548.003 |
| 100004  | Windows failed logon spike      | 60122    | 5 failures, same IP, 120s | 10    | T1110     |

## All rules tested and verified firing in the Wazuh dashboard. See `lab/custom-detection-rules.md` for full write-up.

---

## 📝 Notes

**pavilion agent — manual config required:** The DEB package installer does not always populate `MANAGER_IP` correctly in `/var/ossec/etc/ossec.conf`. The placeholder value `MANAGER_IP` must be replaced manually with the actual Wazuh server IP. The agent will fail to start entirely if the config is invalid — check `/var/ossec/logs/ossec.log` for the error.

After fixing ossec.conf, manual agent registration was required:

```bash
/var/ossec/bin/agent-auth -m 192.168.20.XX
systemctl restart wazuh-agent
```

**Missing dependency on minimal Debian systems:** `lsb-release` was not present and caused the package installation to halt. Install it before the Wazuh agent package:

```bash
apt install lsb-release -y
```
