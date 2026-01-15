import collections
from string import Template


def get_template_variables(template: str) -> list[str]:
    if hasattr(Template, "get_identifiers"):
        return Template(template).get_identifiers()  # type: ignore
    else:
        d = collections.defaultdict(str)
        Template(template).safe_substitute(d)
        return list(d.keys())
