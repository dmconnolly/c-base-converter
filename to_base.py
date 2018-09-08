import sublime
import sublime_plugin

from . import convert

class ToBaseContextCommand(sublime_plugin.TextCommand):
    def run(self, edit : sublime.Edit, base):

        for region in self.view.sel():
            s = self.view.substr(region)

            val = convert.to_base(s, base)

            if(val != None):
                self.view.replace(edit, region, val)

    def is_visible(self, base):
        for region in self.view.sel():
            s = self.view.substr(region)

            if(convert.to_base(s, base) != None):
                return True

        return False

    def description(self):
        return "Convert to base"
