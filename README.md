- Creer un environnement virtuel python : 
    - python -m venv chemin/vers/dossier/MedihubDiagBot/venv 
    - Un sous dossier venv sera creer !

- Activer l'environnement virtuel: 
    - cd chemin/vers/dossier/MedihubDiagBot
    - source venv/bin/activate
      
- Test llm model
    - venv/bin/chainlit run src/Diagbot/model.py -w
    - visualiser : http://127.0.0.1:8000/

- Lancer l'application web & l'api Diagbot
    - venv/bin/python src/manage.py runservers
    - venv/bin/python src/Diagbot/testapi.py
    - visualiser : http://127.0.0.1:8000
    
