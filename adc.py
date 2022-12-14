import re
import pandas as pd

runes = open("data/common-ioc.ioc")
timer_cpp = open("code-generated/timer_runes.cpp", "w")

init_data_timers = {}

def search_timer_data(line):
    if re.search(r"^TIM", line):
        if not re.search(r"Channel", line):
            timer, data = line.strip().split(".")
            if timer not in init_data_timers:
                init_data_timers[timer] = {}
            name, value = data.split("=")
            init_data_timers[timer][name] = value

def get_data():
    for line in runes.readlines():
        search_timer_data(line)

def write_header():
    timer_cpp.write(
        '#include "ST-LIB.hpp"\n\n'
        '#ifdef HAL_TIM_MODULE_ENABLED\n\n'
    )

def write_extern_timers():
    for timer in init_data_timers:
        timer_cpp.write(
            f"extern TIM_HandleTypeDef htim{timer[-1]};\n"
        )
    timer_cpp.write("\n")

def write_timers_init_data():
    for timer, data in init_data_timers.items():
        timer_cpp.write(
            f"TimerPeripheral::InitData init_data_timer{timer[-1]} = TimerPeripheral::InitData({timer}"
            )
        for name, value in data.items():
            timer_cpp.write(
                f", {name}={value}"
            )
        timer_cpp.write(
            f");\n"
        )

def write_timers():
    for timer in init_data_timers:
        number = re.split('(\d+)', timer)[1]

        timer_cpp.write(
            f"TimerPeripheral timer{number}(&htim{number}, init_data_number{number});\n"
        )
    timer_cpp.write("\nvector<reference_wrapper<TimerPeripheral>> TimerPeripheral::timers = {\n")

    for timer in init_data_timers:
        number = re.split('(\d+)', timer)[1]
        timer_cpp.write(
            f"\ttimer{number},\n"
        )
    timer_cpp.write("};\n")
def write_data():
    write_header()
    write_extern_timers()
    write_timers_init_data()
    write_timers()
    write_closure()

def write_closure():
    timer_cpp.write("\n#endif")
   
if __name__ == "__main__":
    get_data()
    write_data()