import ipaddress
import sys


def subnetCalculator(requiredIP):

    try:
        ip = ipaddress.IPv4Network(requiredIP, strict=False)
        initial = int(str(ip).split('.')[0])
        ipclass = ''

        if initial == 0:
            return print('This is the source IP')
        elif initial >= 1 and initial <= 126:
            ipclass = "CLASS A - IP range 1-126"
        elif initial == 127:
            return print('This is a Loopback Address range')
        elif initial >= 126 and initial <= 191:
            ipclass = "CLASS B - IP range 128-191"
        elif initial >= 192 and initial <= 223:
            ipclass = "CLASS C - IP range 192-223"
        elif initial >= 224 and initial <= 239:
            return print('Class D - Multicast Address range')
        else:
            return print('Class E - Experimental Address range')
    except ipaddress.AddressValueError:
            return print('This is not a valid IP address')
    except ipaddress.NetmaskValueError:
            return print('Invalid Subnet mask')


    if ip.is_private:
        print('This is a private range')

    print('The Network ID is {}'.format(ip.with_netmask))
    print('The First IP assignable for an host is {}'.format(ip.network_address + 1))
    print('The Last IP assignable fo an host is {}'.format(ip.broadcast_address - 1))
    print('The Broadcast address is {}'.format(ip.broadcast_address))
    print('The Number of Assignable IP is {}'.format(ip.num_addresses))

def main():
    subnetCalculator('196.128.4.6/24')

if __name__ == ('__main__'):
    main()