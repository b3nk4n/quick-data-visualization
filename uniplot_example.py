import argparse
from uniplot import plot
import data.datasets as ds


def show_array(args):
    print(args)
    plot(ys=ds.get_numpy_array()[:, 1],
         title='Timeseries Numpy Array',
         lines=args.lines,
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
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('--width', type=int, default=64, help='The width of the plotting region, in characters. Default is 64.')
    common_parser.add_argument('--color', type=bool, default=True, action=argparse.BooleanOptionalAction,
                           help='Enable (default) or disable colors.')
    common_parser.add_argument('--interactive', type=bool, default=False, action=argparse.BooleanOptionalAction,
                           help='Enable or disable (default) interactive mode.')

    array = subparsers.add_parser('array', parents=[common_parser])
    array.add_argument('--lines', type=bool, default=True, action=argparse.BooleanOptionalAction,
                       help='Enable (default) or disable lines between data points.')
    array.set_defaults(func=show_array)

    list_data = subparsers.add_parser('list', parents=[common_parser])
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
