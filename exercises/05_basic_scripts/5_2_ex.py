#!/usr/bin/python3
import sys

addr = input('Please type an ip address: ')

ip = addr.split('/')[0].split('.')
mask = int(addr.split('/')[1])
print('Network: ')
print('{:08b} {:08b} {:08b} {:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))) 
bmask =('{:0<32}'.format('1' * mask))
print('Mask: ')
print(addr[-3:])
print ('{:<8}{:<8}{:<8}{:<8}'.format(int(bmask[0:8], 2), int(bmask[8:16], 2), int(bmask[16:24], 2), int(bmask[24:32], 2)))
print ('{:<9}{:<9}{:<9}{:<9}'.format(int(bmask[0:8]), int(bmask[8:16]), int(bmask[16:24]), int(bmask[24:32])))

