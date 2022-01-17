def interface():
    keep_running = True
    print("Blodd Test Analysis")
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_driver()
    return
   
def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)

def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return out_string

def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60 > HDL_value >= 40:
        answer = "Borderline Low"
    elif HDL_value < 40:
        answer = "Low"
    return answer

def HDL_driver():
    HDLvalue = accept_input("HDL")
    classification = check_HDL(HDLvalue)
    print_result("HDL", HDLvalue, classification)

interface()