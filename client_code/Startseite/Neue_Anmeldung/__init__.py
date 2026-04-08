from ._anvil_designer import Neue_AnmeldungTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Neue_Anmeldung(Neue_AnmeldungTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    sql_neue_anmeldung = """
    SELECT Vorname || ' ' || Nachname AS Mitglied
    FROM Mitglieder
    """

    datenanzeigen = anvil.server.call('query_database_dict', sql_neue_anmeldung)
    print("SQL:", datenanzeigen)

    self.repeating_panel_1.items = datenanzeigen

    # Any code you write here will run before the form opens.

  @handle("neue_anmeldung", "click")
  def neue_anmeldung_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Neue_Anmeldung')

  @handle("zurueck", "click")
  def zurueck_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite')
