# Phase 1: Hardware Setup & Upgrades

This phase documents the foundation of the cyber-homelab: the hardware. I repurposed an **HP Pavilion 23-q067c All-in-One** system by upgrading its storage and RAM, preparing it for virtualization and lab deployments.

---

## 🖥️ Original Hardware Specs

Before upgrades, the machine had:

- **CPU**: Intel Core i5-4590T @ 2.0GHz (4 cores / 4 threads)
- **RAM**: 8 GB DDR3L
- **Storage**: 1 TB HDD (5400 RPM)
- **GPU**: Integrated Intel HD Graphics 4600

Task Manager snapshots (pre-upgrade):

- ![CPU Pre-Upgrade](../images/phase1-hardware/old-pavilion-task-manager-cpu-pre-upgrade.PNG)
- ![RAM Pre-Upgrade](../images/phase1-hardware/old-pavilion-task-manager-ram-pre-upgrade.PNG)
- ![Storage Pre-Upgrade](../images/phase1-hardware/old-pavilion-task-manager-storage-pre-upgrade.PNG)
- ![GPU Pre-Upgrade](../images/phase1-hardware/old-pavilion-task-manager-gpu-pre-upgrade.PNG)
- ![Network Pre-Upgrade](../images/phase1-hardware/old-pavilion-task-manager-net-pre-upgrade.PNG)

---

## 🔧 Teardown & Inspection

The Pavilion was disassembled to access its internals. Key steps:

- Removing the back cover
- Laying out components
- Inspecting RAM and storage slots

Pictures from the teardown:

- ![Cover Off](../images/phase1-hardware/pavilion-cover-off.jpg)
- ![Open Top](../images/phase1-hardware/pavilion-open-top.jpg)
- ![Laid Out](../images/phase1-hardware/pavilion-laid-out.jpg)
- ![Complete Teardown](../images/phase1-hardware/pavilion-complete-teardown.jpg)
- ![Right Table View](../images/phase1-hardware/pavilion-table-right-view.jpg)

Close-up component views:

- ![Old HDD](../images/phase1-hardware/closeup-hdd.jpg)
- ![Old Storage](../images/phase1-hardware/closeup-old-pavilion-storage.jpg)
- ![RAM Slot](../images/phase1-hardware/closeup-old-pavilion-ram-slot.jpg)
- ![Old Components](../images/phase1-hardware/closeup-old-components.jpg)

---

## 🔄 Upgrades Performed

### Memory

- Added another **8 GB DDR3L stick**, bringing total to **16 GB**.

![RAM Upgrade](../images/phase1-hardware/closeup-ram.jpg)  
![Second RAM Slotted](../images/phase1-hardware/closeup-second-ram-upgrade-slotted.jpg)

### Storage

- Replaced the slow HDD with a **Samsung 870 EVO 500GB SSD** for faster performance.

![Upgraded Storage](../images/phase1-hardware/closeup-upgraded-storage.jpg)

---

## ✅ Reassembly & Boot

The Pavilion was carefully reassembled after upgrades.

- ![Assembled](../images/phase1-hardware/upgraded-pavilion-assembled.jpg)
- ![Sealed](../images/phase1-hardware/upgraded-pavilion-sealed.jpg)
- ![Boot Screen](../images/phase1-hardware/old-pavilion-boot.jpg)

---

## 📂 Supporting Files

This phase includes:

- [`hardware.yaml`](./hardware.yaml): Structured hardware inventory
- [`hardware-spec-script.txt`](./hardware-spec-script.txt): Script used for pulling specs
- [`hardware-spec-script-results.txt`](./hardware-spec-script-results.txt): Captured results after running script

---

## 🚀 Outcome

With upgraded RAM and SSD storage, the Pavilion is now capable of handling **Proxmox VE** and multiple lightweight virtual machines. This sets the stage for the next phase: **Proxmox installation**.
