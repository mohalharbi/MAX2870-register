# Copyright (c) 2025 Mohammed Alharbi
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 or later.
# See the LICENSE file for more details.

from tkinter import ttk, messagebox, StringVar
import tkinter as tk

import sys


# Print Python and Tkinter version info
print("Python version:", sys.version)
print("Tkinter version:", tk.TkVersion)

def insert_space(binary_str):
    return ' '.join([binary_str[i:i+4] for i in range(0, len(binary_str), 4)])

def update_Reg0(event):
    # print(event)
    Reg0_entered_bit31 = combo_reg0_bit31.get()
    Reg0_entered_bit3015 = Reg0_entry_bit3015.get()
    Reg0_entered_bit1403 = Reg0_entry_bit1403.get()

    # check if bit 31 not empty and update its value
    if (Reg0_entered_bit31 != '' and Reg0_entered_bit31 == 'Integer N'):
        reg0_bit31 = 1
    else:
        reg0_bit31 = 0

    # check if bit 30-15 are not empty and convert to binary with 16 bit size
    if Reg0_entered_bit3015 != '':
        bin_Reg0_bit3015 = bin(int(Reg0_entered_bit3015))[2:]
        bin_Reg0_bit3015 = bin_Reg0_bit3015.zfill(16)
        # print(bin_Reg0_bit3015)

    # check if bit 14-03 are not empty and convert them to binary with 12 bit size
    if Reg0_entered_bit1403 != '':
        bin_Reg0_bit1403 = bin(int(Reg0_entered_bit1403))[2:]
        bin_Reg0_bit1403 = bin_Reg0_bit1403.zfill(12)
        # print(bin_Reg0_bit1403)

    # check if all bits 31-0 are filled and give the value of register in binary and hexdecimal
    if (Reg0_entered_bit3015 != '' and Reg0_entered_bit31 != '' and Reg0_entered_bit1403 != ''):
        #reg0_display_box.config(text=str(bin(reg0_bit31)) + bin_Reg0_bit3015 + bin_Reg0_bit1403 + "000")
        #form the registery data in binary format
        Reg0_bin = str(reg0_bit31) + bin_Reg0_bit3015 + bin_Reg0_bit1403 + "000"
        print(Reg0_bin)
        # add space to binary values to make it readbale
        binary_with_spaces = insert_space(Reg0_bin)
        # in order to convert binary string into hex, we need to convert into decimal then hexadecimal
        Reg0_decimal = int(Reg0_bin, 2)
        Reg0_hex = hex(Reg0_decimal)[2:]
        Reg0_hex=Reg0_hex.upper() #convert hex to uppercase
        #to show all 32 bits even if they are zeroes
        Reg0_hex = Reg0_hex.zfill(8)
        #update register 0 data in binary and hex format
        hex_reg0_text.set(Reg0_hex)
        bin_reg0_text.set(binary_with_spaces)
        #print("hex_str value is:", Reg0_hex)
        #print("Type of hex_str:", type(hex_str))
        # print(equ_num)

def update_Reg1(event):
    #print(event)
    Reg1_entered_bit31 = combo_reg1_bit31.get()
    Reg1_entered_bit3029=combo_reg1_bit3029.get()
    Reg1_entered_bit2827=combo_reg1_bit2827.get()
    Reg1_entered_bit2615=Reg1_entry_bit2615.get()
    Reg1_entered_bit1403=Reg1_entry_bit1403.get()
    # check if bit 31 not empty and update its value
    if (Reg1_entered_bit31 != '' and Reg1_entered_bit31 == 'Disable clamping'):
        reg1_bit31_value = 0
        bin_Reg1_bit31 = bin(reg1_bit31_value)[2:]
    else:
        reg1_bit31_value = 1
        bin_Reg1_bit31 = bin(reg1_bit31_value)[2:]

    #check bit 30-29
    if (Reg1_entered_bit3029 != '' and Reg1_entered_bit3029 == 'Disable CP (INT)'):
        reg1_bit3029_value = 0
        #convert value into binary of 2 bits
        bin_Reg1_bit3029 = bin(reg1_bit3029_value)[2:]
        bin_Reg1_bit3029 = bin_Reg1_bit3029.zfill(2)

    else:
        reg1_bit3029_value = 1
        #convert value into binary of 2 bits
        bin_Reg1_bit3029 = bin(reg1_bit3029_value)[2:]
        bin_Reg1_bit3029 = bin_Reg1_bit3029.zfill(2)

    #check bit 28 - 27
    if (Reg1_entered_bit2827 != '' and Reg1_entered_bit2827 == 'Normal mode'):
        reg1_bit2827_value = 0
        #convert value into binary of 2 bits
        bin_Reg1_bit2827 = bin(reg1_bit2827_value)[2:]
        bin_Reg1_bit2827 = bin_Reg1_bit2827.zfill(2)

    elif (Reg1_entered_bit2827 == 'Source mode'):
        reg1_bit2827_value = 2
        #convert value into binary of 2 bits
        bin_Reg1_bit2827 = bin(reg1_bit2827_value)[2:]
        bin_Reg1_bit2827 = bin_Reg1_bit2827.zfill(2)
    else:
        reg1_bit2827_value = 3
        #convert value into binary of 2 bits
        bin_Reg1_bit2827 = bin(reg1_bit2827_value)[2:]
        bin_Reg1_bit2827 = bin_Reg1_bit2827.zfill(2)

    # check if bits 26 - 15 are not empty and convert to binary with 12 bit size
    if Reg1_entered_bit2615 != '':
        bin_Reg1_bit2615 = bin(int(Reg1_entered_bit2615))[2:]
        bin_Reg1_bit2615 = bin_Reg1_bit2615.zfill(12)

    # check if bits 14 - 3 are not empty and convert to binary with 12 bit size
    if Reg1_entered_bit1403 != '':
        bin_Reg1_bit1403 = bin(int(Reg1_entered_bit1403))[2:]
        bin_Reg1_bit1403 = bin_Reg1_bit1403.zfill(12)

    # check if all bits 31-0 are filled and give the value of register in binary and hexdecimal
    if (Reg1_entered_bit31 != '' and Reg1_entered_bit3029 != '' and Reg1_entered_bit2827 != '' and Reg1_entered_bit2615 != '' and Reg1_entered_bit1403 != ''):
        Reg1_bin = bin_Reg1_bit31 + bin_Reg1_bit3029 + bin_Reg1_bit2827 +bin_Reg1_bit2615+bin_Reg1_bit1403+ "001"
        Reg1_binary_with_spaces = insert_space(Reg1_bin)
        #print("Type of Reg1_bin:", type(Reg1_bin))
        Reg1_decimal = int(Reg1_bin,2)
        print(Reg1_decimal)
        Reg1_hex = hex(Reg1_decimal)[2:]
        Reg1_hex=Reg1_hex.upper() #convert hex to uppercase
        #to show all 32 bits even if it is zeroes
        Reg1_hex=Reg1_hex.zfill(8)
        #update register 0 data in binary and hex format
        hex_reg1_text.set(Reg1_hex)
        bin_reg1_text.set(Reg1_binary_with_spaces)

def update_Reg2(event):
    #print(event)
    Reg2_entered_bit31 = combo_reg2_bit31.get()
    Reg2_entered_bit3029 = combo_reg2_bit3029.get()
    Reg2_entered_bit2826 = combo_reg2_bit2826.get()
    Reg2_entered_bit25 = combo_reg2_bit25.get()
    Reg2_entered_bit24 = combo_reg2_bit24.get()
    Reg2_entered_bit2314 = Reg2_entry_bit2314.get()
    Reg2_entered_bit13 = combo_reg2_bit13.get()
    Reg2_entered_bit1209 = combo_reg2_bit1209.get()
    Reg2_entered_bit08 = combo_reg2_bit08.get()
    Reg2_entered_bit07 = combo_reg2_bit07.get()
    Reg2_entered_bit06 = combo_reg2_bit06.get()
    Reg2_entered_bit05 = combo_reg2_bit05.get()
    Reg2_entered_bit04 = combo_reg2_bit04.get()
    Reg2_entered_bit03 = combo_reg2_bit03.get()


    #get bit31 value
    if (Reg2_entered_bit31 == 'f_PFD < 32 MHz'):
        reg2_bit31_value = 0
        bin_Reg2_bit31 = bin(reg2_bit31_value)[2:]
    else:
        reg2_bit31_value = 1
        bin_Reg2_bit31 = bin(reg2_bit31_value)[2:]

    # get bit 30 -29 values  Low noise mode", "Low spur mode 1", "Low spur mode 2
    if (Reg2_entered_bit3029 == 'Low noise mode'):
        reg2_bit3029_value = 0
        bin_Reg2_bit3029 = bin(reg2_bit3029_value)[2:]
        bin_Reg2_bit3029=bin_Reg2_bit3029.zfill(2)

    elif (Reg2_entered_bit3029 == 'Low spur mode 1'):
        reg2_bit3029_value = 2
        bin_Reg2_bit3029 = bin(reg2_bit3029_value)[2:]
        bin_Reg2_bit3029 = bin_Reg2_bit3029.zfill(2)

    else:
        reg2_bit3029_value = 3
        bin_Reg2_bit3029 = bin(reg2_bit3029_value)[2:]
        bin_Reg2_bit3029 = bin_Reg2_bit3029.zfill(2)

    # get bit 28 -26 values  Low noise mode", "Low spur mode 1", "Low spur mode 2
    if (Reg2_entered_bit2826 == 'Three state output'):
        reg2_bit2826_value = 0
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    elif (Reg2_entered_bit2826 == 'D_VDD'):
        reg2_bit2826_value = 1
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    elif (Reg2_entered_bit2826 == 'D_GND'):
        reg2_bit2826_value = 2
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    elif (Reg2_entered_bit2826 == 'R-divider output'):
        reg2_bit2826_value = 3
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    elif (Reg2_entered_bit2826 == 'N-divider output'):
        reg2_bit2826_value = 4
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    elif (Reg2_entered_bit2826 == 'Analog lock detect'):
        reg2_bit2826_value = 5
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    elif (Reg2_entered_bit2826 == 'Digital lock detect'):
        reg2_bit2826_value = 6
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    else:
        reg2_bit2826_value = 4
        bin_Reg2_bit2826 = bin(reg2_bit2826_value)[2:]
        bin_Reg2_bit2826 = bin_Reg2_bit2826.zfill(3)
        # update reg5 for MSB for MUX
        update_Reg5(event)

    # get bit25 value
    if (Reg2_entered_bit25 == 'Disable reference doubler'):
        reg2_bit25_value = 0
        bin_Reg2_bit25 = bin(reg2_bit25_value)[2:]
    else:
        reg2_bit25_value = 1
        bin_Reg2_bit25 = bin(reg2_bit25_value)[2:]

    # get bit24 value
    if (Reg2_entered_bit24 == 'Disable reference divided by 2'):
        reg2_bit24_value = 0
        bin_Reg2_bit24 = bin(reg2_bit24_value)[2:]
    else:
        reg2_bit24_value = 1
        bin_Reg2_bit24 = bin(reg2_bit24_value)[2:]

    # check if bits 23 - 14 are not empty and convert to binary with 10 bit size
    if Reg2_entered_bit2314 != '':
        bin_Reg2_bit2314 = bin(int(Reg2_entered_bit2314))[2:]
        bin_Reg2_bit2314 = bin_Reg2_bit2314.zfill(10)

    # get bit13 value
    if (Reg2_entered_bit13 == 'Disable double buffer'):
        reg2_bit13_value = 0
        bin_Reg2_bit13 = bin(reg2_bit13_value)[2:]
    else:
        reg2_bit13_value = 1
        bin_Reg2_bit13 = bin(reg2_bit13_value)[2:]

    # get bit 12 -9
    match Reg2_entered_bit1209:
        case "0.32":
            reg2_bit1209_value = 0
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209= bin_Reg2_bit1209.zfill(4)
        case "0.64":
            reg2_bit1209_value = 1
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "0.96":
            reg2_bit1209_value = 2
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "1.28":
            reg2_bit1209_value = 3
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "1.60":
            reg2_bit1209_value = 4
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "1.92":
            reg2_bit1209_value = 5
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "2.24":
            reg2_bit1209_value = 6
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "2.56":
            reg2_bit1209_value = 7
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "2.88":
            reg2_bit1209_value = 8
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "3.20":
            reg2_bit1209_value = 9
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "3.52":
            reg2_bit1209_value =10
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "3.84":
            reg2_bit1209_value = 11
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "4.16":
            reg2_bit1209_value = 12
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "4.48":
            reg2_bit1209_value = 13
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "4.80":
            reg2_bit1209_value = 14
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

        case "5.12":
            reg2_bit1209_value = 15
            bin_Reg2_bit1209 = bin(reg2_bit1209_value)[2:]
            bin_Reg2_bit1209 = bin_Reg2_bit1209.zfill(4)

    # get bit 8 value
    if (Reg2_entered_bit08 == 'Frac-N lock detect'):
        reg2_bit8_value = 0
        bin_Reg2_bit8 = bin(reg2_bit8_value)[2:]
    else:
        reg2_bit8_value = 1
        bin_Reg2_bit8 = bin(reg2_bit8_value)[2:]

    # get bit 7 value
    if (Reg2_entered_bit07 == '10 nS'):
        reg2_bit7_value = 0
        bin_Reg2_bit7 = bin(reg2_bit7_value)[2:]
    else:
        reg2_bit7_value = 1
        bin_Reg2_bit7 = bin(reg2_bit7_value)[2:]

    # get bit 6 value
    if (Reg2_entered_bit06 == 'Negative'):
        reg2_bit6_value = 0
        bin_Reg2_bit6 = bin(reg2_bit6_value)[2:]
    else:
        reg2_bit6_value =1
        bin_Reg2_bit6 = bin(reg2_bit6_value)[2:]

    # get bit 5 value
    if (Reg2_entered_bit05 == 'Normal mode'):
        reg2_bit5_value = 0
        bin_Reg2_bit5 = bin(reg2_bit5_value)[2:]
    else:
        reg2_bit5_value =1
        bin_Reg2_bit5 = bin(reg2_bit5_value)[2:]


    # get bit 4 value
    if (Reg2_entered_bit04 == 'Disabled'):
        reg2_bit4_value = 0
        bin_Reg2_bit4 = bin(reg2_bit4_value)[2:]
    else:
        reg2_bit4_value = 1
        bin_Reg2_bit4 = bin(reg2_bit4_value)[2:]

    # get bit 3 value
    if (Reg2_entered_bit03 == 'Normal operation'):
        reg2_bit3_value = 0
        bin_Reg2_bit3 = bin(reg2_bit3_value)[2:]
    else:
        reg2_bit3_value = 1
        bin_Reg2_bit3 = bin(reg2_bit3_value)[2:]

     #display register 2 values
    if (Reg2_entered_bit31 != '' and
            Reg2_entered_bit3029 != '' and
            Reg2_entered_bit2826 != '' and
            Reg2_entered_bit25 != '' and
            Reg2_entered_bit24 != '' and
            Reg2_entered_bit2314 != '' and
            Reg2_entered_bit13 != '' and
            Reg2_entered_bit1209 != '' and
            Reg2_entered_bit08 != '' and
            Reg2_entered_bit07 != '' and
            Reg2_entered_bit06 != '' and
            Reg2_entered_bit05 != '' and
            Reg2_entered_bit04 != '' and
            Reg2_entered_bit03 != ''):

        Reg2_bin = bin_Reg2_bit31 + bin_Reg2_bit3029 + bin_Reg2_bit2826 + bin_Reg2_bit25 + bin_Reg2_bit24 + bin_Reg2_bit2314 + bin_Reg2_bit13 + bin_Reg2_bit1209 + bin_Reg2_bit8 + bin_Reg2_bit7 + bin_Reg2_bit6 + bin_Reg2_bit5 + bin_Reg2_bit4 + bin_Reg2_bit3+"010"
        Reg2_binary_with_spaces = insert_space(Reg2_bin)
        #print(Reg2_binary_with_spaces)
        Reg2_decimal = int(Reg2_bin, 2)
        Reg2_hex = hex(Reg2_decimal)[2:]
        Reg2_hex=Reg2_hex.upper()
        #to show all 32 bits even if it is zeroes
        Reg2_hex=Reg2_hex.zfill(8)

        # update register 0 data in binary and hex format

        hex_reg2_text.set(Reg2_hex)
        bin_reg2_text.set(Reg2_binary_with_spaces)

def update_Reg3(event):
    Reg3_entered_bit3126 = Reg3_entry_bit3126.get()
    Reg3_entered_bit25 = combo_reg3_bit25.get()
    Reg3_entered_bit24 = combo_reg3_bit24.get()
    Reg3_entered_bit1615 =combo_reg3_bit1615.get()
    Reg3_entered_bit1403 = Reg3_entry_bit1403.get()

    # check if bits 31 - 26 are not empty and convert to binary with 6 bit size
    if Reg3_entered_bit3126 != '':
        bin_Reg3_bit3126 = bin(int(Reg3_entered_bit3126))[2:]
        bin_Reg3_bit3126 = bin_Reg3_bit3126.zfill(6)

    #get bit25 value
    if (Reg3_entered_bit25 == 'VAS enabled'):
        reg3_bit25_value = 0
        bin_Reg3_bit25 = bin(reg3_bit25_value)[2:]
    else:
        reg3_bit25_value = 1
        bin_Reg3_bit25 = bin(reg3_bit25_value)[2:]

    #get bit 24 value
    if (Reg3_entered_bit24 == 'disabled'):
        reg3_bit24_value = 0
        bin_Reg3_bit24 = bin(reg3_bit24_value)[2:]
    else:
        reg3_bit24_value =1
        bin_Reg3_bit24 = bin(reg3_bit24_value)[2:]

    #get bit 16 -15 value
    if (Reg3_entered_bit1615 == 'Clock divider off'):
        reg3_bit1615_value = 0
        bin_Reg3_bit1615 = bin(reg3_bit1615_value)[2:]
        bin_Reg3_bit1615 = bin_Reg3_bit1615.zfill(2)
    elif (Reg3_entered_bit1615 == 'Fast-lock enabled'):
        reg3_bit1615_value = 1
        bin_Reg3_bit1615 = bin(reg3_bit1615_value)[2:]
        bin_Reg3_bit1615 = bin_Reg3_bit1615.zfill(2)
    else:
        reg3_bit1615_value = 2
        bin_Reg3_bit1615 = bin(reg3_bit1615_value)[2:]
        bin_Reg3_bit1615 = bin_Reg3_bit1615.zfill(2)


    # check if bits 14- 3 are not empty and convert to binary with 12 bit size
    if Reg3_entered_bit1403 != '':
        bin_Reg3_bit1403 = bin(int(Reg3_entered_bit1403))[2:]
        bin_Reg3_bit1403 = bin_Reg3_bit1403.zfill(12)

  #display register 3 values
    if (Reg3_entered_bit3126 != '' and
            Reg3_entered_bit25 != '' and
            Reg3_entered_bit24 != '' and
            Reg3_entered_bit1615 != '' and
            Reg3_entered_bit1403 != ''):

        Reg3_bin = bin_Reg3_bit3126+bin_Reg3_bit25+bin_Reg3_bit24+"0000000"+bin_Reg3_bit1615+bin_Reg3_bit1403+"011"
        Reg3_binary_with_spaces = insert_space(Reg3_bin)
        print(Reg3_binary_with_spaces)
        Reg3_decimal = int(Reg3_bin, 2)
        Reg3_hex = hex(Reg3_decimal)[2:]
        Reg3_hex=Reg3_hex.upper()
        #to show all 32 bits even if it is zeroes
        Reg3_hex=Reg3_hex.zfill(8)

        # update register 0 data in binary and hex format

        hex_reg3_text.set(Reg3_hex)
        bin_reg3_text.set(Reg3_binary_with_spaces)

def update_Reg4(event):
    Reg4_entered_bit23 = combo_reg4_bit23.get()
    Reg4_entered_bit2220 = combo_reg4_bit2220.get()
    Reg4_entered_bit1912 = Reg4_entry_bit1912.get()
    Reg4_entered_bit09 = combo_reg4_bit09.get()
    Reg4_entered_bit08 = combo_reg4_bit08.get()
    Reg4_entered_bit0706 = combo_reg4_bit0706.get()
    Reg4_entered_bit05 = combo_reg4_bit05.get()
    Reg4_entered_bit0403 = combo_reg4_bit0403.get()

    #get bit23 value
    if (Reg4_entered_bit23 == 'Divided'):
        reg4_bit23_value = 0
        bin_Reg4_bit23 = bin(reg4_bit23_value)[2:]
    else:
        reg4_bit23_value = 1
        bin_Reg4_bit23 = bin(reg4_bit23_value)[2:]

    #get bit2220 value
    if (Reg4_entered_bit2220 == 'Divide by 1'):
        reg4_bit2220_value = 0
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    elif (Reg4_entered_bit2220 == 'Divide by 2'):
        reg4_bit2220_value = 1
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    elif (Reg4_entered_bit2220 == 'Divide by 4'):
        reg4_bit2220_value = 2
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    elif (Reg4_entered_bit2220 == 'Divide by 8'):
        reg4_bit2220_value = 3
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    elif (Reg4_entered_bit2220 == 'Divide by 16'):
        reg4_bit2220_value = 4
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    elif (Reg4_entered_bit2220 == 'Divide by 32'):
        reg4_bit2220_value = 5
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    elif (Reg4_entered_bit2220 == 'Divide by 64'):
        reg4_bit2220_value = 6
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)
    else:
        reg4_bit2220_value = 7
        bin_Reg4_bit2220 = bin(reg4_bit2220_value)[2:]
        bin_Reg4_bit2220=bin_Reg4_bit2220.zfill(3)

    # check if bits 31 - 26 are not empty and convert to binary with 6 bit size
    if Reg4_entered_bit1912 != '':
        bin_Reg4_bit1912 = bin(int(Reg4_entered_bit1912))[2:]
        bin_Reg4_bit1912LSB = bin_Reg4_bit1912.zfill(10)[2:]
        bin_Reg4_bit2524 = bin_Reg4_bit1912.zfill(10)[:2]
        #print(bin_Reg4_bit1912LSB)
        #print(bin_Reg4_bit2524)
        #print("type is:", type(bin_Reg4_bit1912LSB))

    #get bit9 value
    if (Reg4_entered_bit09 == 'VCO divided output'):
        reg4_bit09_value = 0
        bin_Reg4_bit09 = bin(reg4_bit09_value)[2:]
    else:
        reg4_bit09_value = 1
        bin_Reg4_bit09 = bin(reg4_bit09_value)[2:]

    #get bit8 value
    if (Reg4_entered_bit08 == 'Disabled'):
        reg4_bit08_value = 0
        bin_Reg4_bit08 = bin(reg4_bit08_value)[2:]
    else:
        reg4_bit08_value = 1
        bin_Reg4_bit08 = bin(reg4_bit08_value)[2:]

    #get bit 7 - 6 value
    if (Reg4_entered_bit0706 == '-4 dB'):
        reg4_bit0706_value = 0
        bin_Reg4_bit0706 = bin(reg4_bit0706_value)[2:]
        bin_Reg4_bit0706 = bin_Reg4_bit0706.zfill(2)
    elif (Reg4_entered_bit0706 == '-1 dB'):
        reg4_bit0706_value = 1
        bin_Reg4_bit0706 = bin(reg4_bit0706_value)[2:]
        bin_Reg4_bit0706 = bin_Reg4_bit0706.zfill(2)
    elif (Reg4_entered_bit0706 == '+2 dB'):
        reg4_bit0706_value = 2
        bin_Reg4_bit0706 = bin(reg4_bit0706_value)[2:]
        bin_Reg4_bit0706 = bin_Reg4_bit0706.zfill(2)
    else:
        reg4_bit0706_value = 3
        bin_Reg4_bit0706 = bin(reg4_bit0706_value)[2:]
        bin_Reg4_bit0706 = bin_Reg4_bit0706.zfill(2)

    #get bit5 value
    if (Reg4_entered_bit05 == 'Disabled'):
        reg4_bit05_value = 0
        bin_Reg4_bit05 = bin(reg4_bit05_value)[2:]
    else:
        reg4_bit05_value = 1
        bin_Reg4_bit05 = bin(reg4_bit05_value)[2:]

    #get bit 4 - 3 value
    if (Reg4_entered_bit0403 == '-4 dB'):
        reg4_bit0403_value = 0
        bin_Reg4_bit0403 = bin(reg4_bit0403_value)[2:]
        bin_Reg4_bit0403 = bin_Reg4_bit0403.zfill(2)
    elif (Reg4_entered_bit0403 == '-1 dB'):
        reg4_bit0403_value = 1
        bin_Reg4_bit0403 = bin(reg4_bit0403_value)[2:]
        bin_Reg4_bit0403 = bin_Reg4_bit0403.zfill(2)
    elif (Reg4_entered_bit0403 == '+2 dB'):
        reg4_bit0403_value = 2
        bin_Reg4_bit0403 = bin(reg4_bit0403_value)[2:]
        bin_Reg4_bit0403 = bin_Reg4_bit0403.zfill(2)
    else:
        reg4_bit0403_value = 3
        bin_Reg4_bit0403 = bin(reg4_bit0403_value)[2:]
        bin_Reg4_bit0403 = bin_Reg4_bit0403.zfill(2)



  #display register 3 values
    if (Reg4_entered_bit23 != '' and
            Reg4_entered_bit2220 != '' and
            Reg4_entered_bit1912 != '' and
            Reg4_entered_bit09 != '' and
            Reg4_entered_bit08 != '' and
            Reg4_entered_bit0706 != '' and
            Reg4_entered_bit05 != '' and
            Reg4_entered_bit0403 != ''):

        Reg4_bin = "000000"+bin_Reg4_bit2524+bin_Reg4_bit23+bin_Reg4_bit2220+bin_Reg4_bit1912LSB+"00"+bin_Reg4_bit09+bin_Reg4_bit08+bin_Reg4_bit0706+bin_Reg4_bit05+bin_Reg4_bit0403+"100"
        Reg4_binary_with_spaces = insert_space(Reg4_bin)
        #print(Reg4_binary_with_spaces)
        Reg4_decimal = int(Reg4_bin, 2)
        Reg4_hex = hex(Reg4_decimal)[2:]
        Reg4_hex=Reg4_hex.upper()
        #to show all 32 bits even if it is zeroes
        Reg4_hex=Reg4_hex.zfill(8)

        # update register 0 data in binary and hex format

        hex_reg4_text.set(Reg4_hex)
        bin_reg4_text.set(Reg4_binary_with_spaces)

def update_Reg5(event):
    Reg5_entered_bit24 = combo_reg5_bit24.get()
    Reg5_entered_bit2322 = combo_reg5_bit2322.get()
    Reg5_entered_bit18= combo_reg2_bit2826.get() #get value from reigester 2

    #get bit24 value
    if (Reg5_entered_bit24 == 'Set Frac-N'):
        reg5_bit24_value = 0
        bin_Reg5_bit24 = bin(reg5_bit24_value)[2:]
    else:
        reg5_bit24_value = 1
        bin_Reg5_bit24 = bin(reg5_bit24_value)[2:]


    #get bit 23 -22 value
    if (Reg5_entered_bit2322 == 'Low'):
        reg5_bit2322_value = 0
        bin_Reg5_bit2322 = bin(reg5_bit2322_value)[2:]
        bin_Reg5_bit2322=bin_Reg5_bit2322.zfill(2)
    elif (Reg5_entered_bit2322 == 'Digital lock'):
        reg5_bit2322_value = 1
        bin_Reg5_bit2322 = bin(reg5_bit2322_value)[2:]
        bin_Reg5_bit2322 = bin_Reg5_bit2322.zfill(2)
    elif (Reg5_entered_bit2322 == 'Analog lock'):
        reg5_bit2322_value = 2
        bin_Reg5_bit2322 = bin(reg5_bit2322_value)[2:]
        bin_Reg5_bit2322 = bin_Reg5_bit2322.zfill(2)
    else:
        reg5_bit2322_value = 3
        bin_Reg5_bit2322 = bin(reg5_bit2322_value)[2:]
        bin_Reg5_bit2322 = bin_Reg5_bit2322.zfill(2)

    #get bit18 value
    if (Reg5_entered_bit18 == 'Read Register 6'):
        reg5_bit18_value = 1
        bin_Reg5_bit18 = bin(reg5_bit18_value)[2:]
    else:
        reg5_bit18_value = 0
        bin_Reg5_bit18 = bin(reg5_bit18_value)[2:]

  #display register 5 values
    if (Reg5_entered_bit24 != '' and
            Reg5_entered_bit2322 != ''):
        Reg5_bin = "0000000"+bin_Reg5_bit24+bin_Reg5_bit2322+"000"+bin_Reg5_bit18+"000000000000000"+"101"
        Reg5_binary_with_spaces = insert_space(Reg5_bin)
        #print(Reg5_binary_with_spaces)
        Reg5_decimal = int(Reg5_bin, 2)
        Reg5_hex = hex(Reg5_decimal)[2:]
        Reg5_hex=Reg5_hex.upper()
        #to show all 32 bits even if it is zeroes
        Reg5_hex=Reg5_hex.zfill(8)

        # update register 0 data in binary and hex format

        hex_reg5_text.set(Reg5_hex)
        bin_reg5_text.set(Reg5_binary_with_spaces)

def update_RF_clc(event):
    # print(event)
    RF_entered = Rf_desired_entry.get()
    Ref_clk_sel=combo_Ref_clk.get()
    FB_sel=combo_FB_RFclc.get()

    if(RF_entered != ''  ):
        match RF_entered:
            case _ if int(RF_entered) < 46:
                DIVA_calc=128
            case _ if int(RF_entered) >= 46 and int(RF_entered) < 93 :
                DIVA_calc=64
            case _ if int(RF_entered) >= 93 and int(RF_entered) < 187 :
                DIVA_calc=32
            case _ if int(RF_entered) >= 187 and int(RF_entered) < 375 :
                DIVA_calc=16
            case _ if int(RF_entered) >= 375 and int(RF_entered) < 750 :
                DIVA_calc=8
            case _ if int(RF_entered) >= 750 and int(RF_entered) < 1500 :
                DIVA_calc=4
            case _ if int(RF_entered) >= 1500 and int(RF_entered) < 3000 :
                DIVA_calc=2
            case _ if int(RF_entered) >= 1500 and int(RF_entered) < 3000 :
                DIVA_calc=2
            case default:
                DIVA_calc=1


    # check if bit 31 not empty and update its value
    if (RF_entered != '' and FB_sel == 'Fundamental'  and Ref_clk_sel != '' ):
        fvco= int(RF_entered)* DIVA_calc
        N_val= fvco/int(Ref_clk_sel)
    elif (RF_entered != '' and FB_sel == 'Divided'  and Ref_clk_sel != '' and  DIVA_calc <= 16 ):
        fvco = int(RF_entered) * DIVA_calc
        N_val = (fvco / int(Ref_clk_sel))/DIVA_calc
    elif (RF_entered != '' and FB_sel == 'Divided'  and Ref_clk_sel != '' and  DIVA_calc > 16 ):
        fvco = int(RF_entered) * DIVA_calc
        N_val = (fvco / int(Ref_clk_sel))/16

    #update value
    if (RF_entered != '' and Ref_clk_sel != '' and FB_sel != ''):
        INT_value.set(N_val)
        DIVA_value.set(DIVA_calc)

window = tk.Tk()
# window.config(width=500, height=300)
window.minsize(1400, 650)
window.maxsize(1400, 650)
window.title("Max2870")
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
# set frame for Reg0

##############################################
#Register 0
##############################################


frame_reg0 = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=300,
                      height=220,
                      bg="white")
frame_reg0.grid(row=1, column=1, padx=5, pady=10)
reg0 = tk.Label(master=frame_reg0, text="Register 0", bg="white", font=("Helvetica", 12,"bold"))
# place Register 0 label in two merged column
reg0.grid(row=1, column=1, columnspan=2)
# bit 31
reg0_bit31 = tk.Label(master=frame_reg0, text="Int or Frac: ", bg="white", pady=5)
reg0_bit31.grid(row=2, column=1)
combo_reg0_bit31 = ttk.Combobox(master=frame_reg0, state="readonly", values=["Integer N", "Fractional N"])
combo_reg0_bit31.grid(row=2, column=2,sticky="w")
combo_reg0_bit31.current(0)
combo_reg0_bit31.bind("<<ComboboxSelected>>", update_Reg0)
# bit 30:15
reg0_bit3015_warning = tk.Label(master=frame_reg0, text="Integer value must be: (INT : 16 - 65535), and (FRAC: 19 - 4091) ", bg="white",fg="gray",font=("Helvetica", 8,"bold"), pady=2)
reg0_bit3015_warning.grid(row=3, column=1,columnspan=2)
reg0_bit3015 = tk.Label(master=frame_reg0, text="Integer value: ", bg="white", pady=5)
reg0_bit3015.grid(row=4, column=1)
Reg0_entry_bit3015 = tk.Entry(master=frame_reg0)
Reg0_entry_bit3015.bind("<KeyRelease>", update_Reg0)
Reg0_entry_bit3015.grid(row=4, column=2,sticky="w")
# bit 14:3
reg0_bit1403_warning = tk.Label(master=frame_reg0, text="Fractional value must be : 0 - 4095 ",font=("Helvetica", 8,"bold"), bg="white",fg="gray", pady=2)
reg0_bit1403_warning.grid(row=5, column=1,columnspan=2)
Reg0_bit1403 = tk.Label(master=frame_reg0, text="Fractional value: ", bg="white", pady=5)
Reg0_bit1403.grid(row=6, column=1)
Reg0_entry_bit1403 = tk.Entry(master=frame_reg0)
Reg0_entry_bit1403.insert(0, "0")
Reg0_entry_bit1403.bind("<KeyRelease>", update_Reg0)
Reg0_entry_bit1403.grid(row=6, column=2,sticky="w")
#display register 0 values
reg0_display_bin_label = tk.Label(master=frame_reg0, text="Register 0 binary value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg0_display_bin_label.grid(row=7, column=1, columnspan=2)
#reg0_display_box = tk.Label(master=frame_reg0, text="", width=36, font=('Helvetica', 14), bg="white")
#reg0_display_box.grid(row=8, column=1, columnspan=2)

bin_reg0_text=tk.StringVar()
reg0_display_bin=tk.Entry(master=frame_reg0,
                          state='readonly',
                          bd=0,
                          bg="white",
                          justify="center",
                          font=("Helvetica", 12,"bold"),
                          textvariable=bin_reg0_text,
                          width=36)

reg0_display_bin.grid(row=8, column=1, columnspan=2,padx=5)

#create label for regiter0 hex
reg0_display_hex_label = tk.Label(master=frame_reg0, text="Register 0 Hex value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg0_display_hex_label.grid(row=9, column=1, columnspan=2)
#create display for regiter0 hex. entery was used instead of label so the user can copy the value from the netry box
hex_reg0_text=tk.StringVar()
reg0_display_hex_entry = tk.Entry(master=frame_reg0,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=hex_reg0_text)
reg0_display_hex_entry.grid(row=10, column=1, columnspan=2,pady=5)

#################################################

##############################################
#Register 1
##############################################
# set frame for Reg0
frame_reg1 = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=300,
                      height=600,
                      bg="white")
frame_reg1.grid(row=2, column=1, padx=5, pady=0,sticky='n')

reg1 = tk.Label(master=frame_reg1, text="Register 1", bg="white", font=("Helvetica", 12,"bold"))
# place Register 0 label in two merged column
reg1.grid(row=1, column=1, columnspan=2)

# bit 31
reg1_bit31 = tk.Label(master=frame_reg1, text="CPOC: ", bg="white", pady=5)
reg1_bit31.grid(row=2, column=1)
combo_reg1_bit31 = ttk.Combobox(master=frame_reg1, state="readonly", values=["Disable clamping", "Enable clamping"])
combo_reg1_bit31.current(1)
combo_reg1_bit31.grid(row=2, column=2,sticky="w")
combo_reg1_bit31.bind("<<ComboboxSelected>>", update_Reg1)
# bit 30:29
reg1_bit3029 = tk.Label(master=frame_reg1, text="CPL: ", bg="white", pady=5)
reg1_bit3029.grid(row=3, column=1)
combo_reg1_bit3029 = ttk.Combobox(master=frame_reg1, state="readonly", values=["Disable CP (INT)", "Enable CP (FRAC)"])
combo_reg1_bit3029.current(0)
combo_reg1_bit3029.grid(row=3, column=2, sticky="w")
combo_reg1_bit3029.bind("<<ComboboxSelected>>", update_Reg1)
# bit 28:27
reg1_bit2827 = tk.Label(master=frame_reg1, text="CPT: ", bg="white", pady=5)
reg1_bit2827.grid(row=4, column=1)
combo_reg1_bit2827 = ttk.Combobox(master=frame_reg1, state="readonly", values=["Normal mode", "Source mode","Sink mode"])
combo_reg1_bit2827.current(0)
combo_reg1_bit2827.grid(row=4, column=2, sticky="w")
combo_reg1_bit2827.bind("<<ComboboxSelected>>", update_Reg1)
# bit 26:15
reg1_bit2615_warning = tk.Label(master=frame_reg1,
                                text="Phase value must be: 0 - 4095 ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg1_bit2615_warning.grid(row=5, column=1,columnspan=2)
reg1_bit2615 = tk.Label(master=frame_reg1, text="Phase value: ", bg="white", pady=5)
reg1_bit2615.grid(row=6, column=1)
Reg1_entry_bit2615 = tk.Entry(master=frame_reg1)
Reg1_entry_bit2615.insert(0, "0")
Reg1_entry_bit2615.bind("<KeyRelease>", update_Reg1)
Reg1_entry_bit2615.grid(row=6, column=2,sticky="w")
# bit 14:3
reg1_bit1403_warning = tk.Label(master=frame_reg1,
                                text="Mod value must be: 2 - 4095 ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg1_bit1403_warning.grid(row=7, column=1,columnspan=2)
reg1_bit1403 = tk.Label(master=frame_reg1, text="Mod value: ", bg="white", pady=5)
reg1_bit1403.grid(row=8, column=1)
Reg1_entry_bit1403 = tk.Entry(master=frame_reg1)
Reg1_entry_bit1403.insert(0, "2")
Reg1_entry_bit1403.bind("<KeyRelease>", update_Reg1)
Reg1_entry_bit1403.grid(row=8, column=2,sticky="w")

#create label for display register 1 values
reg1_display_bin_label = tk.Label(master=frame_reg1, text="Register 1 binary value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg1_display_bin_label.grid(row=9, column=1, columnspan=2)
frame_reg1.bind('<Double 1>', update_Reg1)
#display Register 1 binary values in entry box so user can copy the value
bin_reg1_text=tk.StringVar()
reg1_display_bin=tk.Entry(master=frame_reg1,
                          state='readonly',
                          bd=0,
                          bg="white",
                          justify="center",
                          font=("Helvetica", 12,"bold"),
                          textvariable=bin_reg1_text,
                          width=36)
reg1_display_bin.grid(row=10, column=1, columnspan=2,padx=5)

#create label for regiter1 hex
reg1_display_hex_label = tk.Label(master=frame_reg1,
                                  text="Register 1 Hex value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
reg1_display_hex_label.grid(row=11, column=1, columnspan=2)
#create display for regiter1 hex. entery was used instead of label so the user can copy the value from the netry box
hex_reg1_text=tk.StringVar()
reg1_display_hex_entry = tk.Entry(master=frame_reg1,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=hex_reg1_text)
reg1_display_hex_entry.grid(row=12, column=1, columnspan=2,pady=5)


##############################################
#Register 2
##############################################
# set frame for Reg2
frame_reg2 = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=300,
                      height=600,
                      bg="white")
frame_reg2.grid(row=1, column=2, padx=5, pady=10, rowspan=2,sticky="n")
reg2 = tk.Label(master=frame_reg2, text="Register 2", bg="white", font=("Helvetica", 12,"bold"))
# place Register 0 label in two merged column
reg2.grid(row=1, column=1, columnspan=2)

# bit 31
reg2_bit31 = tk.Label(master=frame_reg2, text="LDS: ", bg="white", pady=5)
reg2_bit31.grid(row=2, column=1)
combo_reg2_bit31 = ttk.Combobox(master=frame_reg2, state="readonly", values=["f_PFD < 32 MHz", "f_PFD > 32 MHz"])
combo_reg2_bit31.grid(row=2, column=2,sticky="w")
combo_reg2_bit31.current(0)
combo_reg2_bit31.bind("<<ComboboxSelected>>", update_Reg2)

# bit 30 - 29
reg2_bit3029 = tk.Label(master=frame_reg2, text="SDN: ", bg="white", pady=5)
reg2_bit3029.grid(row=3, column=1)
combo_reg2_bit3029 = ttk.Combobox(master=frame_reg2, state="readonly", values=["Low noise mode", "Low spur mode 1", "Low spur mode 2"])
combo_reg2_bit3029.grid(row=3, column=2,sticky="w")
combo_reg2_bit3029.current(0)
combo_reg2_bit3029.bind("<<ComboboxSelected>>", update_Reg2)

#bit 28 - 26
reg2_bit2826 = tk.Label(master=frame_reg2, text="MUX: ", bg="white", pady=5)
reg2_bit2826.grid(row=4, column=1)
combo_reg2_bit2826 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  values=["Three state output",
                                          "D_VDD",
                                          "D_GND",
                                          "R-divider output",
                                          "N-divider output",
                                          "Analog lock detect",
                                          "Digital lock detect",
                                          "Read Register 6"])
combo_reg2_bit2826.grid(row=4, column=2,sticky="w")
combo_reg2_bit2826.current(2)
combo_reg2_bit2826.bind("<<ComboboxSelected>>", update_Reg2)

#bit 25
reg2_bit25 = tk.Label(master=frame_reg2, text="DBR: ", bg="white", pady=5)
reg2_bit25.grid(row=5, column=1)
combo_reg2_bit25 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Disable reference doubler",
                                          "Enable reference doubler"])
combo_reg2_bit25.grid(row=5, column=2,sticky="w")
combo_reg2_bit25.current(0)
combo_reg2_bit25.bind("<<ComboboxSelected>>", update_Reg2)

#bit 24
reg2_bit24 = tk.Label(master=frame_reg2, text="RDIV2: ", bg="white", pady=5)
reg2_bit24.grid(row=6, column=1)
combo_reg2_bit24 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Disable reference divided by 2",
                                          "Enable reference divided by 2"])
combo_reg2_bit24.grid(row=6, column=2,sticky="w")
combo_reg2_bit24.current(0)
combo_reg2_bit24.bind("<<ComboboxSelected>>", update_Reg2)

#bit 23 - 14
reg2_bit2314_warning = tk.Label(master=frame_reg2,
                                text="Reference divider value must be: 1 - 1023 ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg2_bit2314_warning.grid(row=7, column=1,columnspan=2)
reg2_bit2314 = tk.Label(master=frame_reg2, text="Reference divider: ", bg="white", pady=5)
reg2_bit2314.grid(row=8, column=1)
Reg2_entry_bit2314 = tk.Entry(master=frame_reg2)
Reg2_entry_bit2314.insert(0, "0")
Reg2_entry_bit2314.bind("<KeyRelease>", update_Reg2)
Reg2_entry_bit2314.grid(row=8, column=2,sticky="w")

#bit 13
reg2_bit13 = tk.Label(master=frame_reg2, text="REG4DB: ", bg="white", pady=5)
reg2_bit13.grid(row=9, column=1)
combo_reg2_bit13 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Disable double buffer",
                                          "Enable double buffer"])
combo_reg2_bit13.grid(row=9, column=2,sticky="w")
combo_reg2_bit13.current(0)
combo_reg2_bit13.bind("<<ComboboxSelected>>", update_Reg2)

#bit 12 - 9
reg2_bit1209 = tk.Label(master=frame_reg2, text="Charge pump current: ", bg="white", pady=5)
reg2_bit1209.grid(row=10, column=1)
combo_reg2_bit1209 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["0.32",
                                          "0.64",
                                          "0.96",
                                          "1.28",
                                          "1.60",
                                          "1.92",
                                          "2.24",
                                          "2.56",
                                          "2.88",
                                          "3.20",
                                          "3.52",
                                          "3.84",
                                          "4.16",
                                          "4.48",
                                          "4.80",
                                          "5.12"])
combo_reg2_bit1209.grid(row=10, column=2,sticky="w")
combo_reg2_bit1209.current(0)
combo_reg2_bit1209.bind("<<ComboboxSelected>>", update_Reg2)

#bit 8
reg2_bit08 = tk.Label(master=frame_reg2, text="LD function: ", bg="white", pady=5)
reg2_bit08.grid(row=11, column=1)
combo_reg2_bit08 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Frac-N lock detect",
                                          "Int-N lock detect"])
combo_reg2_bit08.grid(row=11, column=2,sticky="w")
combo_reg2_bit08.current(1)
combo_reg2_bit08.bind("<<ComboboxSelected>>", update_Reg2)

#bit 7
reg2_bit07 = tk.Label(master=frame_reg2, text="LD precision: ", bg="white", pady=5)
reg2_bit07.grid(row=12, column=1)
combo_reg2_bit07 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["10 nS",
                                          "6 nS"])
combo_reg2_bit07.grid(row=12, column=2,sticky="w")
combo_reg2_bit07.current(0)
combo_reg2_bit07.bind("<<ComboboxSelected>>", update_Reg2)

#bit 6
reg2_bit06 = tk.Label(master=frame_reg2, text="PD polarity: ", bg="white", pady=5)
reg2_bit06.grid(row=13, column=1)
combo_reg2_bit06 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Negative",
                                          "Positive"])
combo_reg2_bit06.grid(row=13, column=2,sticky="w")
combo_reg2_bit06.current(1)
combo_reg2_bit06.bind("<<ComboboxSelected>>", update_Reg2)

#bit 5
reg2_bit05 = tk.Label(master=frame_reg2, text="Power mode: ", bg="white", pady=5)
reg2_bit05.grid(row=14, column=1)
combo_reg2_bit05 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Normal mode",
                                          "Shutdown"])
combo_reg2_bit05.grid(row=14, column=2,sticky="w")
combo_reg2_bit05.current(0)
combo_reg2_bit05.bind("<<ComboboxSelected>>", update_Reg2)

#bit 4
reg2_bit04 = tk.Label(master=frame_reg2, text="CP three-state: ", bg="white", pady=5)
reg2_bit04.grid(row=15, column=1)
combo_reg2_bit04 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Disabled",
                                          "Enabled"])
combo_reg2_bit04.grid(row=15, column=2,sticky="w")
combo_reg2_bit04.current(0)
combo_reg2_bit04.bind("<<ComboboxSelected>>", update_Reg2)

#bit 3
reg2_bit03 = tk.Label(master=frame_reg2, text="Counter reset: ", bg="white", pady=5)
reg2_bit03.grid(row=16, column=1)
combo_reg2_bit03 = ttk.Combobox(master=frame_reg2,
                                  state="readonly",
                                  width=25,
                                  values=["Normal operation",
                                          "R and N reset"])
combo_reg2_bit03.grid(row=16, column=2,sticky="w")
combo_reg2_bit03.bind("<<ComboboxSelected>>", update_Reg2)
combo_reg2_bit03.current(0)
frame_reg2.bind('<Double 1>', update_Reg2)
#create label for display register 2 values
reg2_display_bin_label = tk.Label(master=frame_reg2, text="Register 2 binary value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg2_display_bin_label.grid(row=17, column=1, columnspan=2)

#display Register 1 binary values in entry box so user can copy the value
bin_reg2_text=tk.StringVar()
reg2_display_bin=tk.Entry(master=frame_reg2,
                          state='readonly',
                          bd=0,
                          bg="white",
                          justify="center",
                          font=("Helvetica", 12,"bold"),
                          textvariable=bin_reg2_text,
                          width=36)
reg2_display_bin.grid(row=18, column=1, columnspan=2,padx=5)

#create label for regiter1 hex
reg2_display_hex_label = tk.Label(master=frame_reg2,
                                  text="Register 2 Hex value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
reg2_display_hex_label.grid(row=19, column=1, columnspan=2)
#create display for regiter2 hex. entery was used instead of label so the user can copy the value from the netry box
hex_reg2_text=tk.StringVar()
reg2_display_hex_entry = tk.Entry(master=frame_reg2,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=hex_reg2_text)
reg2_display_hex_entry.grid(row=20, column=1, columnspan=2,pady=5)


##############################################
#Register 3
##############################################
# set frame for Reg3
frame_reg3 = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=300,
                      height=600,
                      bg="white")
frame_reg3.grid(row=1, column=3, padx=5, pady=10, rowspan=2,sticky="n")

reg3 = tk.Label(master=frame_reg3, text="Register 3", bg="white", font=("Helvetica", 12,"bold"))
# place Register 3 label in two merged column
reg3.grid(row=1, column=1, columnspan=2)

# bit 31 - 26
reg3_bit3126_warning = tk.Label(master=frame_reg3,
                                text="VCO value must be: 0 - 63 ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg3_bit3126_warning.grid(row=2, column=1,columnspan=2)
reg3_bit3126 = tk.Label(master=frame_reg3, text="VCO value: ", bg="white", pady=5)
reg3_bit3126.grid(row=3, column=1)
Reg3_entry_bit3126 = tk.Entry(master=frame_reg3)
Reg3_entry_bit3126.insert(0, "0")
Reg3_entry_bit3126.bind("<KeyRelease>", update_Reg3)
Reg3_entry_bit3126.grid(row=3, column=2,sticky="w")

#bit 25
reg3_bit25 = tk.Label(master=frame_reg3, text="VAS SHDN: ", bg="white", pady=5)
reg3_bit25.grid(row=4, column=1)
combo_reg3_bit25 = ttk.Combobox(master=frame_reg3,
                                  state="readonly",
                                  width=15,
                                  values=["VAS enabled",
                                          "VAS disabled"])
combo_reg3_bit25.grid(row=4, column=2,sticky="w")
combo_reg3_bit25.current(0)
combo_reg3_bit25.bind("<<ComboboxSelected>>", update_Reg3)

#bit 24
reg3_bit24 = tk.Label(master=frame_reg3, text="RE-Tune: ", bg="white", pady=5)
reg3_bit24.grid(row=5, column=1)
combo_reg3_bit24 = ttk.Combobox(master=frame_reg3,
                                  state="readonly",
                                  width=15,
                                  values=["disabled",
                                          "enabled"])
combo_reg3_bit24.grid(row=5, column=2,sticky="w")
combo_reg3_bit24.current(0)
combo_reg3_bit24.bind("<<ComboboxSelected>>", update_Reg3)

#bit 16 -15
reg3_bit1615 = tk.Label(master=frame_reg3, text="CDM: ", bg="white", pady=5)
reg3_bit1615.grid(row=6, column=1)
combo_reg3_bit1615 = ttk.Combobox(master=frame_reg3,
                                  state="readonly",
                                  width=15,
                                  values=["Clock divider off","Fast-lock enabled","Phase mode"])
combo_reg3_bit1615.grid(row=6, column=2,sticky="w")
combo_reg3_bit1615.current(1)
combo_reg3_bit1615.bind("<<ComboboxSelected>>", update_Reg3)

#bit 14 - 3
reg3_bit1403_warning = tk.Label(master=frame_reg3,
                                text="CDIV value must be: 1 - 4095 ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg3_bit1403_warning.grid(row=7, column=1,columnspan=2)
reg3_bit1403 = tk.Label(master=frame_reg3, text="CDIV value: ", bg="white", pady=5)
reg3_bit1403.grid(row=8, column=1)
Reg3_entry_bit1403 = tk.Entry(master=frame_reg3)
Reg3_entry_bit1403.insert(0, "150")
Reg3_entry_bit1403.bind("<KeyRelease>", update_Reg3)
Reg3_entry_bit1403.grid(row=8, column=2,sticky="w")
frame_reg3.bind('<Double 1>', update_Reg3)

#create label for display register 2 values
reg3_display_bin_label = tk.Label(master=frame_reg3, text="Register 3 binary value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg3_display_bin_label.grid(row=9, column=1, columnspan=2)

#display Register 1 binary values in entry box so user can copy the value
bin_reg3_text=tk.StringVar()
reg3_display_bin=tk.Entry(master=frame_reg3,
                          state='readonly',
                          bd=0,
                          bg="white",
                          justify="center",
                          font=("Helvetica", 12,"bold"),
                          textvariable=bin_reg3_text,
                          width=36)
reg3_display_bin.grid(row=10, column=1, columnspan=2,padx=5)

#create label for regiter1 hex
reg3_display_hex_label = tk.Label(master=frame_reg3,
                                  text="Register 3 Hex value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
reg3_display_hex_label.grid(row=11, column=1, columnspan=2)
#create display for regiter2 hex. entery was used instead of label so the user can copy the value from the netry box
hex_reg3_text=tk.StringVar()
reg3_display_hex_entry = tk.Entry(master=frame_reg3,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=hex_reg3_text)
reg3_display_hex_entry.grid(row=12, column=1, columnspan=2,pady=5)

##############################################
#Register 4
##############################################
# set frame for Reg4
frame_reg4 = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=300,
                      height=650,
                      bg="white")
frame_reg4.grid(row=1, column=4, padx=5, pady=10, rowspan=2,sticky="n")

reg4 = tk.Label(master=frame_reg4, text="Register 4", bg="white", font=("Helvetica", 12,"bold"))
# place Register 4 label in two merged column
reg4.grid(row=1, column=1, columnspan=2)

#bit 23
reg4_bit23 = tk.Label(master=frame_reg4, text="FB: ", bg="white", pady=5)
reg4_bit23.grid(row=2, column=1)
combo_reg4_bit23 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["Divided",
                                          "Fundamental"])
combo_reg4_bit23.grid(row=2, column=2,sticky="w")
combo_reg4_bit23.current(1)
combo_reg4_bit23.bind("<<ComboboxSelected>>", update_Reg4)

#bit 22 - 20
reg4_bit2220 = tk.Label(master=frame_reg4, text="DIVA: ", bg="white", pady=5)
reg4_bit2220.grid(row=3, column=1)
combo_reg4_bit2220 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["Divide by 1","Divide by 2","Divide by 4","Divide by 8","Divide by 16"
                                          ,"Divide by 32","Divide by 64","Divide by 128"])
combo_reg4_bit2220.grid(row=3, column=2,sticky="w")
#combo_reg4_bit2220.current(0)
combo_reg4_bit2220.bind("<<ComboboxSelected>>", update_Reg4)

#bit 19 - 12
reg4_bit1912_warning = tk.Label(master=frame_reg4,
                                text="Band select must be: 1 - 1023 ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg4_bit1912_warning.grid(row=4, column=1,columnspan=2)
reg4_bit1912 = tk.Label(master=frame_reg4, text="Band Select: ", bg="white", pady=5)
reg4_bit1912.grid(row=5, column=1)
Reg4_entry_bit1912 = tk.Entry(master=frame_reg4)
Reg4_entry_bit1912.insert(0, "400")
Reg4_entry_bit1912.bind("<KeyRelease>", update_Reg4)
Reg4_entry_bit1912.grid(row=5, column=2,sticky="w")


#bit 9
reg4_bit09 = tk.Label(master=frame_reg4, text="BDIV: ", bg="white", pady=5)
reg4_bit09.grid(row=6, column=1)
combo_reg4_bit09 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["VCO divided output","VCO fundemental"])
combo_reg4_bit09.grid(row=6, column=2,sticky="w")
combo_reg4_bit09.current(0)
combo_reg4_bit09.bind("<<ComboboxSelected>>", update_Reg4)

#bit 8
reg4_bit08 = tk.Label(master=frame_reg4, text="RFB_EN: ", bg="white", pady=5)
reg4_bit08.grid(row=7, column=1)
combo_reg4_bit08 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["Disabled","Enabled"])
combo_reg4_bit08.grid(row=7, column=2,sticky="w")
combo_reg4_bit08.current(0)
combo_reg4_bit08.bind("<<ComboboxSelected>>", update_Reg4)

#bit 7 - 6
reg4_bit0706 = tk.Label(master=frame_reg4, text="BPWR: ", bg="white", pady=5)
reg4_bit0706.grid(row=8, column=1)
combo_reg4_bit0706 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["-4 dB","-1 dB","+2 dB","+5 dB"])
combo_reg4_bit0706.grid(row=8, column=2,sticky="w")
combo_reg4_bit0706.current(0)
combo_reg4_bit0706.bind("<<ComboboxSelected>>", update_Reg4)

#bit 5
reg4_bit05 = tk.Label(master=frame_reg4, text="RFA_EN: ", bg="white", pady=5)
reg4_bit05.grid(row=9, column=1)
combo_reg4_bit05 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["Disabled","Enabled"])
combo_reg4_bit05.grid(row=9, column=2,sticky="w")
combo_reg4_bit05.current(0)
combo_reg4_bit05.bind("<<ComboboxSelected>>", update_Reg4)


#bit 4 - 3
reg4_bit0403 = tk.Label(master=frame_reg4, text="APWR: ", bg="white", pady=5)
reg4_bit0403.grid(row=10, column=1)
combo_reg4_bit0403 = ttk.Combobox(master=frame_reg4,
                                  state="readonly",
                                  width=15,
                                  values=["-4 dB","-1 dB","+2 dB","+5 dB"])
combo_reg4_bit0403.grid(row=10, column=2,sticky="w")
combo_reg4_bit0403.current(0)
combo_reg4_bit0403.bind("<<ComboboxSelected>>", update_Reg4)

#create label for display register 4 values
reg4_display_bin_label = tk.Label(master=frame_reg4, text="Register 4 binary value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg4_display_bin_label.grid(row=11, column=1, columnspan=2)

#display Register 4 binary values in entry box so user can copy the value
bin_reg4_text=tk.StringVar()
reg4_display_bin_entry=tk.Entry(master=frame_reg4,
                          state='readonly',
                          bd=0,
                          bg="white",
                          justify="center",
                          font=("Helvetica", 12,"bold"),
                          textvariable=bin_reg4_text,
                          width=36)
reg4_display_bin_entry.grid(row=12, column=1, columnspan=2,padx=5)

#create label for regiter1 hex
reg4_display_hex_label = tk.Label(master=frame_reg4,
                                  text="Register 4 Hex value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
reg4_display_hex_label.grid(row=13, column=1, columnspan=2)
#create display for regiter4 hex. entery was used instead of label so the user can copy the value from the netry box
hex_reg4_text=tk.StringVar()
reg4_display_hex_entry = tk.Entry(master=frame_reg4,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=hex_reg4_text)
reg4_display_hex_entry.grid(row=14, column=1, columnspan=2,pady=5)


##############################################
#Register 5
##############################################
# set frame for Reg2
frame_reg5 = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=300,
                      height=600,
                      bg="white")
frame_reg5.grid(row=2, column=3, padx=5, pady=80, sticky="n ")

reg5 = tk.Label(master=frame_reg5, text="Register 5", bg="white", font=("Helvetica", 12,"bold"))
# place Register 5 label in two merged column
reg5.grid(row=1, column=1, columnspan=2)

# bit 24
reg5_bit24 = tk.Label(master=frame_reg5, text="F01: ", bg="white", pady=5)
reg5_bit24.grid(row=2, column=1)
combo_reg5_bit24 = ttk.Combobox(master=frame_reg5, state="readonly", values=["Set Frac-N", "Set Int-N"])
combo_reg5_bit24.grid(row=2, column=2,sticky="w")
combo_reg5_bit24.current(1)
combo_reg5_bit24.bind("<<ComboboxSelected>>", update_Reg5)

# bit 23 - 22
reg5_bit2322 = tk.Label(master=frame_reg5, text="LD: ", bg="white", pady=5)
reg5_bit2322.grid(row=3, column=1)
combo_reg5_bit2322 = ttk.Combobox(master=frame_reg5, state="readonly", values=["Low", "Digital lock","Analog lock", "High"])
combo_reg5_bit2322.grid(row=3, column=2,sticky="w")
combo_reg5_bit2322.bind("<<ComboboxSelected>>", update_Reg5)
combo_reg5_bit2322.current(1)
reg5_bit18_warning = tk.Label(master=frame_reg5,
                                text="Must complete MUX in Register 2 first ",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
reg5_bit18_warning.grid(row=4, column=1,columnspan=2)
frame_reg5.bind('<Double 1>', update_Reg5)
#create label for display register 4 values
reg5_display_bin_label = tk.Label(master=frame_reg5, text="Register 5 binary value:", bg="white",fg="green", font=("Helvetica", 10,"bold"),pady=3,justify="center")
reg5_display_bin_label.grid(row=5, column=1, columnspan=2)

#display Register 5 binary values in entry box so user can copy the value
bin_reg5_text=tk.StringVar()
reg5_display_bin_entry=tk.Entry(master=frame_reg5,
                          state='readonly',
                          bd=0,
                          bg="white",
                          justify="center",
                          font=("Helvetica", 12,"bold"),
                          textvariable=bin_reg5_text,
                          width=36)
reg5_display_bin_entry.grid(row=6, column=1, columnspan=2,padx=5)

#create label for regiter1 hex
reg5_display_hex_label = tk.Label(master=frame_reg5,
                                  text="Register 5 Hex value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
reg5_display_hex_label.grid(row=7, column=1, columnspan=2)
#create display for regiter4 hex. entery was used instead of label so the user can copy the value from the netry box
hex_reg5_text=tk.StringVar()
reg5_display_hex_entry = tk.Entry(master=frame_reg5,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=hex_reg5_text)
reg5_display_hex_entry.grid(row=8, column=1, columnspan=2,pady=5)

##############################################
#calc RFout
##############################################
# set frame for Rf output calc
frame_clc = tk.Frame(master=window,
                      highlightbackground="black",
                      highlightthickness=1,
                      width=200,
                      height=100,
                      bg="white")
frame_clc.grid(row=2, column=4, padx=5, pady=120, sticky="s ")

frq_out = tk.Label(master=frame_clc, text="Frequency Calc", bg="white", font=("Helvetica", 12,"bold"))
# place Register 5 label in two merged column
frq_out.grid(row=1, column=1, columnspan=2)

# bit 24
#RF_out = tk.Label(master=frame_clc, text="Rf out ", bg="white", pady=5)
#RF_out.grid(row=2, column=1)

RF_out_warning = tk.Label(master=frame_clc,
                                text="Rf out must be between 23 - 6000 MHz",
                                bg="white",
                                fg="gray",
                                font=("Helvetica", 8,"bold"),
                                pady=2)
RF_out_warning.grid(row=3, column=1,columnspan=2)
Rf_desired = tk.Label(master=frame_clc, text="RF out: ", bg="white", pady=5)
Rf_desired.grid(row=5, column=1)
Rf_desired_entry = tk.Entry(master=frame_clc)
Rf_desired_entry.grid(row=5, column=2,sticky="w")
Rf_desired_entry.bind("<KeyRelease>", update_RF_clc)

# Ref clock
Ref_clk = tk.Label(master=frame_clc, text="REF clock: ", bg="white", pady=5)
Ref_clk.grid(row=6, column=1)
combo_Ref_clk = ttk.Combobox(master=frame_clc, state="readonly", values=["20"])
combo_Ref_clk.grid(row=6, column=2,sticky="w")
combo_Ref_clk.bind("<<ComboboxSelected>>", update_RF_clc)

# Ref clock
FB_RFclc = tk.Label(master=frame_clc, text="FB: ", bg="white", pady=5)
FB_RFclc.grid(row=7, column=1)
combo_FB_RFclc = ttk.Combobox(master=frame_clc, state="readonly", values=["Divided",
          "Fundamental"])
combo_FB_RFclc.grid(row=7, column=2,sticky="w")
combo_FB_RFclc.bind("<<ComboboxSelected>>", update_RF_clc)

#create label for integer values
INT_value_clc = tk.Label(master=frame_clc,
                                  text="Integer value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
INT_value_clc.grid(row=8, column=1, sticky="w")
#create display for regiter4 hex. entery was used instead of label so the user can copy the value from the netry box
INT_value=tk.StringVar()
INT_value_entry = tk.Entry(master=frame_clc,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=INT_value)
INT_value_entry.grid(row=8, column=2, sticky="e")

#create label for Diva values
DIVA_value_clc = tk.Label(master=frame_clc,
                                  text="DIVA value:",
                                  bg="white",
                                  fg="green",
                                  font=("Helvetica", 10,"bold"),
                                  pady=3,
                                  justify="center")
DIVA_value_clc.grid(row=9, column=1, sticky="e")
#create display for Div value entery was used instead of label so the user can copy the value from the netry box
DIVA_value=tk.StringVar()
DIVA_value_entry = tk.Entry(master=frame_clc,
                                  state='readonly',
                                  highlightbackground="white",
                                  bd=0,
                                  bg='yellow',
                                  justify="center",
                                  font=("Helvetica", 12,"bold"),
                                  textvariable=DIVA_value)
DIVA_value_entry.grid(row=9, column=2, sticky="e")

window.mainloop()