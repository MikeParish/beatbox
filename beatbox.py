#!/usr/bin/python

import pygame
import spidev
import time

#pre-initialize pygame.mixer with a smaller buffer size to lessen sound lag
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
    
#open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

def readChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

#define sensor channels
swt_channel_0 = 0
swt_channel_1 = 1
swt_channel_2 = 2

#define delay between readings
delay = 0.05

while True:
    #read switch state
    swt_val_0 = readChannel(swt_channel_0)
    swt_val_1 = readChannel(swt_channel_1)
    swt_val_2 = readChannel(swt_channel_2)
    #when not pressed value read is 1023 when using MCP3008 10-bit ADC (3.3V or 5V)
    if swt_val_0 < 1010:
        #kick
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("drum_bass_hard.wav"))
        print("kick = {}".format(swt_val_0))
    if swt_val_1 < 1010:
        #snare
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("drum_snare_hard.wav"))
        print("snare = {}".format(swt_val_1))
    if swt_val_2 < 1010:
        #hihat
        pygame.mixer.Channel(2).play(pygame.mixer.Sound("drum_cymbal_closed.wav"))
        print("hihat = {}".format(swt_val_2))
    time.sleep(delay)
