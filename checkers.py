from difflib import SequenceMatcher

from settings import EQUAL_PERCENT


TRANSLATED_PATTERNS = {"А": "A", "А1": "A1", "В1": "B1", "В": "B"}


def check_city(city_1, city_2):
    return str(city_1).strip() == str(city_2).strip()


def check_side(side_1, side_2):
    if str(side_1).strip() not in TRANSLATED_PATTERNS:
        return False
    return TRANSLATED_PATTERNS[str(side_1).strip()] == str(side_2).strip()


def check_addres(addres_1, addres_2):
    normalized_addres_1 = str(addres_1).replace("(Digital)", "").replace(" ", "")
    normalized_addres_2 = str(addres_2).replace("(Digital)", "").replace(" ", "")
    if normalized_addres_1 == normalized_addres_2:
        return True
    if (
        SequenceMatcher(
            a=str(addres_1).replace("(Digital)", "").replace(" ", ""),
            b=str(addres_2).replace("(Digital)", "").replace(" ", ""),
            autojunk=True,
        ).ratio()
        >= EQUAL_PERCENT
    ):
        access = input(f'Подтвердите что адрес {addres_1} это {addres_2}, напишите y или Y \n')
        if access in ['y', 'Y']:
            return True
    return False


def check_sum(item, source_item) -> bool:
    return str(item["Итого, NET"]) == str(source_item["Цена ролик 5 сек"])