import numpy as np
import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class RangeCommand(BaseCommand):
    syntax = Syntax(
        [
            Positional("column", required=True, otl_type=OTLType.TEXT),
            Positional("a", required=True, otl_type=OTLType.NUMBERIC),
            Positional("b", required=True, otl_type=OTLType.NUMBERIC),
            Keyword("step", required=False, otl_type=OTLType.NUMBERIC),
            Keyword("number", required=False, otl_type=OTLType.NUMBERIC),
            Keyword("dtype", required=False, otl_type=OTLType.TEXT)
        ],
    )

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start range command')
        col = self.get_arg("column").value
        a = self.get_arg("a").value
        b = self.get_arg("b").value
        step = self.get_arg("step")
        number = self.get_arg("number")
        dtype = self.get_arg("dtype").value or None

        if df is None:
            df = pd.DataFrame()

        if (step.value is None and number.value is None) or (step.value is not None and number.value is None):
            self.logger.info("Step was provided => using np.arange")
            step = step.value or 1
            df[col] = np.arange(a, b, step, dtype=dtype)
        elif step.value is None and number.value is not None:
            self.logger.info("Number was provided => using np.linspace")
            number = number.value or 10
            df[col] = np.linspace(a, b, num=number)
        else:
            self.logger.error("Both number and step were provided")
            raise ValueError("Cannot handle arguments number and step at the same time")

        return df
