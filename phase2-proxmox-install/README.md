# Phase 2: Proxmox Installation

With the hardware upgraded and stable, the next step was to install a **bare-metal hypervisor**. For this homelab, I chose **Proxmox VE (Virtual Environment)** to serve as the foundation for virtualization, containerization, and resource management.

---

## 💾 Preparing Installation Media

- Downloaded the latest **Proxmox VE ISO** from the official site.
- Flashed it onto a USB thumb drive using **balenaEtcher**.

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/flash-proxmox-iso-balenaetcher.png" alt="Flashing Proxmox ISO" style="width:600px;">
  </div>
</picture>

Due to issues detailed later, I switched to and tested **Ventoy** to create a bootable multi-ISO USB.

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/ventoy-bootloader.jpg" alt="Ventoy Bootloader" style="width:600px;">
  </div>
</picture>

---

## ⚙️ BIOS/UEFI Configuration

To boot successfully into the installer:

1. Entered BIOS setup.
2. Disabled unnecessary boot sources.
3. Ensured only the USB was enabled.

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/choose-boot-media.jpg" alt="Choose Boot Media" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/disable-boot-sources-except-thumbdrive.jpg" alt="Disable Other Boot Sources" style="width:600px;">
  </div>
</picture>

At first, the drive wasn't detected:

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/drive-not-detected.jpg" alt="Drive Not Detected" style="width:600px;">
  </div>
</picture>

The fix: enabling **Legacy Boot** in BIOS.

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/enable-legacy-boot.jpg" alt="Enable Legacy Boot" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/legacy-boot-disabled.jpg" alt="Legacy Boot Disabled" style="width:600px;">
  </div>
</picture>

---

## 🛠️ Installing Proxmox VE

Once the system recognized the USB, I booted into the **Proxmox installer**.

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/proxmox-installer.jpg" alt="Proxmox Installer" style="width:600px;">
  </div>
</picture>

Steps included:

- Selecting the target SSD
- Configuring root password and email
- Setting network hostname and management IP
- Completing installation

---

## 🌐 Accessing the Web Interface

After reboot, Proxmox VE was accessible via browser at:  
`https://<proxmox-ip>:8006`

<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/proxmox-web-interface-login.png" alt="Login Screen" style="width:600px;">
  </div>
</picture>
<picture>
  <div align="center">
    <img src="../images/phase2-proxmox-install/proxmox-web-interface-home.png" alt="Proxmox Dashboard" style="width:600px;">
  </div>
</picture>

---

## 🚀 Outcome

At the end of Phase 2, the Pavilion is running **Proxmox VE** with access to the web management interface. This provides the core virtualization platform to deploy containers and VMs for future phases of the homelab.
