
with open("./dist/index.html", "r") as f:

    content = f.read()

    content = content.replace('"/', '"./')

    f.close()

with open("./dist/index.html", "w") as f:

    f.write(content)

    f.close()