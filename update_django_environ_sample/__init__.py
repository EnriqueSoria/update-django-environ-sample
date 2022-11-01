import sys
from pathlib import Path

import click


def get_env_sample_text(values: dict, write_defaults: bool = False) -> str:
    text = ""
    for env_name, env_config in values.items():
        has_default: bool = isinstance(env_config, tuple) and len(env_config) == 2

        if has_default:
            if write_defaults:
                cast, default_value = env_config
                text += f"{env_name}={default_value}\n"
        else:
            text += f"{env_name}=\n"

    return text


@click.command()
@click.option(
    "--environment_defaults_path",
    "-p",
    default="app/settings/",
    help="Path where environment_defaults.py is located",
    show_default=True,
)
@click.option(
    "--output",
    "-o",
    default="./env.sample",
    help="Path of the sample env file",
    show_default=True,
)
@click.option(
    "--defaults",
    "-d",
    is_flag=True,
    default=False,
    help="Write default values to sample env file",
    show_default=True,
)
def generate_env_sample(*, environment_defaults_path: str, output: str, defaults: bool):
    env_location = Path(environment_defaults_path)
    assert env_location.exists()
    assert (env_location / "environment_defaults.py").exists()

    # Make ENV_DEFAULTS importable
    sys.path.append(str(env_location.absolute()))
    from environment_defaults import ENV_DEFAULTS

    # Write env sample
    text = get_env_sample_text(ENV_DEFAULTS, write_defaults=defaults)
    with open(output, "w") as f:
        f.write(text)


def main():
    generate_env_sample()


if __name__ == "__main__":
    main()
