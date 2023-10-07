html = ""
css = ""

with open("index.html", "r") as d:
    html = d.read()

with open("output.css", "r") as d:
    css = d.read()

css = "<style>" + css.strip() + "</style>"
zeilen = html.split("\n")
html = ""

for zeile in zeilen:
    zeile = zeile.strip()

    if zeile == '<link rel="stylesheet" type="text/css" href="output.css">':
        zeile = css

    if zeile.startswith("<!--"):
        continue

    html += zeile
    # html += "\n"

with open("kompiliert.html", "w") as d:
    d.write(html)

with open("kompiliert.ino", "w") as d:
    # html_string = html.replace("\n", "\\\n").replace('"', '\\"')
    html_string = html.replace('"', '\\"')
    parts = html_string.split("true")

    ino = "String gibWebUI(bool wischtGerade) {\n"
    ino += '\tString h = "'
    ino += parts[0]
    ino += '";\n'
    ino += '\th += wischtGerade? "true" : "false";\n'
    ino += '\th += \"'
    ino += parts[1]
    ino += '";\n'
    ino += "\treturn h;\n"
    ino += "}\n"
    d.write(ino)
