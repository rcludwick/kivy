from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
<LineEllipse1>:
    canvas:
        Color:
            rgba: 1, .1, .1, .9
        Line:
            width: 2.
            ellipse: (self.x, self.y, self.width, self.height)
    Label:
        center: root.center
        text: 'Ellipse'

<LineEllipse2>:
    canvas:
        Color:
            rgba: 1, .1, .1, .9
        Line:
            width: 2.
            ellipse: (self.x, self.y, self.width, self.height, 90, 180)
    Label:
        center: root.center
        text: 'Ellipse from 90 to 180'

# fun result with low segments!
<LineEllipse3>:
    canvas:
        Color:
            rgba: 1, .1, .1, .9
        Line:
            width: 2.
            ellipse: (self.x, self.y, self.width, self.height, 90, 720, 10)
    Label:
        center: root.center
        text: 'Ellipse from 90 to 720\\n10 segments'
        halign: 'center'

<LineCircle1>:
    canvas:
        Color:
            rgba: .1, 1, .1, .9
        Line:
            width: 2.
            circle: (self.center_x, self.center_y, min(self.width, self.height) / 2)
    Label:
        center: root.center
        text: 'Circle'

<LineCircle2>:
    canvas:
        Color:
            rgba: .1, 1, .1, .9
        Line:
            width: 2.
            circle: (self.center_x, self.center_y, min(self.width, self.height) / 2, 90, 180)
    Label:
        center: root.center
        text: 'Circle from 90 to 180'

<LineCircle3>:
    canvas:
        Color:
            rgba: .1, 1, .1, .9
        Line:
            width: 2.
            circle: (self.center_x, self.center_y, min(self.width, self.height) / 2, 90, 180, 10)
    Label:
        center: root.center
        text: 'Circle from 90 to 180\\n10 segments'
        halign: 'center'

<LineRectangle>:
    canvas:
        Color:
            rgba: .1, .1, 1, .9
        Line:
            width: 2.
            rectangle: (self.x, self.y, self.width, self.height)
    Label:
        center: root.center
        text: 'Rectangle'
''')


class LineEllipse1(Widget):
    pass

class LineEllipse2(Widget):
    pass

class LineEllipse3(Widget):
    pass

class LineCircle1(Widget):
    pass

class LineCircle2(Widget):
    pass

class LineCircle3(Widget):
    pass

class LineRectangle(Widget):
    pass

class LineExtendedApp(App):
    def build(self):
        root = GridLayout(cols=2, padding=50, spacing=50)
        root.add_widget(LineEllipse1())
        root.add_widget(LineEllipse2())
        root.add_widget(LineEllipse3())
        root.add_widget(LineCircle1())
        root.add_widget(LineCircle2())
        root.add_widget(LineCircle3())
        root.add_widget(LineRectangle())
        return root

if __name__ == '__main__':
    LineExtendedApp().run()
