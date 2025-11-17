# currency.py

def format_conversion_text(date_str, from_currency, to_currency, rate, from_amount):
    """
    Formats output in the exact required convention:

    The conversion rate on <date> from <from> to <to> was <rate>.
    So <from amount> in <from> correspond to <to amount> in <to>
    The inverse rate was <inverse rate>.
    """
    to_amount = from_amount * rate
    inverse_rate = 1 / rate if rate else 0

    return (
        f"The conversion rate on {date_str} from {from_currency} to {to_currency} was {rate}. "
        f"So {from_amount} in {from_currency} correspond to {to_amount} in {to_currency} "
        f"The inverse rate was {inverse_rate}."
    )
