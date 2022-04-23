import logging


class Log() :

  def __init__(self, fichier) :
      self.fichier = "Logs"
   
  def message (self,message) :
    logger = logging.getlogger(self.fichier)
    logger.setlevel(logging.DEBUG)
    LB = logging.FileHandler(self.fichier)
    formatter = logging.Formatter('%(levelname)-15s %(asctime)s %(message)s')

    LB.setFormatter(formatter)
    LB.setlevel(logging.Debug)
    logger.info(message)
    
  def ErrorConnection(self) :

    logger = logging.getlogger(self.fichier)
    logger.setlevel(logging.DEBUG)
    LB = logging.FileHandler(self.fichier)
    formatter = logging.Formatter('%(levelname)-15s %(asctime)s %(message)s')
    LB.setFormatter(formatter)
    LB.setlevel(logging.Debug)
    logger.addHandler(LB)
    logger.error(" Connection error")