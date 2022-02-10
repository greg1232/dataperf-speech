import config
import os

import logging

logger = logging.getLogger(__name__)

global_config = None

def initialize_config_and_logging():
    global global_config
    global_config = build_config()

    setup_logging(global_config)

    logger.debug("Config: " + str(global_config))

    return global_config

def get_config():
    global global_config
    assert global_config is not None
    return global_config

def build_config(dictionary = {}):
    return config.ConfigurationSet(
        config.config_from_env(prefix="DATAPERF", separator="_", lowercase_keys=True),
        config.config_from_yaml(config_path(), read_from_file=True),
        config.config_from_dict(dictionary),
    )

def config_path():
    home = os.path.expanduser("~")
    home_config_path = os.path.join(home, "dataperf.yaml")
    if os.path.exists(home_config_path):
        return home_config_path

    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "configs", "dataperf.yaml")

def config_to_dict(config):
    dictionary = {}

    for key, value in config.as_dict().items():
        scope = dictionary
        components = key.split(".")

        for component in components[:-1]:
            if not component in scope:
                scope[component] = {}
            scope = scope[component]

        scope[components[-1]] = value

    return dictionary

def setup_logging(arguments):

    logging_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

    if arguments["verbose"]:
        logging.basicConfig(level=logging.DEBUG, format=logging_format)
    elif arguments["verbose_info"]:
        logging.basicConfig(level=logging.INFO, format=logging_format)
    else:
        logging.basicConfig(level=logging.WARNING, format=logging_format)

    root_logger = logging.getLogger()

    if arguments["verbose"]:
        root_logger.setLevel(logging.DEBUG)
    elif arguments["verbose_info"]:
        root_logger.setLevel(logging.INFO)
    else:
        root_logger.setLevel(logging.WARNING)

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("filelock").setLevel(logging.WARNING)


