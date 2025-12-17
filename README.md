# mac-spoofer.py  
Simple Linux CLI utility that temporarily changes the MAC address of any network interface.

## Requirements
- Linux (tested on Debian/Ubuntu/Kali)  
- `ifconfig` (net-tools package)  
- Python 3.x (standard library only)

## Usage
1. Clone or download the script.  
2. Make it executable:  
   `chmod +x mac-spoofer.py`  
3. Run as root (required for `ifconfig`):  
   `sudo ./mac-spoofer.py`

4. Follow the prompts:
   - Enter interface name → e.g. `eth0`, `wlan0`  
   - Choose random MAC (`y`) or type your own (`n`)

## Examples
Random MAC:  02:f4:91:3b:78:ea


## Notes & Warnings
- The change is **temporary**—MAC resets after reboot.  
- Always run with `sudo`; otherwise `ifconfig` will fail.  
- Using a locally-administered address (bit-1 set) avoids conflicts; the script forces this when generating random MACs.  
- Misuse on networks you don’t own may violate policies or laws.

## Troubleshooting
`SIOCSIFHWADDR: Operation not supported` → Interface/driver doesn’t allow spoofing.  
`Device busy` → bring interface down first (script already does) or disable NetworkManager temporarily.
