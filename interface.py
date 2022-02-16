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

def check_LDL(LDL_value):
    if LDL_value < 130:
        answer = "Normal"
    elif 130 <= LDL_value <= 159:
        answer = "Borderline High"
    elif 160 <= LDL_value <= 189:
        answer = "High"
    elif LDL_value >= 190:
        answer = "Very High"
    return answer

def check_Total_Cholesterol(val):
    if val < 200:
        answer = "Normal"
    elif 200 <= val <= 239:
        answer = "Borderline High"
    elif val > 240:
        answer = "High"
    return answer

def HDL_driver():
    HDLvalue = accept_input("HDL")
    classification = check_HDL(HDLvalue)
    print_result("HDL", HDLvalue, classification)

interface()