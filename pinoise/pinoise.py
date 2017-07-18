import pygame
from gpiozero import Button, LED

pygame.init()


buttons = {
           "BTN1": Button(17)
           "BTN2": Button(27)
           "BTN3": Button(22)
           "BTN4": Button(10)
           }

leds = {
        "LED1": LED(5)
        "LED2": LED(6)
        "LED3": LED(13)
        "LED4": LED(19)
        }

# testing portion
my_sound = pygame.mixer.Sound("path/mysound.wav")
my_sound.play()