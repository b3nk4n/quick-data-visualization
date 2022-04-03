import argparse
import plotly.express as px
import data.datasets as ds


def show_array(args):
    data = ds.get_numpy_array()
    fig = px.line(x=data[:, 0], y=data[:, 1], title='Timeseries line chart')
    fig.update_xaxes(title_text='Timestamp')
    fig.update_yaxes(title_text='Value')
    fig.show()


def show_dataframe(args):
    df = ds.get_dataframe()
    fig = px.bar(df[['Price', 'UVP']],
                 title='Product prices and UVP',
                 barmode=('relative' if args.stacked else 'group'))
    fig.show()


def show_list_data(args):
    headers = ds.get_list_headers()
    data = ds.get_list()

    labels = [d[0] for d in data]
    radii = [d[1] for d in data]

    fig = px.pie(names=labels, values=radii, title=headers[1])
    if args.cartoon:
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                          marker=dict(colors=['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'indianred'],
                                      line=dict(color='#000000', width=2)))
    fig.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotly example plots')
    parser.set_defaults(func=lambda args: parser.print_help())
    subparsers = parser.add_subparsers()

    array = subparsers.add_parser('array')
    array.set_defaults(func=show_array)

    dataframe = subparsers.add_parser('dataframe')
    dataframe.add_argument('--stacked', type=bool, default=False, action=argparse.BooleanOptionalAction,
                           help='Enable or disable stacking. Default is False.')
    dataframe.set_defaults(func=show_dataframe)

    list_data = subparsers.add_parser('list')
    list_data.add_argument('--cartoon', type=bool, default=True, action=argparse.BooleanOptionalAction,
                           help='Enable or disable cartoon effect. Default is True.')
    list_data.set_defaults(func=show_list_data)

    arguments = parser.parse_args()
    arguments.func(arguments)
