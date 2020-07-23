from setuptools import setup

setup(
    name="hang_timer",
    version="0.0",
    author_email="samuelryan18@gmail.com",
    packages=["hang_timer"],
    python_requires=">=3.4",
    install_requires=["colorama", "fire", "playsound", "pyobjc", "tqdm", "pyyaml",],
    entry_points={"console_scripts": ["sesh = hang_timer.hangboard_timer:sesh"]},
)
