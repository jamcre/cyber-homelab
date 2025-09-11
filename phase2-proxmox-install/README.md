# Phase 2: Proxmox Installation

With the hardware upgraded and stable, the next step was to install a **bare-metal hypervisor**. For this homelab, I chose **Proxmox VE (Virtual Environment)** to serve as the foundation for virtualization, containerization, and resource management.

---

## 💾 Preparing Installation Media

- Downloaded the latest **Proxmox VE ISO** from the official site.
- Flashed it onto a USB thumb drive using **balenaEtcher**.

![Flashing Proxmox ISO](../images/phase2-proxmox-install/flash-proxmox-iso-balenaetcher.png)

Due to issues detailed later, I switched to and tested **Ventoy** to create a bootable multi-ISO USB.

![Ventoy Bootloader](../images/phase2-proxmox-install/ventoy-bootloader.jpg)

---

## ⚙️ BIOS/UEFI Configuration

To boot successfully into the installer:

1. Entered BIOS setup.
2. Disabled unnecessary boot sources.
3. Ensured only the USB was enabled.

![Choose Boot Media](../images/phase2-proxmox-install/choose-boot-media.jpg)  
![Disable Other Boot Sources](../images/phase2-proxmox-install/disable-boot-sources-except-thumbdrive.jpg)

At first, the drive wasn’t detected:

![Drive Not Detected](../images/phase2-proxmox-install/drive-not-detected.jpg)

The fix: enabling **Legacy Boot** in BIOS.

![Enable Legacy Boot](../images/phase2-proxmox-install/enable-legacy-boot.jpg)  
![Legacy Boot Disabled](../images/phase2-proxmox-install/legacy-boot-disabled.jpg)

---

## 🛠️ Installing Proxmox VE

Once the system recognized the USB, I booted into the **Proxmox installer**.

![Proxmox Installer](../images/phase2-proxmox-install/proxmox-installer.jpg)

Steps included:

- Selecting the target SSD
- Configuring root password and email
- Setting network hostname and management IP
- Completing installation

---

## 🌐 Accessing the Web Interface

After reboot, Proxmox VE was accessible via browser at:  
`https://<proxmox-ip>:8006`

- ![Login Screen](../images/phase2-proxmox-install/proxmox-web-interface-login.png)
- ![Proxmox Dashboard](../images/phase2-proxmox-install/proxmox-web-interface-home.png)

---

## 🚀 Outcome

At the end of Phase 2, the Pavilion is running **Proxmox VE** with access to the web management interface. This provides the core virtualization platform to deploy containers and VMs for future phases of the homelab.
