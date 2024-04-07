class OrderData:

    user_data = [["", "Ivanov", "1241515", "Error: First Name is required"],
                 ["Denis", "", "1241515", "Error: Last Name is required"],
                 ["Denis", "Ivanov", "", "Error: Postal Code is required"]]

    user_data_with_valid_credential = ["Denis", "Ivanov", "1241515"]
    successful_message = "Thank you for your order!"
