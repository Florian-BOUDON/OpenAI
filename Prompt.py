import config
OPENAI_API_KEY = config.OPENAI_API_KEY

import openai

class chatGPT:
    openai.api_key = OPENAI_API_KEY 

    def script(self, prompt: str) -> str:
        try:
            # Envoi de la requête à l'API OpenAI
            completion =  openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Tu es un assistant qui m'aide à coder et à ameliorer mes script python."},
                    {"role": "user", "content": prompt}
                ]
            )
            # Retourne la réponse
            return completion.choices[0].message.content
        except Exception as e:
            return f"Erreur lors de l'envoi de la requête: {str(e)}"


if __name__ == "__main__":
    api_key = OPENAI_API_KEY
    assistant = chatGPT()
