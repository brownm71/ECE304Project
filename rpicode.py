import time
import spidev
from gpiozero import Button, LED

# Create spi objects
spi1 = spidev.SpiDev()
spi2 = spidev.SpiDev()
# Open spi1 bus 0, device 0 and 1 (for first potentiometer, use CE0)
spi1.open(0, 0)
spi2.open(0,1)

# Set spi1 speed and mode
spi1.max_speed_hz = 10 * 10**5  # Max speed in Hz
spi1.mode = 0  # spi1 mode 0 (CPOL=0, CPHA=0)



# Function to set the tap position on the AD8403
def set_potentiometer(tap_position, cs_pin, addr):
    # Ensure the tap position is within the range (0 to 255)
    if tap_position < 0 or tap_position > 255:
        raise ValueError("Tap position must be between 0 and 255")

    # Select the correct CS pin (device 0 or device 1)
    if(cs_pin == 0 ):
    # Send the command to the AD8403 (split into high and low bytes)
        spi1.xfer2([addr, tap_position])
    else:
        spi2.xfer2([addr, tap_position])

# Define buttons with pins
button1 = Button(14)
button2 = Button(3)
button3 = Button(4)
button4 = Button(17)
button5 = Button(27)

Rst1 = LED(20)
Rst2 = LED(21)
shdwn1 = LED(12)
shdwn2 = LED(16)



shdwn1.on()
shdwn2.on()
time.sleep(0.1)

Rst1.off()
Rst2.off()
time.sleep(0.1)
Rst1.on()
Rst2.on()

## 0.2 microFarad
## 1.44 / ((Ra + 2Rb) * C) = Frequency
## (Ra + Rb) / (Ra + 2Rb) = duty cycle

while (True):
    
    if (button1.is_active):
        set_potentiometer(70, 0, 0) # Play C5 70
        set_potentiometer(141, 0, 1) # 141

        
    if (button2.is_active):
        set_potentiometer(63, 0, 0)
        set_potentiometer(126, 0, 1)
        
    if (button3.is_active):
        set_potentiometer(56, 0, 0)
        set_potentiometer(112, 0, 1)
        
    if (button4.is_active):
        set_potentiometer(53, 0, 0)
        set_potentiometer(106, 0, 1)

    if (button5.is_active):
        set_potentiometer(47, 0, 0)
        set_potentiometer(94, 0, 1)



# Close spi1 connection
spi1.close()

