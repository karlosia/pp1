phonetic_alphabet={
        "B":"BRAH voh",
        "C":"CHAR lee",
        "D":"DELL tah",
        "E":"ECK oh",
        "F":"FOKS trot",
        "G":"golf",
        "H":"ho TELL",
        "I":"IN dee ah",
        "J":"JEW lee ET,T",
        "K":"KeYY loh",
        "L":"LEE mah",
        "M":"mike",
        "N":"no VEM ber",
        "O":"OSS cah",
        "P":"pah PAH",
        "Q":"keh BECK",
        "R":"ROW me oh",
        "S":"see AIR rah",
        "T":"TANG go",
        "U":"YOU nee form",
        "V":"VIK tah",
        "W":"WISS key",
        "X":"ECKS ray",
        "Y":"YANG key",
        "Z":"ZOO loo",
}

def spell_text(text):
    spelled_text=[phonetic_alphabet.get(char.upper(),char) for char in text]
    return " ".join(spelled_text)

user_input=input("Enter text: ")

spelled_result=spell_text(user_input)

print(spelled_result)
    


    