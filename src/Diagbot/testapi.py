from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from model import final_result

app = FastAPI()

# Page d'accueil avec un formulaire pour soumettre une question
@app.get("/diagbot", response_class=HTMLResponse)
async def read_form():
    return """
        <html>
            <head>
                <title>Diagbot</title>
            </head>
            <body>
                <h1>Diagbot</h1>
                <form method="post">
                    <input type="text" name="query" placeholder="Entrez votre question" required>
                    <button type="submit">Soumettre</button>
                </form>
            </body>
        </html>
    """

# Endpoint pour recevoir la question, traiter la réponse et afficher la réponse
@app.post("/diagbot")
async def get_query_result(query: str = Form(...)):
    # Passer la question à final_result
    response = final_result(query)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)
