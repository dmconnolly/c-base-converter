import sublime
import sublime_plugin

from . import convert

class ToDec(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            s = self.view.substr(region)
            dec = convert.get_val(s)

            if(dec == None):
                continue

            self.view.replace(edit, region, str(dec))

    def is_visible(self):
        for s in [self.view.substr(region) for region in self.view.sel()]:
            if(convert.get_val(s) != None):
                return True
        return False

    def is_enabled(self):
        return True

    def description(self):
        return "Convert to decimal"
