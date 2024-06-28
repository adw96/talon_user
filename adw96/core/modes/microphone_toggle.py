# created by aegis for Amy on Oct 2 2023
from talon import Module, actions

mod = Module()
@mod.action_class
class Actions:
    def toggle_microphone():
        """Toggle the microphone between None and SpeechWare USB MultiAdapter"""
        active = actions.sound.active_microphone()
        if active == "None":
            actions.sound.set_microphone("SpeechWare USB MultiAdapter")
        else:
            actions.sound.set_microphone("None")