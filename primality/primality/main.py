"""Perform primality testing with both exhaustive and efficient approaches."""

# TODO: Add all of the required imports for the program,
# ensuring that they are in the correct order mandated
# by the industry-standard set by the isort program

# TODO: create a Typer object to support the command-line interface

# TODO: create a Profiler object to support timing program code segments
# TODO: Refer to https://github.com/joerick/pyinstrument to learn more
# about how you need to construct the Profiler object and later use it


class PrimalityTestingApproach(str, Enum):
    """Define the name for the approach for performing primality testing."""

    EXHAUSTIVE = "exhaustive"
    EFFICIENT = "efficient"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # TODO: produce a human-readable value for a bool
    # True --> "Yes"
    # False --> "No"
    # This return value is a placeholder
    return "Yes"


def pretty_print_list(values: Iterable[int]) -> str:
    """Pretty print a list without brackets and adding commas."""
    # TODO: create and return a version of the list without brackets
    # and with commas in between all of the values
    # TODO: This return value is a placeholder; replace it with a correct one
    return ""

def primality_test_exhaustive(number: int) -> Tuple[bool, List[int]]:
    """Perform an exhaustive primality test on the provided integer."""
    # TODO: declare the smallest_divisor with default of None
    # TODO: exhaustively search through all of the values, starting at 2
    # --> if the number is evenly divisible, then it is not prime
    # TODO: if smallest_divisor is no longer None then the function has
    # found a non-prime number with a specific smallest_divisor
    # TODO: if the smallest_divisor is still None then the function has
    # found a prime number and it should return both itself and 1
    # TODO: make sure that the function returns:
    # --> a bool for whether or not the number was prime
    # --> a List[int] for the list with the smallest divisor for the number
    # --> if the number is prime, return the List[int] with both the number and 1
    # TODO: This return value is a placeholder; replace it with a correct one
    return (False, [0,1])


def primality_test_efficient(number: int) -> Tuple[bool, List[int]]:
    """Perform an efficient primality test on the provided integer."""
    smallest_divisor = None
    # TODO: determine first if the number is even and then confirm
    # that it does have a smallest_divisor of 2
    # TODO: if the number is not even, then iteratively perform primality test
    # TODO: use a range function that skips over the even values
    # TODO: make sure that the function returns:
    # --> a bool for whether or not the number was prime
    # --> a List[int] for the list with the smallest divisor for the number
    # --> if the number is prime, return the List[int] with both the number and 1
    # TODO: This return value is a placeholder; replace it with a correct one
    return (False, [0,1])


@cli.command()
def primality(
    number: int = typer.Option(5),
    profile: bool = typer.Option(False),
    approach: PrimalityTestingApproach = PrimalityTestingApproach.EFFICIENT,
) -> None:
    """Use iteration to perform primality testing on a number and run a profiling data collection if requested."""
    # create a console for rich text output
    console = Console()
    # create an empty primality_tuple
    primality_tuple: Tuple[bool, List[int]]
    # TODO: use the efficient primality testing algorithm
    if approach.value == PrimalityTestingApproach.EFFICIENT:
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        # TODO: perform profiling on the execution of the primality test
        # TODO: do not perform profiling
    # TODO: use the exhaustive primality testing algorithm
    elif approach.value == PrimalityTestingApproach.EXHAUSTIVE:
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        # TODO: perform profiling on the execution of the primality test
        # TODO: do not perform profiling
    # display the results of the primality test
    was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    console.print(f":smile: Attempting to determine if {number} is a prime number!")
    console.print()
    console.print(
        f":sparkles: What divisors were found? {pretty_print_list(divisor_list)}"
    )
    console.print(
        f":sparkles: Was this a prime number? {human_readable_boolean(was_prime_found)}"
    )
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profile data from performing primality testing on {number}!"
        )
        profiler.print()
