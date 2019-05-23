import psutil

disk_partitions = psutil.disk_partitions()

for disk_partition in disk_partitions:
    print('Device: %s (%s), MountPoint: %s, opts=%s'
          % (disk_partition.device, disk_partition.fstype, disk_partition.mountpoint, disk_partition.opts))
