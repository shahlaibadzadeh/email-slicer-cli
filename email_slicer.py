email_config = {
    "gmail": {
        "name": "Gmail",
        "domain": "gmail.com",
        "url": "http://gmail.com"
    },
    "mail": {
        "name": "Mail ru",
        "domain": "mail.ru",
        "url": "http://mail.ru"
    },
    "yahoo": {
        "name": "Yahoo",
        "domain": "yahoo.com",
        "url": "http://yahoo.com"
    }
}


def get_email_config(provider_domain):
    try:
        provider_details = email_config[provider_domain.lower()]
        return provider_details
    except KeyError:
        print("This provider does not exist!")


def validate_email(email):
    if email.count("@") == 1:
        return True
    else:
        return False


def parse_email(email):
    if validate_email(email):
        email_list = email.split("@")
        username = email_list[0]
        domain = email_list[1].split(".")[0]
        config = get_email_config(domain)
        if config:
            return {
                "username": username,
                "provider": config,
            }
    print(f"{email} is not valid email")


def create_email(name, surname, provider):
    provider_details = get_email_config(provider)
    return f'{name}{surname}@{provider_details["domain"]}'


def get_user_info():
    name = input("Enter your name: ").lower()
    surname = input("Enter your surname: ").lower()
    provider = input("Enter your provider: ").lower()
    return name, surname, provider


def get_email():
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            return email
        print("Invalid email")


if __name__ == "__main__":

    while True:
        print("Welcome!", "Select one option below:",
              "1. Create", "2. View details", sep="\n")
        user_input = input("Your choice: ")

        if user_input == "1":
            user_info = get_user_info()
            result = create_email(*user_info)
            print(result)
            break
        elif user_input == "2":
            email = get_email()
            result = parse_email(email)
            if result:
                print(
                    f"Your username is {result['username']} and provider is {result['provider']['name']}. User registered in {result['provider']['url']}")
                break
        else:
            print(">"*10, "Invalid option.")
