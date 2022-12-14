#include "ST-LIB.hpp"

#ifdef HAL_TIM_MODULE_ENABLED

extern TIM_HandleTypeDef htim1;

TimerPeripheral::InitData init_data_timer1 = TimerPeripheral::InitData(TIM1, Period=1000, Prescaler=270);
TimerPeripheral timer1(&htim1, init_data_number1);

vector<reference_wrapper<TimerPeripheral>> TimerPeripheral::timers = {
	timer1,
};

#endif