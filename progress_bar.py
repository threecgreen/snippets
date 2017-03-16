"""
Contains the ProgressBar(object) class used to easily implement a command-line ProgressBar in
command-line interfaces for monitoring the progress of a time-consuming loop.
"""
import sys                              # Used for standard output in ProgressBar class


class ProgressBar(object):
    """
    Create's a command-line progress bar for keeping tabs on the progress of time-consuming loops.

    Args:
        total (int): Total number of iterations to be performed.
        iteration (int): Default 0, starting iteration.
        prefix (str): Default "Progress", the text displayed on the line before the progress bar.
        suffix (str): Default "Complete", the text displayed on the line before the progress bar.
        bar_length (int): Default 20, the length in number of characters of the progress bar.
        style (str): Default "dash", which symbol to use to fill the progress bar. The other option
            is fill, which uses this character: "█".
        show_iter (bool): Default False, whether to specify the exact current iteration of the loop.

    Attributes:
        iteration (int): Current iteration in the loop.
        symbol (str): Symbol used to fill the progress bar. Derived from `style` parameter.
        format_string (str): String used to format the progress bar.
    """
    def __init__(self, total,
                 iteration=0, prefix="Progress", suffix="Complete", bar_length=20,
                 style="dash", show_iter=False):
        self.iteration = iteration
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.bar_length = bar_length
        if style == "fill":
            self.symbol = "█"
        else:
            self.symbol = "#"

        self.show_iter = show_iter
        if self.show_iter:
            self.format_string = "\r{prefix}: {iter} / {total} [{prog_bar}] {percent}% {suffix}"
        else:
            self.format_string = "\r{prefix}: [{prog_bar}] {percent}% {suffix}"

        self._update()
        self._print_bar()

    def next(self):
        """
        Advances the progress bar iteration and updates the progress bar.

        This method should be called at the end of each loop.
        """
        # TODO switch to an __iter__ based implementation for easier use.
        self.iteration += 1
        self._update()
        self._print_bar()

    def _print_bar(self):
        prog_bar = self.symbol * self.fill_length + "-" * (self.bar_length - self.fill_length)
        if self.show_iter:
            sys.stdout.write(self.format_string.format(prefix=self.prefix, iter=self.iteration, total=self.total,
                                                       prog_bar=prog_bar, percent=self.percent, suffix=self.suffix))
        else:
            sys.stdout.write(self.format_string.format(prefix=self.prefix, prog_bar=prog_bar,
                                                       percent=self.percent, suffix=self.suffix))
        if self.iteration == self.total:
            sys.stdout.write('\n')
        sys.stdout.flush()

    def _update(self):
        self.percent = round(100 * (self.iteration / self.total), ndigits=1)
        self.fill_length = int(round(self.bar_length * self.iteration / self.total))
