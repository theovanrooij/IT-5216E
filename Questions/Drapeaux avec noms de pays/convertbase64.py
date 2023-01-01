import base64
import os



results = []
os.chdir("./h240-jpeg")

for file in os.listdir():
    with open(file, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        results.append(b64_string)
        fichier = open(str(file.split('.')[0])+".txt", "a")
        fichier.write(str(b64_string).split("'")[1])
        fichier.close()

print(len(results))