import argparse
from uniplot import plot
import data.datasets as ds


def show_array(args):
    plot(ys=ds.get_numpy_array()[:, 1],
         title='Timeseries Numpy Array',
         lines=True,
         width=args.width,
         color=args.color,
         interactive=args.interactive)


def show_list_data(args):
    headers = ds.get_list_headers()
    data = ds.get_list()

    labels = [d[0] for d in data]
    xs = [[d[1]] for d in data]
    ys = [[d[2]] for d in data]

    plot(ys=ys,
         xs=xs,
         title='Planet {} vs. {}'.format(headers[1], headers[2]),
         legend_labels=labels,
         lines=False,
         width=args.width,
         color=args.color,
         interactive=args.interactive)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Uniplot example plots')
    parser.add_argument('--width', default=64, help='The width of the plotting region, in characters. Default is 64.')
    parser.add_argument('--color', default=True, help='Enable (default) or disable colors.')
    parser.add_argument('--interactive', default=False, help='Enable or disable (default) interactive mode.')
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    array = subparsers.add_parser('array')
    array.add_argument('--lines', default=True, help='Enable (default) or disable lines between data points.')
    array.set_defaults(func=show_array)

    list_data = subparsers.add_parser('list')
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
