#include "ST-LIB.hpp"

#ifdef HAL_TIM_MODULE_ENABLED

map<Pin, PWMservice::Instance> PWMservice::available_instances = {
	{PB14, PWMService::Instance(&timer12, TIM_CHANNEL_1, NORMAL)},
	{PB15, PWMService::Instance(&timer12, TIM_CHANNEL_2, NORMAL)},
	{PB4, PWMService::Instance(&timer3, TIM_CHANNEL_1, NORMAL)},
	{PB5, PWMService::Instance(&timer3, TIM_CHANNEL_2, NORMAL)},
	{PC8, PWMService::Instance(&timer3, TIM_CHANNEL_3, NORMAL)},
	{PD12, PWMService::Instance(&timer4, TIM_CHANNEL_1, NORMAL)},
	{PD13, PWMService::Instance(&timer4, TIM_CHANNEL_2, NORMAL)},
	{PD15, PWMService::Instance(&timer4, TIM_CHANNEL_4, NORMAL)},
	{PE14, PWMService::Instance(&timer1, TIM_CHANNEL_4, NORMAL)},
	{PE6, PWMService::Instance(&timer15, TIM_CHANNEL_2, NORMAL)},
	{PF1, PWMService::Instance(&timer23, TIM_CHANNEL_2, NORMAL)},
	{PF2, PWMService::Instance(&timer23, TIM_CHANNEL_3, NORMAL)},
	{PF3, PWMService::Instance(&timer23, TIM_CHANNEL_4, NORMAL)},
}

map<Pin, PWMservice::Instance> PWMservice::available_instances = {
	{{PB8,PB6}, PWMService::Instance(&timer16, TIM_CHANNEL_1, DUAL)},
	{{PB9,PB7}, PWMService::Instance(&timer17, TIM_CHANNEL_1, DUAL)},
	{{PE11,PE10}, PWMService::Instance(&timer1, TIM_CHANNEL_2, DUAL)},
	{{PE13,PE12}, PWMService::Instance(&timer1, TIM_CHANNEL_3, DUAL)},
	{{PE5,PE4}, PWMService::Instance(&timer15, TIM_CHANNEL_1, DUAL)},
	{{PE9,PE8}, PWMService::Instance(&timer1, TIM_CHANNEL_1, DUAL)},
}

#endif