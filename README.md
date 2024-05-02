- Creer un environnement virtuel python : 
    - python -m venv chemin/vers/dossier/MedihubDiagBot/venv 
    - Un sous dossier venv sera creer !

- Activer l'environnement virtuel: 
    - cd chemin/vers/dossier/MedihubDiagBot
    - source venv/bin/activate

- Lancer l'application web
    - venv/bin/python src/manage.py runservers
    - visualiser : http://127.0.0.1:8000/

- Lancer l'api Diabot
    - venv/bin/python src/Diagbot/testapi.py

- Test llm model
    - venv/bin/chainlit run src/Diagbot/model.py -w
    - visualiser : http://127.0.0.1:8000/