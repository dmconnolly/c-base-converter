import sublime
import sublime_plugin

from . import convert

class ToBin(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            s = self.view.substr(region)
            val = convert.get_val(s)

            if(val == None):
                continue

            self.view.replace(edit, region, bin(val))

    def is_visible(self):
        for s in [self.view.substr(region) for region in self.view.sel()]:
            if(convert.get_val(s) != None):
                return True
        return False

    def is_enabled(self):
        return True

    def description(self):
        return "Convert to binary"
