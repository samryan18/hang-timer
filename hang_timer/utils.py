import time

import yaml
from playsound import playsound
from tqdm import tqdm


def load_config(config_path: str) -> dict:
    try:
        with open(config_path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config not found at path: {config_path}!")

    return config


def beep_and_wait(
    config: dict,
    tqdm_prefix: str = "",
    sound_key: str = "start",
    wait_secs: float = 5,
    encouragement: bool = False,
):
    beep(config, sound_key)
    t0 = time.time()
    current_time = time.time() - t0
    with tqdm(
        total=round(wait_secs),
        desc=tqdm_prefix,
        unit="seconds",
        bar_format="{desc} [{elapsed} / {total} seconds]",
    ) as pbar:
        while current_time < wait_secs + 0.01:
            prev_current_time = current_time
            current_time = time.time() - t0
            pbar.update(current_time - prev_current_time)

            if encouragement:
                beep(config, "encouragement")
                encouragement = False


def welcome_message(delay_before_start: float):
    print("TIMER!\n(PRESS CTRL-C TO STOP AT ANY TIME)\n")

    if delay_before_start > 0:
        tqdm_prefix = "👻 Starting in "
        t0 = time.time()
        current_time = time.time() - t0
        with tqdm(
            total=round(delay_before_start),
            desc=tqdm_prefix,
            unit="seconds",
            bar_format="{desc}{remaining}",
        ) as pbar:
            while current_time < delay_before_start + 0.01:
                prev_current_time = current_time
                current_time = time.time() - t0
                pbar.update(current_time - prev_current_time)


def beep(config: dict, sound_key: str):
    path = config["path"]
    sound_paths = config["sound_paths"]
    try:
        playsound(f"{path}{sound_paths[sound_key]}")
    except OSError:
        if "debug_mode" in config and config["debug_mode"]:
            raise
        elif "encouragement" not in sound_key:
            print("\a", end="")  # this makes a beep on OSX (who knew??)
