import argparse
import math

parser = argparse.ArgumentParser(description="Loan calculator!")
parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

find_payment = {args.periods, args.principal, args.interest}
find_principal = {args.periods, args.payment, args.interest}
find_months = {args.principal, args.payment, args.interest}


def calculate_diff_payment(principal, periods, interest):
    i = interest / 12 / 100
    total = 0
    for j in range(1, periods + 1, 1):
        payment = math.ceil(principal / periods + i * (principal - principal * (j - 1) / periods))
        total += payment
        print(f'Month {j}: payment is {payment}')
    overpayment = total - principal
    print('', f'Overpayment = {overpayment}', sep='\n')


def calculate_loan_principal(periods, payment, interest):
    i = interest / 12 / 100
    principal = (math.ceil(payment
                           / ((i * math.pow(1 + i, periods))
                              / (math.pow(1 + i, periods)
                                 - 1))))

    overpayment = periods * payment - principal
    print(f'Your loan principal = {principal}!',
          f'Overpayment = {overpayment}', sep='\n')


def calculate_payments_number(principal, payment, interest):
    i = interest / 12 / 100
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))

    text_output = ''
    if n == 1:
        text_output = "It will take {} month to repay this loan!".format(n)
    elif n < 12:
        text_output = "It will take {} months to repay this loan!".format(n)
    elif n >= 12:
        if n == 12:
            text_output = "It will take {} year to repay this loan!".format(n // 12)
        elif n % 12 == 0:
            text_output = "It will take {} years to repay this loan!".format(n // 12)
        elif n % 12 == 1:
            text_output = "It will take {} years and {} month to repay this loan!".format(n // 12, n % 12)
        else:
            text_output = "It will take {} years and {} months to repay this loan!".format(n // 12, n % 12)
    overpayment = n * payment - principal
    print(text_output, f'Overpayment = {overpayment}', sep='\n')


def calculate_monthly_payment(principal, periods, interest):
    i = interest / 12 / 100
    ordinary_annuity = (math.ceil((principal
                                   * i
                                   * math.pow(1 + i, periods))
                                  / (math.pow(1 + i, periods) - 1)))
    overpayment = ordinary_annuity * periods - principal
    print(f'Your annuity payment = {ordinary_annuity}!',
          f'Overpayment = {overpayment}', sep='\n')


if args.type is None or args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")
elif args.type == "diff":
    if (len(vars(args)) == 5
            and args.payment is None
            and args.principal > 0
            and args.periods > 0
            and args.interest > 0):
        calculate_diff_payment(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")
elif args.type == "annuity" and args.interest is not None:
    if all(find_principal) is not None and all(find_principal) > 0:
        calculate_loan_principal(args.periods, args.payment, args.interest)
    elif all(find_months) is not None and all(find_months) > 0:
        calculate_payments_number(args.principal, args.payment, args.interest)
    elif all(find_payment) is not None and all(find_payment) > 0:
        calculate_monthly_payment(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
