from presto import Presto

presto = Presto()

display = presto.display

width = display.measure_text("2,400km", 1, 3)
height = display.measure_text("2,400km", 1, 3)

TEXT_BLUE = display.create_pen(34, 36, 91)

display.set_pen(TEXT_BLUE)
display.set_thickness(3)
display.set_font("sans")
display.text("2,400km", width, height, scale=1)
presto.update()