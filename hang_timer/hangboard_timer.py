import sys
import time

import fire
from colorama import Fore, Style

from hang_timer.utils import beep_and_wait, load_config, welcome_message


def time_hangboard_sesh(
    n_sets: int = 18,
    delay_before_start: float = 20,
    time_on: float = 7,
    rest_time: float = 3,
    encouragement_set: int = 100,
    config_path: str = "config.yml",
):
    """Timing for a hangboard sessión

    See README.md for instructions.

    Parameters
    ----------
    n_sets : int
        number of total sets
    delay_before_start : float
        time delay before start (seconds)
    time_on : float
        time for set (seconds)
    rest_time : float
        time between sets (seconds)
    encouragement_set : int
        pick a set to get some extra encouragement!
    config_path : str
        path to config
    """
    config = load_config(config_path)["config"]
    welcome_message(delay_before_start)
    for n_completed in range(1, n_sets + 1):

        beep_and_wait(
            config=config,
            tqdm_prefix=Fore.GREEN + "🦄 START!" + Style.RESET_ALL,
            sound_key="start",
            wait_secs=time_on,
            encouragement=(n_completed == (encouragement_set) and time_on > 5.1),
        )

        beep_and_wait(
            config=config,
            tqdm_prefix=Fore.RED + "🛑 STOP!" + Style.RESET_ALL,
            sound_key="stop",
            wait_secs=rest_time,
        )
        print(f"{n_completed}/{n_sets} set(s) completed!\n")

    beep_and_wait(
        config=config,
        tqdm_prefix=Fore.RED + "All Done!" + Style.RESET_ALL,
        sound_key="done",
        wait_secs=0,
    )


def sesh():
    fire.Fire((time_hangboard_sesh))
