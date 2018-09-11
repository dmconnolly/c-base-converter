import sublime
import sublime_plugin

from . import convert
from . import config

stored_regions = []
stored_values = []

# TODO: Fix quick panel quirks on exit and focus lost

class ToBaseCommand(sublime_plugin.TextCommand):
    def run(self, edit : sublime.Edit, base : int):
        if not config.settings:
            return

        for region in self.view.sel():
            s = self.view.substr(region)

            val = convert.to_base(s, base)

            if(val != None):
                self.view.replace(edit, region, val)

    def is_visible(self, base : int):
        if not config.settings or not config.settings.get('context_menu_options_enabled', True):
            return False

        base_enabled = False
        for base_data in config.enabled_bases:
            if base_data['value'] == base:
                base_enabled = True
                break

        if not base_enabled:
            return False

        for region in self.view.sel():
            s = self.view.substr(region)

            if(convert.to_base(s, base) != None):
                return True

        return False

    def is_enabled(self):
        return config.settings != None

class ToBasePromptCommand(sublime_plugin.WindowCommand):
    first_opened = True
    last_used_index = 1

    def run(self):
        if not config.settings:
            return

        options = []

        for base_data in config.enabled_bases:
            options.append(base_data['string'])

        # Only option quick panel if any options are enabled
        if options:
            # Reset last_used_index if outside options list
            if self.last_used_index >= len(options):
                self.last_used_index = 0

            self.highlighted_index = self.last_used_index

            self.window.show_quick_panel(
                options, # Options list
                self.on_done, # On done handler
                0, # Flags (bitwise OR of sublime.MONOSPACE_FONT and sublime.KEEP_OPEN_ON_FOCUS_LOST)
                self.last_used_index, # Start index
                self.on_highlight # On highlight handler
            )

    def on_highlight(self, index : int):
        # Don't change value when quick panel is first opened
        if self.first_opened == True:
            self.first_opened = False
            pass # Store current values
            return

        base = config.enabled_bases[index]['value']

        if self.window.active_view():
            self.window.active_view().run_command("to_base", {"base": base})

    def on_done(self, index : int):
        self.first_opened = True

        if index == -1:
            if config.settings.get('revert_on_quick_panel_exit', True):
                pass # Load original values
        else:
            base = config.enabled_bases[index]['value']

            if self.window.active_view():
                self.window.active_view().run_command("to_base", {"base": base})

            self.last_used_index = index
