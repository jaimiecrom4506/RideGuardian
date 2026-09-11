import time
print("RideGuardian starting")
print("Possible crash detected")
cancel = input("Type CANCEL to stop SOS or press ENTER to continue: ")
if cancel.strip().lower() == "cancel"
: print("SOS cancelled. Rider is safe.")
        else:
         print("Emergency countdown starting")
         for seconds in range(10, 0, -1):
            print(f"SOS in {seconds}") 
            time.sleep(1) 
        : print("SOS ALERT TRIGGERED")
