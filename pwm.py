import re

runes = open("data/common-ioc.ioc")
pwm_cpp = open("code-generated/pwm_runes.cpp", "w")


available_instances = {}

def search_pwm_pins(line):
    if re.search("PWM_OUT", line):
        pin, line = line.strip().split(".")
        pin = pin.split("(")[0]

        if line[-1] == 'T':
            while not (re.search("Signal", line)):
                line = runes.readline()
            trash, timer, channel = line.strip().split("_")

            key = timer+channel
            if key not in available_instances:
                available_instances[timer+channel] = {
                    "MODE" : "NORMAL",
                    "TIMER" : timer,
                    "CHANNEL" : channel[2:],
                    "PIN" : pin
                    }
            else:
                available_instances[timer+channel]["MODE"] = "DUAL"
                available_instances[timer+channel]["PIN"] = pin

        elif line[-1] == 'N':
            while not (re.search("Signal", line)):
                line = runes.readline()
            timer, channel = line.strip().split("=")[1].split("_")
            
            key = timer + channel[:-1]
            if key not in available_instances:
                available_instances[key] = {
                    "MODE" : "NORMAL",
                    "TIMER" : timer,
                    "CHANNEL" : channel[2:-1],
                    "PIN2" : pin
                    }
            else:
                key 
                available_instances[key]["MODE"] = "DUAL"
                available_instances[key]["PIN2"] = pin

        else:
            print("ERROR")
            return -1

def get_data():
    line = runes.readline()
    while line:
        search_pwm_pins(line)
        line = runes.readline()

def write_header():
    pwm_cpp.write(
        '#include "ST-LIB.hpp"\n\n'
        '#ifdef HAL_TIM_MODULE_ENABLED\n\n'
    )

def write_normal_instances():
    pwm_cpp.write("map<Pin, PWMservice::Instance> PWMservice::available_instances = {\n")
    for instance in available_instances.values():
        if instance["MODE"] != "NORMAL":
            continue

        pin = instance["PIN"]
        timer = re.split('(\d+)', instance["TIMER"])[1]
        channel = instance["CHANNEL"]
        pwm_cpp.write("\t{" + f"{pin}, PWMService::Instance(&timer{timer}, TIM_CHANNEL_{channel}, NORMAL)" + "},\n")
    pwm_cpp.write("}\n\n")

def write_dual_instances():
    pwm_cpp.write("map<Pin, PWMservice::Instance> PWMservice::available_instances = {\n")
    for instance in available_instances.values():
        if instance["MODE"] != "DUAL":
            continue

        pin = instance["PIN"]
        pin2 = instance["PIN2"]
        timer = re.split('(\d+)', instance["TIMER"])[1]
        channel = instance["CHANNEL"]
        pwm_cpp.write("\t{{" + f"{pin},{pin2}" + "}, " + f"PWMService::Instance(&timer{timer}, TIM_CHANNEL_{channel}, DUAL)" + "},\n")
    pwm_cpp.write("}\n")

def write_closure():
    pwm_cpp.write("\n#endif")

def write_data():
    write_header()
    write_normal_instances()
    write_dual_instances()
    write_closure()

if __name__ == "__main__":
    get_data()
    write_data()
