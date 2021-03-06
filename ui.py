import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from tabs import sidepanel, tabs, navbar
from database import transforms
from assets import colors


def set_ui(application):
    # Get the data
    df = transforms.df
    dfcenter = transforms.dfcenter
    # Set the layout
    application.layout = html.Div([
        navbar.Navbar(application),
        html.Div(
            className="container-fluid",
            children=[
                html.Div(
                    className='row py-2',
                    children=[
                        html.Div(
                            className="col-xs-4 col-md-2 collapse m-0 p-0 h-100",
                            id="collapseExample",
                            children=[
                                sidepanel.layout
                            ], style={'backgroundColor': '#FFFFFF'}
                        ),
                        html.Div(
                            className='col-xs-8 col-md-10 mx-auto',
                            children=[
                                tabs.layout(application)
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="fab-container",
                    children=[
                        html.Div(
                            className="fab fab-icon-holder",
                            children=[
                                html.A(
                                    **{
                                        'data-toggle': 'collapse',
                                    },
                                    href="#collapseExample",
                                    role="button",
                                    children=[
                                        html.I(
                                            className="fas fa-filter",
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),

            ]
        )

    ])

    @application.callback(
        [
            Output('graph_circuits', 'figure'),
            Output('2graph_time', 'figure'),
            Output('unmapa', 'figure'),
        ],
        [
            Input('techlocation', 'value'),
            Input('townlocation', 'value')
        ])
    def update_figure(tech, townco):
        if (townco is None or townco == []) and (tech is None or tech == []):
            techf = transforms.listaTechLocation
            townf = transforms.listLoc
            dff = df[df['town'].isin(townf)]
            dff = dff[dff['LocationResume'].isin(techf)]

        if (townco is not None and townco != []) and (tech is None or tech == []):
            townf = townco
            techf = transforms.listaTechLocation
            dff = df[df['town'].isin(townf)]
            dff = dff[dff['LocationResume'].isin(techf)]
        if (townco is None or townco == []) and (tech is not None and tech != []):
            techf = tech
            townf = transforms.listLoc
            dff = df[df['town'].isin(townf)]
            dff = dff[dff['LocationResume'].isin(techf)]
        if (townco is not None and townco != []) and (tech is not None and tech != []):
            townf = townco
            techf = tech
            dff = df[df['town'].isin(townf)]
            dff = dff[dff['LocationResume'].isin(techf)]

        return create_g1(dff), create_g2(dff), update_map_center(townf, townco)

    def create_g1(dff):
        #dff= df[df['LocationResume'] == tech]
        dfg = dff.groupby(dff['Circuit'])['NumberOT'].count().reset_index()
        dfg.sort_values(by=['NumberOT'], inplace=True, ascending=False)
        fig = px.bar(dfg, x='Circuit', y='NumberOT',
                     color_discrete_sequence=colors.paleta1)
        fig.update_layout(
            title_text='Total of Work Orders by Circuit', title_x=0.5)

        fig.update_traces(marker_color='darkseagreen')
        fig.update_layout(
            autosize=True,
            width=450,
            height=250,
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=34,
                pad=4
            ),
            paper_bgcolor="white",
        )
        #print('creando g1')
        return fig

    def create_g2(dff):
        #print('creando g2')
        dfg = dff.groupby(['month', 'town'])['NumberOT'].count().reset_index()
        fig2 = px.line(dfg, x="month", y="NumberOT", color='town',
                       color_discrete_sequence=colors.paleta1)  # , color='town'
        fig2.update_layout(
            title_text="Work orders Totals by time", title_x=0.5)
        fig2.update_layout(showlegend=False)
        fig2.update_layout(
            autosize=True,
            width=450,
            height=250,
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=34,
                pad=4
            ),
            paper_bgcolor="white",
        )

        return fig2

    def update_map_center(townf, t):

        dfcenter2 = dfcenter[dfcenter['lugar'] == townf[0]]
        #print('mapa loc')
        # print(dfcenter2.head())
        if (t is None or t == []):
            transforms.fig_mapbox.update_layout(
                mapbox_center={"lat": 8.119863, "lon": -76.58538})
            transforms.fig_mapbox.update_layout(mapbox_zoom=8)
        else:
            transforms.fig_mapbox.update_layout(mapbox_zoom=14)
            transforms.fig_mapbox.update_layout(
                mapbox_center={"lat": dfcenter2.iloc[0, 1], "lon": dfcenter2.iloc[0, 2]})
        return transforms.fig_mapbox
