import argparse
import plotext as plt
import data.datasets as ds


def show_array(_):
    data = ds.get_numpy_array()
    plt.plot(data[:, 0], data[:, 1])
    plt.title('Timeseries line chart')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.show()


def show_dataframe(_):
    df = ds.get_dataframe()
    product_list = df['Product'].to_list()
    price_list = df['Price'].to_list()
    uvp_list = df['UVP'].to_list()

    plt.multiple_bar(product_list, [price_list, uvp_list], label=df.columns.to_list()[1:])
    plt.title('Product prices and UVP')
    plt.show()


def show_list_data(args):
    headers = ds.get_list_headers()
    data = ds.get_list()

    labels = [d[0] for d in data]
    radii = [d[1] for d in data]

    plt.bar(labels, radii, orientation=args.orientation)
    plt.title(headers[1])
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotext example plots')
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    array = subparsers.add_parser('array')
    array.set_defaults(func=show_array)

    dataframe = subparsers.add_parser('dataframe')
    dataframe.add_argument('--stacked', type=bool, default=False, action=argparse.BooleanOptionalAction,
                           help='Enable or disable stacking. Default is False.')
    dataframe.set_defaults(func=show_dataframe)

    list_data = subparsers.add_parser('list')
    list_data.add_argument('--orientation', type=str, default='v',
                           help='The orientation of the plot, such as "horizontal"/"h" or "vertical"/"v". Default is "v".')
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
