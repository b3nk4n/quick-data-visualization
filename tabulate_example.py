import argparse
from tabulate import tabulate
import data.datasets as ds


def show_array(args):
    print(tabulate(
        ds.get_numpy_array(),
        tablefmt=args.tablefmt,
        floatfmt=('.0f', '.2f')))


def show_dataframe(args):
    print(tabulate(
        ds.get_dataframe(),
        headers='firstrow',
        tablefmt=args.tablefmt,
        floatfmt=args.floatfmt))


def show_list_data(args):
    print(tabulate(
        ds.get_list(with_headers=True),
        headers='firstrow',
        tablefmt=args.tablefmt,
        floatfmt=args.floatfmt))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tabulate example plots')
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('--tablefmt', type=str, default='fancy_grid',
                               help='The table format, e.g. fancy_grid (default), simple, pipe.')

    array = subparsers.add_parser('array', parents=[common_parser])
    array.set_defaults(func=show_array)

    dataframe = subparsers.add_parser('dataframe', parents=[common_parser])
    dataframe.add_argument('--floatfmt', type=str, default='.2f', help='The number format, e.g. ".2f" (default).')
    dataframe.set_defaults(func=show_dataframe)

    list_data = subparsers.add_parser('list', parents=[common_parser])
    list_data.add_argument('--floatfmt', type=str, default='.2f', help='The number format, e.g. ".2f" (default).')
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
