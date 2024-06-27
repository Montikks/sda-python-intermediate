# Napis program, ktory bude kazdu sekundu vypisovat
# f'Python {i} initiated...' pre i od 0 do nekonecna.
# Ak uzivatel stlaci v konzoli ctrl+c, cim sa vyhodi `KeyboardInterrupt` vynimka,
# program vypise 'You cannot stop me that easily!'
# Je vhodne pouzit napriklad `time.sleep(1)` (`import time`), aby program cakal 1 sekundu.

# Ako potom program vypnete?
# Ostava ako uloha pre pozornych citatelov






import time

i = 0
stop_attempts = 0  # Počet pokusů o zastavení

while True:
    try:
        print(f'Python {i} initiated...')
        i += 1
        time.sleep(1)
    except KeyboardInterrupt:
        if stop_attempts == 0:
            print('You cannot stop me that easily!')
            stop_attempts += 1
        else:
            print('Alright, you win. Stopping the program.')
            break

print('Program has ended.')



