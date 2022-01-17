def interface():
    keep_running = True
    print("Blodd Test Analysis")
    while keep_running:
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == 9:
            keep_running = False
    return
   
def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)

def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60 > HDL_value >= 40:
        answer = "Borderline Low"
    elif HDL_value < 40:
        answer = "Low"
    return answer

interface()