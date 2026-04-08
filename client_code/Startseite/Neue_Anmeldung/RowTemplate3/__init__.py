from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate3(RowTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("Anmelden", "click")
  def Anmelden_click(self, **event_args):
    """This method is called when the button is clicked"""
    #self.Mitglied.visible = False
    #if(Anmelden):
      #self.Mitglied.visible = False
    #self.item.visible = False
