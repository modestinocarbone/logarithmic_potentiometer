#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:33:03 2025
@author: modestino
"""
import numpy as np
import matplotlib.pyplot as plt 

max_angle = 270  # Maximum degree of potentiometer

# Resistors in Parallel
def parr(R1, R2):
    return R1 * R2 / (R1 + R2)

# Angle range 
ang = np.linspace(0, max_angle, 100)

R0 = 10**3
# linear potentiometer
R_lin_1 = ang / max_angle * R0  
# the other port of the linear potentiometer
R_lin_2 = R0 - R_lin_1

plt.figure(1)
plt.title("Linear Potentiometer Curve")

plt.plot(ang, R_lin_1/1000, label='lin pot')
plt.legend()
plt.grid()
plt.xlabel('ang /°')
plt.ylabel(r'R /$k\Omega$')

#%%

plt.figure(2)
plt.title('Linear Pot')

# Voltage divider
Vout_Vin = R_lin_1 / (R_lin_1 + R_lin_2)

plt.plot(ang, Vout_Vin, label='linear')
plt.legend()
plt.grid()
plt.xlabel('ang /°')
plt.ylabel('Vout/Vin')

#%%

plt.figure(3)
plt.title('Log Pot')

# logaritmic plot
for b in range(1, 7):
    Vout_Vin = parr(R_lin_1, R0 / b) / (parr(R_lin_1, R0 / b) + R_lin_2)
    plt.plot(ang, Vout_Vin, label=f'b={b}')

plt.legend()
plt.grid()
plt.xlabel('ang /°')
plt.ylabel('Vout/Vin')


#%%

plt.figure(4)
plt.title('Log Pot vs Linear-in-dB Curve')

b = 9

# linear potentiometer
Vout_Vin_lin = 20 * np.log10(R_lin_1 / (R_lin_1 + R_lin_2))

# log potentiometer
Vout_Vin = parr(R_lin_1, R0 / b) / (parr(R_lin_1, R0 / b) + R_lin_2)
Vout_Vin_dB = 20 * np.log10(Vout_Vin)

# ideal curve 12 °/dB 
max_dB = 30
ideal_dB = ang * (max_dB / max_angle) - max_dB

plt.plot(ang, Vout_Vin_dB, label=f'log pot (b={b})')
plt.plot(ang, ideal_dB, '--', label=f'ideal linear dB {int(max_angle/max_dB)}°/dB')
plt.plot(ang, Vout_Vin_lin, label='linear pot')

plt.legend()
plt.grid()
plt.xlabel('ang /°')
plt.ylabel('Vout/Vin [dB]')
