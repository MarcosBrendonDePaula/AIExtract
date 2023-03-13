import os, openai
from dotenv import load_dotenv
from AIExtract import Utilities,IF

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# extractor = Utilities.Extractor(lang="portugues", layout={
#   "nome":"",
#   "dias_trabalhados": ["y-m-d a y-m-d" ]
# }, numeric=True)
# print(extractor.extract("me chamo marcos onde iniciei meus trabalhos no dia um de janeiro de 2023 onde venho trabalahndo até hoje que é dia 30 de dezembro, meus amigos são o ezequiel, mateus, eric, henri, diego"))

# ifai = IF()
# ifai.addRule("dizer algo de graus", "{'graus':valor}")
# ifai.addRule("dizer algo de fareheight", "{todas_unidades_convertidas}")
# ifai.addRule("dizer algo de kelvin", "kelvin")
# ifai.addRule("somente um numero", "numero")
# print(ifai.input("hoje está -30 graus a mais que ontem quanto graus estava ontem"))