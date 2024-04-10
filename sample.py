import asyncio

from pylitterbot import Account

# Set email and password for initial authentication.
username = "Your username"
password = "Your password"


async def main():
    # Create an account.
    account = Account()

    try:
        # Connect to the API and load robots.
        await account.connect(
            username=username, password=password, load_robots=True, load_pets=True
        )

        # Print robots associated with account.
        print("Robots:")
        for robot in account.robots:
            print(robot)

        print("Pets:")
        for pet in account.pets:
            await pet.fetch_image()
            if pet.image:
                pet.image.save(pet.name + ".jpeg")
            else:
                print("No pet image.")

            weight_history = await pet.fetch_weight_history()
            for weight in weight_history:
                print(weight)
    finally:
        # Disconnect from the API.
        await account.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
