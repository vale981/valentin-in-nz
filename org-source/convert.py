import orgparse
import orgparse.date
import pypandoc
import datetime
import os

try:
    os.mkdir("out")
except:
    pass

root = orgparse.load("./content.org")
for node, i in zip(root.children, range(len(root.children))):
    try:
        date = orgparse.date.OrgDate.from_str(
            node.properties["EXPORT_DATE"][1:-1]
        ).start.strftime("%d.%m.%Y")
    except:
        print(node.heading)

    export = node.properties["EXPORT_FILE_NAME"]
    title = node.heading
    content = node.body

    latex_content = pypandoc.convert_text(content, "latex", format="org")
    prefix = str(i + 1).zfill(2)
    filename = f"{prefix}_{export}"
    print(fr"\include{{chapters/{filename}}}")
    with open("out/" + filename + ".tex", "w") as f:
        f.write(f"\chapdate{{{date}}}\n")
        f.write(f"\chapter{{{title}}}\n\n")
        f.write(latex_content)
