from orchestrator.controller import Controller

if __name__ == "__main__":

    topic = input("Topic: ")
    theme = input("Theme (modern/minimal/dark/corporate): ")
    path = input("Save path: ")

    system = Controller()
    output = system.run(topic, theme, path)

    print(output)