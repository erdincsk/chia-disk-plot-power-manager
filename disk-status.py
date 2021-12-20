import os.path
  
disks = [	"1_1TB", "2_1TB",
			"1_2TB",
			"1_4TB",
			"1_8TB", "2_8TB", "3_8TB", "4_8TB", "5_8TB", "6_8TB", "7_8TB", "8_8TB", "9_8TB", "10_8TB", "11_8TB", "12_8TB", "13_8TB", "14_8TB", "15_8TB", "16_8TB", "17_8TB", "18_8TB", "19_8TB", "20_8TB", "21_8TB", "22_8TB", "23_8TB", "24_8TB", "25_8TB", "26_8TB", "27_8TB", "28_8TB", 	
			"1_16TB", "2_16TB", "3_16TB"
		]

root_mount_folder = os.path.expanduser('~/disks/')

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
print("Toplam Disk Sayısı: "+str(len(disks)))
print("Toplam Bağlı Sayısı: "+str(len(mounted_disks)))
print("Toplam Bağlı Olmayan Sayısı: "+str(len(unmounted_disks)))
print()
print("***________________________________________________________________")
print()
if ( len(mounted_disks) > 0 ):
	print("Bağlı Diskler: ")
	print("________________________________________________________________")
	print()

	for mounted_disk in mounted_disks:
		if ( "_1TB" in mounted_disk ):
			print ("******  1TB  ******")
			print(mounted_disk)
		elif ( "_2TB" in mounted_disk ):
			print ("******  2TB  ******")
			print(mounted_disk)
		elif ( "_4TB" in mounted_disk ):
			print ("******  4TB  ******")
			print(mounted_disk)
		elif ( "_8TB" in mounted_disk ):
			print ("******  8TB  ******")
			print(mounted_disk)
		elif ( "_16TB" in mounted_disk ):
			print ("******  16TB  ******")
			print(mounted_disk)

if ( len(unmounted_disks) > 0 ):
	print("Bağlı Olmayan Diskler: ")
	print()
	for unmounted_disk in unmounted_disks:
		print (unmounted_disk)

 