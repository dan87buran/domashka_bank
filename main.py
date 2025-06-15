from src.masks import get_mask_card_number, get_mask_account_number

def main():
    """Основная функция для демонстрации работы"""
    card_number = "4276 1300 4546 7592"
    masked_card = get_mask_card_number(card_number)
    print(f"Замаскированная карта: {masked_card}")

    account_number = "40702810000000000000"
    masked_account = get_mask_account_number(account_number)
    print(f"Замаскированный счет: {masked_account}")

if __name__ == "__main__":
    main()