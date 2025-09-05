# Hardware Specs Grabber for Homelab Documentation
# Run this in PowerShell as Administrator

Write-Host "Gathering system information..." -ForegroundColor Green
Write-Host "=================================`n" -ForegroundColor Green

# Computer Make, Model, and Serial Number
$computerSystem = Get-CimInstance -ClassName Win32_ComputerSystem
$computerBIOS = Get-CimInstance -ClassName Win32_BIOS

# OS Information
$computerOS = Get-CimInstance -ClassName Win32_OperatingSystem

# CPU Information
$computerCPU = Get-CimInstance -ClassName Win32_Processor

# RAM Information
$computerRAM = Get-CimInstance -ClassName Win32_PhysicalMemory
$totalRAM = ($computerRAM | Measure-Object -Property Capacity -Sum).Sum / 1GB
$ramSticks = @()
foreach ($stick in $computerRAM) {
    $ramSticks += @{
        size_gb = [math]::Round($stick.Capacity / 1GB, 2)
        speed_mhz = $stick.Speed
        manufacturer = $stick.Manufacturer
        part_number = $stick.PartNumber.Trim()
    }
}

# Disk Information
$computerDisks = Get-CimInstance -ClassName Win32_DiskDrive | Where-Object { $_.MediaType -ne 'Removable Media' }

$diskArray = @()
foreach ($disk in $computerDisks) {
    $diskArray += @{
        model = $disk.Model
        size_gb = [math]::Round($disk.Size / 1GB, 2)
        interface = $disk.InterfaceType
        media_type = $disk.MediaType
        serial_number = $disk.SerialNumber.Trim()
    }
}

# Network Adapters (excluding virtual ones)
$networkAdapters = Get-CimInstance -ClassName Win32_NetworkAdapterConfiguration | Where-Object { $_.IPEnabled -eq $true }

$adapterArray = @()
foreach ($adapter in $networkAdapters) {
    $adapterArray += @{
        description = $adapter.Description
        ipv4_address = $adapter.IPAddress -join ', '
        mac_address = $adapter.MACAddress
    }
}

# Graphics Card
$graphicsCard = Get-CimInstance -ClassName Win32_VideoController | Where-Object { $_.Name -notlike '*Remote*' -and $_.Name -notlike '*Mirror*' } | Select-Object -First 1

# Output the data in a structured, human-readable way for your YAML
Write-Host "`n"
Write-Host "=== COPY THE OUTPUT BELOW INTO YOUR YAML FILE ===" -ForegroundColor Cyan
Write-Host "`n"

Write-Output "hardware:"
Write-Output "  manufacturer: `"$($computerSystem.Manufacturer.Trim())`""
Write-Output "  model: `"$($computerSystem.Model.Trim())`""
Write-Output "  serial_number: `"$($computerBIOS.SerialNumber.Trim())`""
Write-Output "  bios_version: `"$($computerBIOS.SMBIOSBIOSVersion) $($computerBIOS.SMBIOSMajorVersion).$($computerBIOS.SMBIOSMinorVersion)`""
Write-Output "  cpu:"
Write-Output "    model: `"$($computerCPU.Name.Trim())`""
Write-Output "    cores: $($computerCPU.NumberOfCores)"
Write-Output "    threads: $($computerCPU.NumberOfLogicalProcessors)"
Write-Output "    frequency_ghz: $([math]::Round($computerCPU.MaxClockSpeed / 1000, 2))"
Write-Output "  memory:"
Write-Output "    total_gb: $totalRAM"
Write-Output "    sticks:"
foreach ($stick in $ramSticks) {
    Write-Output "      - size_gb: $($stick.size_gb)"
    Write-Output "        speed_mhz: $($stick.speed_mhz)"
    Write-Output "        manufacturer: `"$($stick.manufacturer)`""
    Write-Output "        part_number: `"$($stick.part_number)`""
}
Write-Output "  storage:"
foreach ($disk in $diskArray) {
    Write-Output "    - model: `"$($disk.model)`""
    Write-Output "      size_gb: $($disk.size_gb)"
    Write-Output "      interface: `"$($disk.interface)`""
    Write-Output "      type: `"$($disk.media_type)`""
    Write-Output "      serial_number: `"$($disk.serial_number)`""
}
Write-Output "  graphics:"
Write-Output "    model: `"$($graphicsCard.Name)`""
Write-Output "    memory_mb: $([math]::Round($graphicsCard.AdapterRAM / 1MB, 2))"
Write-Output "  network_adapters:"
foreach ($adapter in $adapterArray) {
    Write-Output "    - description: `"$($adapter.description)`""
    Write-Output "      ipv4_address: `"$($adapter.ipv4_address)`""
    Write-Output "      mac_address: `"$($adapter.mac_address)`""
}

Write-Host "`n"
Write-Host "=== DATA COLLECTION COMPLETE ===" -ForegroundColor Green
Write-Host "1. Select all the text above starting under the === line."
Write-Host "2. Right-click to copy it."
Write-Host "3. Paste it directly into your YAML file under the appropriate node." -ForegroundColor Yellow