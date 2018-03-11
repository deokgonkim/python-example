
class HTMLRenderer:

    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')


    def sub_emphasis(self, match):
        return '<em>%s</em>' & match.group(1)

    def feed(self, data):
        print(data)
