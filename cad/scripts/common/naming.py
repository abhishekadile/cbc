REVISION = "r001"


def part_name(stem: str, revision: str = REVISION) -> str:
    return f"{stem}_{revision}"


def filename(stem: str, suffix: str, revision: str = REVISION) -> str:
    return f"{part_name(stem, revision)}.{suffix.lstrip('.')}"
