from tealprint import TealConfig, TealLevel

_app_name = "mcman-index"


class Config:
    def __init__(self):
        # Default values
        self.app_name: str = _app_name
        TealConfig.level = TealLevel.info

    def set_from_cli(self, args):
        """Set additional configuration from script arguments

        Args:
            args (list): All the parsed arguments
        """
        if args.debug:
            TealConfig.level = TealLevel.debug
        elif args.verbose:
            TealConfig.level = TealLevel.verbose


config = Config()
