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

<picture>
  <div align="center">
    <img src="../images/phase1-hardware/old-pavilion-task-manager-cpu-pre-upgrade.png" alt="CPU Pre-Upgrade" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/old-pavilion-task-manager-ram-pre-upgrade.png" alt="RAM Pre-Upgrade" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/old-pavilion-task-manager-storage-pre-upgrade.png" alt="Storage Pre-Upgrade" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/old-pavilion-task-manager-gpu-pre-upgrade.png" alt="GPU Pre-Upgrade" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/old-pavilion-task-manager-net-pre-upgrade.png" alt="Network Pre-Upgrade" style="width:600px;">
  </div>
</picture>

---

## 🔧 Teardown & Inspection

The Pavilion was disassembled to access its internals. Key steps:

- Removing the back cover
- Laying out components
- Inspecting RAM and storage slots

Pictures from the teardown:

<picture>
  <div align="center">
    <img src="../images/phase1-hardware/pavilion-cover-off.jpg" alt="Cover Off" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/pavilion-open-top.jpg" alt="Open Top" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/pavilion-laid-out.jpg" alt="Laid Out" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/pavilion-complete-teardown.jpg" alt="Complete Teardown" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/pavilion-table-right-view.jpg" alt="Right Table View" style="width:600px;">
  </div>
</picture>

Close-up component views:

<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-hdd.jpg" alt="Old HDD" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-old-pavilion-storage.jpg" alt="Old Storage" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-old-pavilion-ram-slot.jpg" alt="RAM Slot" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-old-components.jpg" alt="Old Components" style="width:600px;">
  </div>
</picture>

---

## 🔄 Upgrades Performed

### Memory

- Added another **8 GB DDR3L stick**, bringing total to **16 GB**.

<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-ram.jpg" alt="RAM Upgrade" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-second-ram-upgrade-slotted.jpg" alt="Second RAM Slotted" style="width:600px;">
  </div>
</picture>

### Storage

- Replaced the slow HDD with a **PNY CS900 1TB SSD** for faster performance.

<picture>
  <div align="center">
    <img src="../images/phase1-hardware/closeup-upgraded-storage.jpg" alt="Upgraded Storage" style="width:600px;">
  </div>
</picture>

---

## ✅ Reassembly & Boot

The Pavilion was carefully reassembled after upgrades.

<picture>
  <div align="center">
    <img src="../images/phase1-hardware/upgraded-pavilion-assembled.jpg" alt="Assembled" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/upgraded-pavilion-sealed.jpg" alt="Sealed" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase1-hardware/old-pavilion-boot.jpg" alt="Boot Screen" style="width:600px;">
  </div>
</picture>

---

## 📂 Supporting Files

This phase includes:

- [`hardware.yaml`](./hardware.yaml): Structured hardware inventory
- [`hardware-spec-script.txt`](/scripts/hardware-specs.ps1): Script used for pulling specs
- [`hardware-spec-script-results.txt`](./hardware-specs-script-results.txt): Captured results after running script

---

## 🚀 Outcome

With upgraded RAM and SSD storage, the Pavilion is now capable of handling **Proxmox VE** and multiple lightweight virtual machines. This sets the stage for the next phase: **Proxmox installation**.
