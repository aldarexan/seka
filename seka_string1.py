print("=" * 50)
print("1. STRING CREATION")
print("=" * 50)
text = "Hello, Python World!"
multi_line = """This is a
multi-line string"""
print(f"Single line: {text}")
#print("Single line: " + text) #<-- može i ovako
print(f"Multi-line: {multi_line}\n")
#print(f"Multi-line: {3 + 7}\n") #<-- može i ovako
text2 = ""
ime = "Seka"
prezime = "Morriarty"
jmbg = 22222222
#print(" Vaši podaci su: \n", ime, "\n", prezime, "\n", jmbg, "\n") #<-- može i ovako
satiranje = f"""Vaši podaci su: 
{ime} 
{prezime} 
{jmbg}"""
#print(f"{satiranje}\n")#<-- može i ovako; uvek vraća string
print(satiranje)#<-- ovako je čistije; nemam dvaput f