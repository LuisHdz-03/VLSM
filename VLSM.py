import ipaddress
import math

class Logica:
    def __init__(self):
        pass

    def calculate_vlsm(self, network_ip, host_requirements):
        sorted_requirements = sorted(host_requirements, reverse=True)
        main_network = ipaddress.ip_network(network_ip, strict=False)

        total_required_hosts = sum(
            [2 ** math.ceil(math.log2(hosts + 2)) for hosts in sorted_requirements]
        )
        available_hosts = main_network.num_addresses - 2

        if total_required_hosts > available_hosts:
            return (
                f"Error: Las subredes requieren {total_required_hosts} direcciones, "
                f"pero la red principal solo tiene {available_hosts} direcciones disponibles."
            )

        subnets = []
        current_ip = main_network.network_address

        for hosts in sorted_requirements:
            bits_needed = math.ceil(math.log2(hosts + 2))
            subnet_mask = 32 - bits_needed

            new_subnet = ipaddress.ip_network(f"{current_ip}/{subnet_mask}", strict=False)

            subnets.append(
                {
                    "network": str(new_subnet.network_address),
                    "mask": str(new_subnet.netmask),
                    "prefix_length": subnet_mask,
                    "first_ip": str(new_subnet.network_address),
                    "last_ip": str(new_subnet.broadcast_address),
                    "broadcast": str(new_subnet.broadcast_address),
                    "total_hosts": hosts,
                }
            )

            current_ip = new_subnet.broadcast_address + 1

            if current_ip > main_network.broadcast_address:
                return "Error: No hay suficiente espacio en la red para todas las subredes requeridas."

        return subnets
