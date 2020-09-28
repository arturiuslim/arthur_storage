#!/usr/bin/python3
from sys import argv

#addr = input('Please type an ip address: ')
addr = argv[1]
ip = addr.split('/')[0].split('.')
mask = int(addr.split('/')[1])
bmask =('{:0<32}'.format('1' * mask))
ipaddr = '{:08b} {:08b} {:08b} {:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])) 
tmp_ip = '{:08b}{:08b}{:08b}{:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])) 
prlntb = '{:<8} {:<8} {:<8} {:<8}'.format(int(bmask[0:8], 2), int(bmask[8:16], 2), int(bmask[16:24], 2), int(bmask[24:32], 2))
prlntd = '{:<8} {:<8} {:<8} {:<8}'.format(int(bmask[0:8]), int(bmask[8:16]), int(bmask[16:24]), int(bmask[24:32]))

ntw = tmp_ip[0:mask]
#print(ntw)
ntw = (ntw + '0' * (32-mask))
#print(ntw)
prf = '{:<8} {:<8} {:<8} {:<8}'.format(ntw[0:8], ntw[8:16], ntw[16:24], ntw[24:32])
prf_d = '{:<8} {:<8} {:<8} {:<8}'.format(int(ntw[0:8], 2), int(ntw[8:16], 2), int(ntw[16:24], 2), int(ntw[24:32], 2))
#print(prf)
#print(prf_d)

print('Network: ')
print(prf_d)
print(prf)
print('Mask: ')
print(addr[-3:])
print(prlntb)
print (prlntd)

