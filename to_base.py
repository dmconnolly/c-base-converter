import sublime
import sublime_plugin

from . import convert

# TODO: Configurable key bindings

# TODO: Move to configurable settings
context_menu_options_enabled = True

class ToBaseCommand(sublime_plugin.TextCommand):
    def run(self, edit : sublime.Edit, base : int):

        for region in self.view.sel():
            s = self.view.substr(region)

            val = convert.to_base(s, base)

            if(val != None):
                self.view.replace(edit, region, val)

    def is_visible(self, base):
        if not context_menu_options_enabled:
            return False

        for region in self.view.sel():
            s = self.view.substr(region)

            if(convert.to_base(s, base) != None):
                return True

        return False

    def is_enabled(self):
        return context_menu_options_enabled

class ToBasePromptCommand(sublime_plugin.WindowCommand):
    first_opened = True
    last_used_index = 1

    def run(self):
        self.window.show_quick_panel(["Binary", "Octal", "Decimal",  "Hexidecimal"], self.on_done, 0, self.last_used_index, self.on_highlight)

    def on_highlight(self, index : int):
        # Don't change value when quick panel is first opened
        if self.first_opened == True:
            self.first_opened = False
            return

        base = convert.supported_bases[index]

        if self.window.active_view():
            self.window.active_view().run_command("to_base", {"base": base})

    def on_done(self, index : int):
        base = convert.supported_bases[index]

        if self.window.active_view():
            self.window.active_view().run_command("to_base", {"base": base})

        self.first_opened = True
        self.last_used_index = index
