import argparse
import matplotlib.pyplot as plt
import data.datasets as ds


def show_array(args):
    data = ds.get_numpy_array()
    plt.plot(data[:, 0], data[:, 1])
    plt.title('Timeseries line chart')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.show()


def show_dataframe(args):
    df = ds.get_dataframe()
    products = df['Product'].to_list()

    df.plot.bar(stacked=args.stacked)
    plt.title('Product prices and UVP')
    plt.xticks(range(len(products)), products)
    plt.show()


def show_list_data(args):
    headers = ds.get_list_headers()
    data = ds.get_list()

    labels = [d[0] for d in data]
    radii = [d[1] for d in data]

    fig, ax = plt.subplots()
    ax.pie(radii, labels=labels, shadow=args.shadow, startangle=90)
    plt.title(headers[1])
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Matplotlib example plots')
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    array = subparsers.add_parser('array')
    array.set_defaults(func=show_array)

    dataframe = subparsers.add_parser('dataframe')
    dataframe.add_argument('--stacked', type=bool, default=False, action=argparse.BooleanOptionalAction,
                           help='Enable or disable stacking. Default is False.')
    dataframe.set_defaults(func=show_dataframe)

    list_data = subparsers.add_parser('list')
    list_data.add_argument('--shadow', type=bool, default=False, action=argparse.BooleanOptionalAction,
                           help='Enable or disable shadow effect. Default is False.')
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
