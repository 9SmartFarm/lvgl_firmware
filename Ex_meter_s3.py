
import utime
import lvgl as lv
from ili9XXX import gc9107
from machine import reset, soft_reset, RTC, WDT, Pin

disp = gc9107()

meter = lv.meter(lv.scr_act())
meter.set_size(128, 128)
meter.center()

#Add a scale first
scale_min = meter.add_scale()
meter.set_scale_ticks(scale_min, 41, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(scale_min, 8, 4, 15, lv.color_black(), 10)
#meter.set_style_text_font(lv.font_montserrat_18, 0)

indic = lv.meter_indicator_t()

# Add a blue arc to the start
indic = meter.add_arc(scale_min, 3, lv.palette_main(lv.PALETTE.BLUE), 0)
meter.set_indicator_start_value(indic, 0)
meter.set_indicator_end_value(indic, 20)

# Make the tick lines blue at the start of the scale
indic = meter.add_scale_lines(scale_min, lv.palette_main(
    lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.BLUE), False, 0)
meter.set_indicator_start_value(indic, 0)
meter.set_indicator_end_value(indic, 20)

# Add a red arc to the end
indic = meter.add_arc(scale_min, 3, lv.palette_main(lv.PALETTE.RED), 0)
meter.set_indicator_start_value(indic, 80)
meter.set_indicator_end_value(indic, 100)

# Make the tick lines red at the end of the scale
indic = meter.add_scale_lines(scale_min, lv.palette_main(
    lv.PALETTE.RED), lv.palette_main(lv.PALETTE.RED), False, 0)
meter.set_indicator_start_value(indic, 80)
meter.set_indicator_end_value(indic, 100)

# Add a needle line indicator
indic = meter.add_needle_line(
    scale_min, 4, lv.palette_main(lv.PALETTE.GREY), -10)

def set_value(indic, v):
    meter.set_indicator_value(indic, v)
    
# Create an animation to set the value
a = lv.anim_t()
a.init()
a.set_var(indic)
a.set_values(0, 100)
a.set_time(2000)
a.set_repeat_delay(100)
a.set_playback_time(500)
a.set_playback_delay(100)
a.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
a.set_custom_exec_cb(lambda a,val: set_value(indic,val))
lv.anim_t.start(a)

label = lv.label(lv.scr_act())
label.set_text('ภาษาไทย')
#label.set_text('PHENGSALAE')
label.align(lv.ALIGN.CENTER, 0, 46)
label.set_style_text_font(lv.Kanit_Regular_20, 0)
