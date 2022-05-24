from functools import reduce

MD_EXT = [".mdown", ".mkd", ".mkdn", ".md", ".markdown"]

MAIN_FILE = "home.md"
TITLE = "Home"


def clean_links(link: str):
    return reduce(
        lambda line, rep: line.replace(*rep), [(f"{ext}#", "#") for ext in MD_EXT], link
    )
