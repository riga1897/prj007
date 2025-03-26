def get_mask_card_number(card_number: str) -> str:
    """
    Функция маскировки номера банковской карты
    """
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """
    Функция маскировки номера банковского счета
    """
    return f"**{account[-4:]}"


if __name__ == "__main__":
    my_card_number = "7000792289606361"
    my_account = "73654108430135874305"
    print(get_mask_card_number(my_card_number))
    print(get_mask_account(my_account))
