# -----------------
#   UART rs485
# -----------------
UART_ID = 0
TX_PIN = 0
RX_PIN = 1
FLOW_PIN = 2
ULED_PIN = "LED"

BAUDRATE = 115200
# BAUDRATE = 9600
BITS = 8
BIT_STOP = 1
MP_MASTER = True


# -----------------
#   DEVICE
# -----------------
SN = '1'
DEVICE_TYP = 'PM-MSR-WR'

DEVICE_DEFAULT_DATA = {'name': f'PM-buss-master-{SN}',
                       'dev_id': None,
                       'rid': None,
                       'addr': '0xfe',
                       'status': 0,
                       'led_pin': 'LED',
                       'master': True,
                       'parent': None,
                       }