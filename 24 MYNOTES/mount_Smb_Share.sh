echo Please Uncomment to execute the code.

#mount_smbfs //sambas@192.168.0.104/SharedFolder /mnt/smbshare

#mount_smbfs -W WORKGROUP //sambas@192.168.0.104/SharedFolder /mnt/smbshare

#mount -t smbfs //sambas:password@192.168.0.104/SharedFolder /mnt/smbshare

