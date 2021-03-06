import os.path

disks_1TB = 	["1_1TB", "2_1TB"]
disks_2TB = 	["1_2TB"]
disks_4TB = 	["1_4TB"]
disks_8TB = 	["1_8TB", "2_8TB", "3_8TB", "4_8TB", "5_8TB", "6_8TB", "7_8TB", "8_8TB", "9_8TB", "10_8TB",
				"11_8TB", "12_8TB", "13_8TB", "14_8TB", "15_8TB", "16_8TB", "17_8TB", "18_8TB", "19_8TB", 
				"20_8TB", "21_8TB", "22_8TB", "23_8TB", "24_8TB", "25_8TB", "26_8TB", "27_8TB", "28_8TB"]
disks_16TB = 	["1_16TB", "2_16TB", "3_16TB"]

disks = disks_1TB + disks_2TB + disks_4TB + disks_8TB + disks_16TB

root_mount_folder = os.path.expanduser('~/plot-disks/')

mounted_disks = []
unmounted_disks = []

for disk in disks:

	mount_point = root_mount_folder+disk
	ismounted = os.path.ismount(mount_point)

	if ( ismounted == True ):
		mounted_disks.append(disk)
	else:
		unmounted_disks.append(disk)

print("________________________________________________________________")
print()
print(" Disk Sayısı: "+str(len(disks)))
print(" Bağlı Sayısı: "+str(len(mounted_disks)))
print(" Bağlı Olmayan Sayısı: "+str(len(unmounted_disks)))
print()
print("________________________________________________________________")
print()

if ( len(unmounted_disks) > 0 ):
	print("Bağlı Olmayan Diskler: ")
	print()
	for unmounted_disk in unmounted_disks:
		print (unmounted_disk)

print("\n")

