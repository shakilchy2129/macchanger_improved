import subprocess ,random
interface=input("Enter the interface name (ex: eth0 or wlan0):")
choose=input("wanna set a random mac? (ex:y/n) (default is n):")
if choose=="y" or choose=="Y" or choose=="yes" or choose=="Yes" or choose=="YES":
    octets = [random.randint(0, 255) for _ in range(6)]
    octets[0] = (octets[0] & 0xFE) | 0x02
    new_mac=(":".join(f"{b:02x}" for b in octets))
else:
    new_mac=input("Enter the new mac to set (ex:02:42:ac:11:00:02) :")
subprocess.run("ifconfig "+interface+" down",shell=True)
subprocess.run("ifconfig "+interface+" hw ether "+new_mac, shell=True)
subprocess.run("ifconfig "+interface+" up",shell=True)

print("Your new temporary mac is now: ",new_mac)
