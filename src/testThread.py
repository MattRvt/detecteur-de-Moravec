from concurrent.futures import thread
from threading import Thread, RLock

verrou = RLock()

class Afficheur(Thread):
   intensite = 0
   #"""Thread chargé simplement d'afficher un mot dans la console."""

   def __init__(self, r,g,b):
      Thread.__init__(self)
      self.r = r
      self.g = g
      self.b = b
      self.intensite

   def run(self):
      """Code à exécuter pendant l'exécution du thread."""
      self.intensite = self.r * 1 + self.g * 3 + self.b * 2

# Création des threads
threads = []
for i in range(10000000):
   thread = Afficheur(1*i,2*i,3*i)
   threads.append(thread)


# Lancement des threads
for thread in threads:
   thread.start()

for thread in threads:
   print(thread.intensite)
# Attend que les threads se terminent
for thread in threads:
   thread.join()