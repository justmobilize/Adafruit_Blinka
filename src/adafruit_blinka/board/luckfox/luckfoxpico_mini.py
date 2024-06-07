# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Lockfox Pico Mini."""

from adafruit_blinka.microcontroller.rockchip.rv1106 import pin

G42 = pin.GPIO1_B2
G43 = pin.GPIO1_B3
G48 = pin.GPIO1_C0 # This port is in use as CS0. This port is not available.
G49 = pin.GPIO1_C1
G50 = pin.GPIO1_C2
G51 = pin.GPIO1_C3
G52 = pin.GPIO1_C4
G53 = pin.GPIO1_C5
G56 = pin.GPIO1_D0
G57 = pin.GPIO1_D1
G58 = pin.GPIO1_D2
G59 = pin.GPIO1_D3
G54 = pin.GPIO1_C6
G55 = pin.GPIO1_C7
G4 = pin.GPIO0_A4

# UART
UART3_TX = pin.UART3_TX_M1
UART3_RX = pin.UART3_RX_M1
UART4_TX = pin.UART4_TX_M1
UART4_RX = pin.UART4_RX_M1

# Default UART
TX = UART3_TX
RX = UART3_RX
TXD = UART3_TX
RXD = UART3_RX

# I2C
I2C3_SCL = pin.I2C3_SCL_M1
I2C3_SDA = pin.I2C3_SDA_M1

# Default I2C
SCL = I2C3_SCL
SDA = I2C3_SDA

# SPI
SPI0_MISO = pin.SPI0_MISO_M0
SPI0_MOSI = pin.SPI0_MOSI_M0
SPI0_SCLK = pin.SPI0_CLK_M0
SPI0_CS0 = pin.SPI0_CS0_M0
SPI0_CS1 = pin.SPI0_CS1_M0

# Default SPI
MISO = SPI0_MISO
MOSI = SPI0_MOSI
SCLK = SPI0_SCLK

# PWM
PWM10 = pin.PWM10
PWM11 = pin.PWM11

# ADC
ADC_IN0 = pin.ADC_IN0
ADC_IN1 = pin.ADC_IN1
