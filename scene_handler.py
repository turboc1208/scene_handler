import appdaemon.plugins.hass.hassapi as hass
import datetime
import time
m4_include('/home/appdaemon/code/appdaemon/adlib_imports.pyi')
class scene_handler(hass.Hass):

  def initialize(self):
    # self.LOGLEVEL="DEBUG"
    self.log("scene_handler App")
    ADUtils=self.get_app("ADutils")

m4_include(/home/appdaemon/code/appdaemon/adlib.pyi)
