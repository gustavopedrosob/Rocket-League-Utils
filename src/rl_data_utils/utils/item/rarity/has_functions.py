from rl_data_utils.utils.item.rarity.is_functions import is_black_market, is_common, is_exotic, is_import, is_legacy, \
    is_limited, is_premium, is_rare, is_uncommon, is_very_rare


def has_black_market(rarities: list[str]) -> bool:
    return any([is_black_market(rarity) for rarity in rarities])


def has_common(rarities: list[str]) -> bool:
    return any([is_common(rarity) for rarity in rarities])


def has_exotic(rarities: list[str]) -> bool:
    return any([is_exotic(rarity) for rarity in rarities])


def has_import(rarities: list[str]) -> bool:
    return any([is_import(rarity) for rarity in rarities])


def has_legacy(rarities: list[str]) -> bool:
    return any([is_legacy(rarity) for rarity in rarities])


def has_limited(rarities: list[str]) -> bool:
    return any([is_limited(rarity) for rarity in rarities])


def has_premium(rarities: list[str]) -> bool:
    return any([is_premium(rarity) for rarity in rarities])


def has_rare(rarities: list[str]) -> bool:
    return any([is_rare(rarity) for rarity in rarities])


def has_uncommon(rarities: list[str]) -> bool:
    return any([is_uncommon(rarity) for rarity in rarities])


def has_very_rare(rarities: list[str]) -> bool:
    return any([is_very_rare(rarity) for rarity in rarities])
