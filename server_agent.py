import psutil
import socket

class ServerAgent:
    def __init__(self) -> None:
        pass

    def get_cpu_data(self) -> dict:
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)
        cpu_ctx = psutil.cpu_stats()
        cpu_load = psutil.getloadavg()

        data:dict = {
            "CPU USAGE":cpu_usage,
            "CPU":cpu_count,
            "LOAD":cpu_load,
            "CPU CONTEXT":cpu_ctx[[0][0]],
            "INTERRUPTS":cpu_ctx[[1][0]]
            }

        return data

    def get_memory_data(self)-> dict:
        mem_total = psutil.virtual_memory()
        data = {
            "TOTAL MEMORY":mem_total[0],
            "AVAILABLE":mem_total[1],
            "USED":mem_total[4],
            "FREE":mem_total[5]
        }
        return data

    def get_disk_data(self) -> dict:
        disk_partion = psutil.disk_partitions()
        disk_usage = psutil.disk_usage('/')

        data = {
            "DEVICE":disk_partion[0][0],
            "MOUNTPOIT":disk_partion[0][1],
            "FSTYPE":disk_partion[0][2],
            "DEVICE 1":disk_partion[1][0],
            "MOUNTPOIT 1":disk_partion[1][1],
            "FSTYPE 1":disk_partion[1][2],
            "DISK":disk_usage[0],
            "USED":disk_usage[1],
            "FREE":disk_usage[2],
            "USAGE PARCET":disk_usage[3]
        }

        return data

    def get_network_data(self) -> dict:
        net_io_count = psutil.net_io_counters()
        ip_addresses = psutil.net_if_addrs()
        
        data = {
            "PACKET SENT": net_io_count.packets_sent,
            "PACKET RECEIVED": net_io_count.packets_recv,
            "ERROR INPUT": net_io_count.errin,
            "ERROR OUTPUT": net_io_count.errout,
            "DROP INPUT": net_io_count.dropin,
            "DROP OUTPUT": net_io_count.dropout,
        
            "INTERFACE IP": {}
        }
        
        for interface, addresses in ip_addresses.items():
        
            data["INTERFACE IP"][interface] = {
                "IPv4": [],
                "IPv6": [],
                "MAC": []
            }
        
            for addr in addresses:
        
                if addr.family == socket.AF_INET:
                    data["INTERFACE IP"][interface]["IPv4"].append(addr.address)
        
                elif addr.family == socket.AF_INET6:
                    data["INTERFACE IP"][interface]["IPv6"].append(addr.address)
        
                elif addr.family == psutil.AF_LINK:
                    data["INTERFACE IP"][interface]["MAC"].append(addr.address)

        return data

def main():
    server = ServerAgent()

    cpu_data = server.get_cpu_data()
    for k,v in cpu_data.items():
        print(f"{k}:{v}")
    print("--"*20)
    mem_data = server.get_memory_data()
    for k,v in mem_data.items():
        print(f"{k}:{v}")
    print("--"*20)
    disk_data = server.get_disk_data()
    for k,v in disk_data.items():
        print(f"{k}:{v}")
    print("--"*20)
    network_data = server.get_network_data()
    for k,v in network_data.items():
        print(f"{k}:{v}")

if __name__=='__main__':
    main()