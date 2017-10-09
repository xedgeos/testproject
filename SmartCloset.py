import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

def start():
    GPIO.input(21)
    GPIO.output(21, GPIO.LOW)
def stop():
    GPIO.input(21)
    GPIO.output(21, GPIO.HIGH)
def read():
     
    import binascii
    import socket
    import time

    import Adafruit_PN532 as PN532
    #import mcpi.minecraft as minecraft

    import mcpi_data


    # PN532 configuration for a Raspberry Pi:
    CS   = 18
    MOSI = 23
    MISO = 24
    SCLK = 25

    # Configure the key to use for writing to the MiFare card.  You probably don't
    # need to change this from the default below unless you know your card has a
    # different key associated with it.
    CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

    # Number of seconds to delay after building a block.  Good for slowing down the
    # update rate to prevent flooding new blocks into the world.
    MAX_UPDATE_SEC = 0.2

    # Create and initialize an instance of the PN532 class.
    pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
    pn532.begin()
    pn532.SAM_configuration()

    print('Tag listener')
    print('')
    print('Waiting for MiFare card...')
    while True:
        # Wait for a card to be available.
        uid = pn532.read_passive_target()
        # Try again if no card found.
        if uid is None:
            continue
        # Found a card, now try to read block 4 to detect the block type.
        print('Found card with UID 0x{0}'.format(binascii.hexlify(uid)))
        # Authenticate and read block 4.
        if not pn532.mifare_classic_authenticate_block(uid, 4, PN532.MIFARE_CMD_AUTH_B,
                                                       CARD_KEY):
            print('Failed to authenticate with card!')
            continue
        data = pn532.mifare_classic_read_block(4)
        if data is None:
            print('Failed to read data from card!')
            continue
        # Check if card has Minecraft block data by looking for header 'MCPI'
        if data[0:4] != b'MCPI':
            print('Card is not written with tag data!')
            continue
        # Parse out the block type and subtype.
        block_id = data[4]
        
        # Find the tag name (it's ugly to search for it, but there are less than 100).
        for block in mcpi_data.BLOCKS:
            if block[1] == block_id:
                block_name = block[0]
                print('Found tag!')
                return block_name
                break
        
    
    
    
    

start()
archivo = open("/home/pi/Desktop/SmartClosetApp/tag.txt", "r")
contenido = archivo.read()
print contenido
archivo.close()
while True: 
    if (contenido == "1"):
        id = read()
        if(id == "1"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "2"):
        id = read()
        if(id == "2"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "3"):
        id = read()
        if(id == "3"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "4"):
        id = read()
        if(id == "4"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "5"):
        id = read()
        if(id == "5"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "6"):
        id = read()
        if(id == "6"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "7"):
        id = read()
        if(id == "7"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "8"):
        id = read()
        if(id == "8"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "9"):
        id = read()
        if(id == "9"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "10"):
        id = read()
        if(id == "10"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "11"):
        id = read()
        if(id == "11"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "12"):
        id = read()
        if(id == "12"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "13"):
        id = read()
        if(id == "13"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "14"):
        id = read()
        if(id == "14"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "15"):
        id = read()
        if(id == "15"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
        
    elif(contenido == "16"):
        id = read()
        if(id == "16"):
            archivo = open ("/home/pi/Desktop/SmartClosetApp/tag.txt","w")
            contenido = archivo.write("")
            print contenido
            stop()
            break
