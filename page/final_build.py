VERSTRING = (
    f"{{_VER.release}}{{f' ({{RELEASE_TYPE}})' if any({{IS_DEV, IS_PRE}}) else ''}}",  # noqa
)
# using an f-string here to simulate the actual build

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
            f"""from .__about__ import __version__

from versions import parse_version

_VER = parse_version(__version__)
IS_DEV: bool = _VER.is_dev_release()
IS_PRE: bool = _VER.is_pre_release()
RELEASE_TYPE: str = (
    "Pre-Release" if IS_PRE else "Development" if IS_DEV else ""
)  # fmt: off

__all__ = ("HTML",)

HTML = r'''{dist.read()}'''.replace(
    "{{version}}",
    {VERSTRING}
)
"""
        )
