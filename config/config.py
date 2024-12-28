import yaml


def load_config(file_path="config/config.yaml"):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config


config = load_config()


def update_config(new_config):
    with open("config/config.yaml", "w") as file:
        yaml.safe_dump(new_config, file)
        print(new_config)
