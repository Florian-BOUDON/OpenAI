# OpenAI : intégration d'une IA conversationnelle
        
Je montre comment créer une class d'objet me permettant d'utiliser chatgpt d'OpenAI en utiliser l'API.      
J'utilise le modèle "gpt-4o-mini", faible en utilisation de token.       
Il n'est pas possible d'avoir accès aux assistants gpt, seulement:
- Assistant conversationnel (LLM)      
- Vision             
        
D'autres modèle sont disponible [lien vers les modèles OpenAI](https://platform.openai.com/docs/models)         
- Embeding : text-embedding-3-large
- Moderation : omni-moderation-latest
- TTS : tts-1 (text-to-speech)
- DALL-E : dall-e-3
          
  1) Création d'un script config.py contenant ma clé d'API openAI
  2) Création d'un script composé d'une class permettant de générer des conversations
  3) Cas d'usages dans un notebook jupyter
          
  Si quelqu'un se sent motivé pour continuer le projet avec moi ne pas hésiter à me joindre sur mon mail privé:       
  fb.boudon@gmail.com

Les prochaines étapes sont : 
- Perfectionner mon script pour pour choisir d'autres modèles avec différents paramètres
- fine-tuné un modèle OpenAI
- Utiliser d'autres modèles vision Dall-e...
- asembler plusieurs IA pour obtenir un système cohérent
