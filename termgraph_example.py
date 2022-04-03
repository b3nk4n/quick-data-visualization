import argparse
from termgraph import termgraph
import data.datasets as ds


def show_dataframe(args):
    df = ds.get_dataframe()
    labels = df['Product'].to_list()

    prices = df['Price'].to_list()
    discount = [uvp - prices[i] for i, uvp in enumerate(df['UVP'].to_list())]
    values = list(zip(prices, discount))

    termgraph.chart(
        colors=[94, 92],
        data=values,
        args=_tg_args(args.width, stacked=True),
        labels=labels
    )


def show_list_data(args):
    data = ds.get_list()
    labels = [d[0] for d in data]
    values = [[d[1]] for d in data]

    termgraph.chart(
        colors=[94],
        data=values,
        args=_tg_args(args.width),
        labels=labels
    )


def _tg_args(width, stacked=False):
    return {
        "stacked": stacked,
        "width": width,
        "no_labels": False,
        "format": "{:<5.2f}",
        "suffix": "",
        "vertical": False,
        "histogram": False,
        "no_values": False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Termgraph example plots')
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('--width', type=int, default=64,
                               help='The width of the plotting region, in characters. Default is 64.')

    dataframe = subparsers.add_parser('dataframe', parents=[common_parser])
    dataframe.set_defaults(func=show_dataframe)

    list_data = subparsers.add_parser('list', parents=[common_parser])
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
