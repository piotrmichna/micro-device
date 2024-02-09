# INSTALL

## configure tty terminal in linux

### download scripts/solvePermissions.sh

```bash
wget https://raw.githubusercontent.com/paulober/MicroPico/main/scripts/solvePermissions.sh
```

### maybe not required

```bash
chmod +x ./solvePermissions.sh
```

### run the script

```bash
./solvePermissions.sh
```

## nawiązanie połączenia z minicom terminala linuxowego po USB-RS485 z pico

```bash
minicom --device /dev/ttyUSB0 --baudrate 115200
```

## Struktura ramki

```text
^addr_odbiorcy;data;addr_nadacy$crc16\n\r
  ________________________________________________________
 | ADRES | FUNKCJA | LEN_DATA |   DANE   |   CRC  |  END  |
 *-------*---------*----------*----------*--------*-------*
 | 16bit |   8bit  |   32bit  | LEN*8bit | c*8bit | 16bit |
  --------------------------------------------------------
```

## Procedura dzałania urzadzenia master

### [ START ]

* inicjalizacja
* załadowanie konfiguracji z pliku
* wyszukanie urządzeń w sieci RS485
* pobranie urządzeń z GUI
  * synchronizacja urządzeń z danymi urzadzeń gui
