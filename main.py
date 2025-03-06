from Monei import MoneiClient, ApiException


def main():
    print("Hello from monei-python-sdk!")

    # Example of using the SDK with accountId and user agent
    try:
        # Initialize the client with API key only
        client = MoneiClient(api_key="YOUR_API_KEY")
        print(f"Initialized client with default user agent: {client.user_agent}")

        # Set a custom user agent
        client.set_user_agent("YourApp/1.0.0 (contact@example.com)")
        print(f"Updated user agent: {client.user_agent}")

        # Set an account ID to act on behalf of a merchant
        client.set_account_id("MERCHANT_ACCOUNT_ID")
        print(f"Set account ID: {client.account_id}")

        # Now all API calls will be made on behalf of the merchant
        # For example:
        # payment = client.payments.create({
        #     'amount': 1250,
        #     'currency': 'EUR',
        #     'description': 'Order from platform',
        # })

        # Remove the account ID to make calls as the platform again
        client.set_account_id(None)
        print("Removed account ID")

    except ApiException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
