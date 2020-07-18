import dash
import dash_html_components as html

from tabs import tab1, tab2, tab3

layout = html.Div([
    html.Ul(
        className='nav nav-tabs',
        role='tablist',
        children=[
            html.Li(
                className='nav-item',
                children=[
                    html.A(
                        className='nav-link active',
                        id='eda1-tab',
                        role='tab',
                        href='#eda1',
                        **{
                            'data-toggle': 'tab',
                            'aria-controls': "eda1",
                            'aria-selected': "true"
                        },
                        children=[
                            'Exploratory Data Analysis 1'
                        ]
                    )
                ]
            ),
            html.Li(
                className='nav-item',
                children=[
                    html.A(
                        className='nav-link',
                        id='eda2-tab',
                        role='tab',
                        href='#eda2',
                        **{
                            'data-toggle': 'tab',
                            'aria-controls': "eda2",
                            'aria-selected': "false"
                        },
                        children=[
                            'Exploratory Data Analysis 2'
                        ]
                    )
                ]
            ),
            html.Li(
                className='nav-item',
                children=[
                    html.A(
                        className='nav-link',
                        id='eda3-tab',
                        role='tab',
                        href='#eda3',
                        **{
                            'data-toggle': 'tab',
                            'aria-controls': "eda3",
                            'aria-selected': "false"
                        },
                        children=[
                            'Mapa prioridades por municipio'
                        ]
                    )
                ]
            )
        ]
    ),
    html.Div(
        className='tab-content',
        children=[
            html.Div(
                id='eda1',
                className='tab-pane fade show active',
                children=[
                    tab1.layout
                ],
                role='tabpanel',
                **{
                    'aria-labelledby': "eda1-tab"
                }
            ),
            html.Div(
                id='eda2',
                className='tab-pane fade',
                children=[
                    tab2.layout
                ],
                role='tabpanel',
                **{
                    'aria-labelledby': "eda2-tab"
                }
            ),
            html.Div(
                id='eda3',
                className='tab-pane fade',
                children=[
                    tab3.layout
                ],
                role='tabpanel',
                **{
                    'aria-labelledby': "eda3-tab"
                }
            )
        ]
    )
])
