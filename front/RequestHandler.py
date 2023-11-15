import sys
import gi
import threading 
import requests
import json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class EntryHandler:
    def __init__(self, entry, callback):
        self.entry = entry
        self.callback = callback
        self.entry.connect("changed", self.on_entry_changed)

    def on_entry_changed(self):
        if self.entry:
            self.thread = threading.Thread(target=self.request)
            self.thread.start()

    def request(self):
        request_data = self.entry.split("?")
        tables = request_data[0]
        variables = request_data[1]
        textvar = ""
        if (len(request_data) >= 2){
            textvar = tables + "&" + variables
        } else if (){
            textvar = tables
        }else{
            return
        }
        url = "http://localhost:8080/CriticalDesignPBE/back/index.php?" + textvar
        response = requests.get(url)
        result = response.json()
        self.callback(result)


