with open("./dist/output.html", "w") as dist:
    with open("./index.html") as html:
        with open("./dist/output.css") as css:
            contents = html.read().splitlines()
            contents.insert(
                4,
                f"<style>{css.read()}</style>",
            )
            dist.write("\n".join(contents))

with open("./dist/output.html") as dist:
    with open("../src/hoist/_html.py", "w") as f:
        f.write(
            f"""from .version import __version__

__all__ = ("HTML",)

HTML = r'''{dist.read()}'''.replace('{{version}}', __version__)
"""
        )
