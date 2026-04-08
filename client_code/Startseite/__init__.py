from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    sql_kuruebersicht = """
     SELECT
    Kurs.Bezeichnung AS Kurs,
    Kurs.Wochentag,
    Kurs.Uhrzeit,
    Trainer.Vorname || '' || Trainer.Nachname AS Trainer,
    (SELECT COUNT(*) FROM anmelden WHERE anmelden.Kurs_ID = Kurs.Kurs_ID) || '/' || Kurs.Max_Teilnehmer As Teilnehmer
    FROM Kurs
    JOIN Trainer ON Kurs.Trainer_ID = Trainer.Trainer_ID
    ORDER BY Wochentag, Uhrzeit
    """

   
    

    datenanzeigen = anvil.server.call('query_database_dict', sql_kuruebersicht)
    print("SQL:", datenanzeigen)

    self.repeating_panel_1.items = datenanzeigen



  @handle("Kursuebersicht", "click")
  def Kursuebersicht_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Kursuebersicht')

  @handle("neue_anmeldung", "click")
  def neue_anmeldung_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Neue_Anmeldung')
