from presto import Presto

presto = Presto()

display = presto.display

WHITE = display.create_pen(255, 255, 255)

display.set_pen(WHITE)
display.text("Hey Presto!", 0, 0)
presto.update()