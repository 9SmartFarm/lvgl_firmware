import lvgl as lv
import utime as time
import sys

from ili9XXX import st7789

disp = st7789(width=135, height=240, rot=-2)

def set_value(indic, v):
    meter.set_indicator_value(indic, v)

#
# A simple meter
#
meter = lv.meter(lv.scr_act())
meter.set_size(135, 135)
meter.center()

#Add a scale first
meter.set_scale_ticks(41, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(8, 4, 15, lv.color_black(), 10)
#meter.set_style_text_font(lv.font_montserrat_18, 0)

indic = lv.meter_indicator_t()

# Add a blue arc to the start
indic = meter.add_arc(3, lv.palette_main(lv.PALETTE.BLUE), 0)
meter.set_indicator_start_value(indic, 0)
meter.set_indicator_end_value(indic, 20)

# Make the tick lines blue at the start of the scale
indic = meter.add_scale_lines(lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.BLUE), False, 0)
meter.set_indicator_start_value(indic, 0)
meter.set_indicator_end_value(indic, 20)

# Add a red arc to the end
indic = meter.add_arc(3, lv.palette_main(lv.PALETTE.RED), 0)
meter.set_indicator_start_value(indic, 80)
meter.set_indicator_end_value(indic, 100)

# Make the tick lines red at the end of the scale
indic = meter.add_scale_lines(lv.palette_main(lv.PALETTE.RED), lv.palette_main(lv.PALETTE.RED), False, 0)
meter.set_indicator_start_value(indic, 80)
meter.set_indicator_end_value(indic, 100)

# Add a needle line indicator
indic = meter.add_needle_line(4, lv.palette_main(lv.PALETTE.GREY), -10)

meter_value = lv.label(lv.scr_act())
meter_value.set_text('ภาษาไทย')
meter_value.align(lv.ALIGN.CENTER, -60, 50)
meter_value.set_style_text_font(lv.Kanit_Regular_16, 0)

meter_value = lv.label(lv.scr_act())
meter_value.set_text('ภาษาไทย')
meter_value.align(lv.ALIGN.CENTER, 60, 50)
meter_value.set_style_text_font(lv.Kanit_Regular_20, 0)

meter_value = lv.label(lv.scr_act())
meter_value.set_text("LVGL")
meter_value.align(lv.ALIGN.CENTER, -80, -58)
meter_value.set_style_text_font(lv.Kanit_Regular_16, 0)

meter_value = lv.label(lv.scr_act())
meter_value.set_text("V "+str(lv.version_major())+"."+str(lv.version_minor())+"."+str(lv.version_patch()))
meter_value.align(lv.ALIGN.CENTER, -80, -40)
meter_value.set_style_text_font(lv.Kanit_Regular_16, 0)

meter_value = lv.label(lv.scr_act())
meter_value.set_text("Micropython")
meter_value.align(lv.ALIGN.CENTER, 74, -58)
meter_value.set_style_text_font(lv.Kanit_Regular_16, 0)

meter_value = lv.label(lv.scr_act())
meter_value.set_text(str(sys.implementation[1]))
meter_value.align(lv.ALIGN.CENTER, 80, -40)
meter_value.set_style_text_font(lv.Kanit_Regular_16, 0)

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
