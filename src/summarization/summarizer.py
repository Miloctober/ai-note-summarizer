import re
from .models import SummaryOutput
from ollama import Client
import sys


class Summarizer:
    """Generates summaries from input text."""

    @staticmethod
    def extract_section(text: str, start_marker: str, end_marker = None) -> list:
        """
        Extrait chaque ligne d'une section délimitée par des marqueurs.
        """
        start = text.lower().find(start_marker.lower())
        if start == -1:
            return []

        start += len(start_marker)

        if end_marker:
            end = text.lower().find(end_marker.lower(), start)
            section = text[start:end] if end != -1 else text[start:]
        else:
            section = text[start:]

        lines = []
        for line in section.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("-"):
                lines.append(line.lstrip("- ").strip())
            else:
                lines.append(line)

        return lines
    
    

    
    def summarize(self, text: str) -> SummaryOutput:
        api_key = "8b3e2f6d39294476a20ac11d85779002.1C791n6oisvSLfdOj2Zut3Bn"

        sys.stdout.reconfigure(encoding='utf-8')

        if api_key is None:
            print("La clé API n'est pas définie.")
        else:
            client = Client(
                host="https://ollama.com",
                headers={'Authorization': 'Bearer ' + api_key}
            )

        messages = [
    {
        "role": "user",
        "content": (
            "Tu es un assistant de cours.\n"
            "Analyse le texte ci-dessous et produis une réponse STRICTEMENT structurée selon les sections suivantes, "
            "dans cet ordre exact et avec ces titres EXACTS :\n\n"
            "Titre\n"
            "Résumé général\n"
            "Points clés\n"
            "Concepts clés\n"
            "Sources\n\n"
            "Règles impératives :\n"
            "- Le texte doit être brut (pas de markdown, pas de **, pas de #).\n"
            "- Chaque section doit commencer par son titre sur une ligne seule.\n"
            "- Les Points clés doivent être une liste avec un élément par ligne, préfixé par '- '.\n"
            "- Les Concepts clés doivent être listés sur une seule ligne, séparés par des virgules.\n"
            "- La section Sources doit lister les sources présentes dans le texte. "
            "S'il n'y a aucune source explicite, écrire exactement : Aucune source mentionnée.\n"
            "- N'invente JAMAIS de source.\n\n"
            "Texte à analyser :\n"
            + text
        )
    }
]

        
        summary = ""
        bullet_points = []
        key_concepts = []
        
        for part in client.chat('cogito-2.1:671b', messages=messages, stream=True):
            response = part['message']['content']
            summary += response
            
            #print("Réponse brute de l'API :")
            #print(response)  # Debug, pour vérifier la réponse brute
            
        # 🔍 Parsing FINAL sur summary (PAS sur response)
        
        title = self.extract_section(
            summary, 
            start_marker= "Titre", 
            end_marker="Concept clés"
            
        )
        
        bullet_points = self.extract_section(
                summary,
                start_marker="Points clés",
                end_marker="Concepts clés"
            )

        key_concepts = self.extract_section(
                summary,
                start_marker="Concepts clés", 
                end_marker="Source"
            )        
        
        sources = self.extract_section(
            summary, 
            start_marker="Source"
        )
        source = sources

        
        text_length = len(text)
        processing_time = 1.2 

        return SummaryOutput(title = title, summary=summary, bullet_points=bullet_points, key_concepts=key_concepts, text_length=text_length, processing_time=processing_time, source = source)

def print_summary(output: SummaryOutput):
    print("\n===== RÉSUMÉ DU DOCUMENT =====\n")

    # Titre
    if output.title:
        print("Titre :")
        if isinstance(output.title, list):
            print(output.title[0])
        else:
            print(output.title)
        print()

    # Résumé général
    print("Résumé général :")
    print(output.summary)
    print()

    # Points clés
    print("Points clés :")
    for point in output.bullet_points:
        print(f"- {point}")
    print()

    # Concepts clés
    print("Concepts clés :")
    if output.key_concepts:
        if len(output.key_concepts) == 1:
            # cas où le modèle renvoie tout sur une ligne
            for concept in output.key_concepts[0].split(","):
                print(f"- {concept.strip()}")
        else:
            for concept in output.key_concepts:
                print(f"- {concept}")
    print()

    # Sources
    print("Sources :")
    if output.source:
        for src in output.source:
            print(f"- {src}")
    else:
        print("- Aucune source mentionnée")

    print("\n==============================\n")


# Appel du résumeur
summarizer = Summarizer()
text_to_summarize = """League of Legends (LoL) est l'un des jeux vidéo les plus populaires et influents de la dernière décennie. Créé et publié par Riot Games en 2009, LoL est un jeu de type MOBA (Multiplayer Online Battle Arena) qui a révolutionné l'industrie du jeu vidéo et est devenu une référence dans le monde des jeux compétitifs et de l'esport. En 2025, LoL continue de dominer la scène des jeux vidéo avec une base de joueurs fidèles, un circuit compétitif de premier plan, et une influence culturelle indéniable."""
summary_result = summarizer.summarize(text_to_summarize)  


        
""" 
    Generate a summary from input text.
    Args:
            text: Raw lecture notes or document text
    Returns:
            SummaryOutput with summary, bullets, and concepts
    Raises:
            ValueError: If text is empty or too short
    """        