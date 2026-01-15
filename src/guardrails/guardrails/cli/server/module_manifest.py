from dataclasses import dataclass, field
from typing import Any

from pydash.strings import snake_case

from guardrails.classes.generic.serializeable import (
    Serializeable,
    SerializeableJSONEncoder,
)


@dataclass
class Contributor(Serializeable):
    name: str
    email: str


@dataclass
class Repository(Serializeable):
    url: str
    branch: str | None = None


@dataclass
class ModuleTags(Serializeable):
    content_type: list[str] | None = field(default_factory=list)
    validation_category: list[str] | None = field(default_factory=list)
    process_requirements: list[str] | None = field(default_factory=list)
    has_guardrails_endpoint: bool | None = field(default_factory=bool)


@dataclass
class ModelAuth(Serializeable):
    type: str
    name: str
    displayName: str | None = None


@dataclass
class ModuleManifest(Serializeable):
    id: str
    name: str
    author: Contributor
    maintainers: list[Contributor]
    repository: Repository
    namespace: str
    package_name: str
    module_name: str
    exports: list[str]
    tags: ModuleTags | None = None
    requires_auth: bool | None = True
    post_install: str | None = None
    index: str | None = None
    required_model_auth: list[ModelAuth] | None = field(default_factory=list)

    # @override
    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        init_kwargs = {snake_case(k): data.get(k) for k in data}
        init_kwargs["encoder"] = init_kwargs.get("encoder", SerializeableJSONEncoder)
        author = init_kwargs.pop("author", {})
        maintainers = init_kwargs.pop("maintainers", [])
        repository = init_kwargs.pop("repository", {})
        tags = init_kwargs.pop("tags", {})
        return cls(
            **init_kwargs,
            author=Contributor.from_dict(author),  # type: ignore
            maintainers=[Contributor.from_dict(m) for m in maintainers],  # type: ignore
            repository=Repository.from_dict(repository),  # type: ignore
            tags=ModuleTags.from_dict(tags),  # type: ignore
        )
