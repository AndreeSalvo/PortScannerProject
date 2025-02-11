import nmap


nm = nmap.PortScanner()


target = input("Enter target IP or domain: ")


options = "-sV -sC"  # Corrected syntax


print(f"Scanning {target}...")
nm.scan(target, arguments=options)


for host in nm.all_hosts():
    print(f"\nHost: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print(f"\nProtocol: {protocol}")
        port_info = nm[host][protocol]

        for port in sorted(port_info.keys()):
            state = port_info[port]['state']
            print(f"Port: {port}\tState: {state}")
