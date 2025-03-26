from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string_to_mask: str) -> str:
    """
    Функция маскировки номера банковской карты или номера банковского счета
    """
    string_list = string_to_mask.split()
    account_or_card = string_list[-1]

    if len(account_or_card) == 16:
        string_list[-1] = get_mask_card_number(account_or_card)
    elif len(account_or_card) == 20:
        string_list[-1] = get_mask_account(account_or_card)

    return " ".join(string_list)


def get_date(date_to_modify: str) -> str:
    """
    Функция преобразования даты из одного формата в другой
    """
    modified_day = ".".join(list(reversed(date_to_modify.split("T")[0].split("-"))))
    return modified_day


if __name__ == "__main__":
    print("Модуль импортируется из main")
