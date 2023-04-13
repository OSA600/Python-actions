import os 


def main():
  print ("c'est un test")
  token = os.environ.get("DOCKER_SECRET_TOKN")
  if not token : 
    raise RuntimeError("accès non autorisé, cette application va se fermer maintenant")
  print ("bienvenue ")
  
#sans cette ligne Github ne saura pas si le code est exécutable ou non
if __name__ == '__main__':
  main()
