import os, openai
from dotenv import load_dotenv
from AIExtract import Utilities,IF

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
extractor = Utilities.Extractor(lang="portugues", layout={
  "user_name":"",
  "nomes": []
}, TNO=True)
print(extractor.extract(" sdsadadasdasd"))

# ifai = IF()
# ifai.addRule("-30 a -10", "muito frio")
# ifai.addRule("-9 a 0 a 9", "frio")
# ifai.addRule("10 a 40", "muito quente")
# print(ifai.input("10"))