import dash_html_components as html
from tabs import tab_maps, tab_performance, tab_us, tab_context


def layout(application):
    return html.Div([
        html.Ul(
            className='nav nav-pills my-3 justify-content-center',
            id="pills-tab",
            role='tablist',
            children=[
                html.Li(
                    className='nav-item',
                    children=[
                        html.A(
                            className='nav-link active',
                            id='performance-tab',
                            role='tab',
                            href='#performance',
                            **{
                                'data-toggle': 'pill',
                                'aria-controls': "performance",
                                'aria-selected': "true"
                            },
                            children=[
                                'Performance indicators'
                            ]
                        )
                    ]
                ),
                html.Li(
                    className='nav-item',
                    children=[
                        html.A(
                            className='nav-link',
                            id='maps-tab',
                            role='tab',
                            href='#maps',
                            **{
                                'data-toggle': 'pill',
                                'aria-controls': "maps",
                                'aria-selected': "false"
                            },
                            children=[
                                'GeoData by town'
                            ]
                        )
                    ]
                ),
                html.Li(
                    className='nav-item',
                    children=[
                        html.A(
                            className='nav-link',
                            id='context-tab',
                            role='tab',
                            href='#context',
                            **{
                                'data-toggle': 'pill',
                                'aria-controls': "context",
                                'aria-selected': "false"
                            },
                            children=[
                                'Context'
                            ]
                        )
                    ]
                ),
                html.Li(
                    className='nav-item',
                    children=[
                        html.A(
                            className='nav-link',
                            id='us-tab',
                            role='tab',
                            href='#us',
                            **{
                                'data-toggle': 'pill',
                                'aria-controls': "us",
                                'aria-selected': "false"
                            },
                            children=[
                                'About Us'
                            ]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className='tab-content',
            id="pills-tabContent",
            children=[
                html.Div(
                    id='performance',
                    className='tab-pane fade show active',
                    children=[
                        tab_performance.layout
                    ],
                    role='tabpanel',
                    **{
                        'aria-labelledby': "performance-tab"
                    }
                ),
                html.Div(
                    id='maps',
                    className='tab-pane fade',
                    children=[
                        tab_maps.layout(application)
                    ],
                    role='tabpanel',
                    **{
                        'aria-labelledby': "maps-tab"
                    }
                ),
                html.Div(
                    id='context',
                    className='tab-pane fade p-2',
                    children=[
                        tab_context.layout()
                    ],
                    role='tabpanel',
                    **{
                        'aria-labelledby': "context-tab"
                    }
                ),
                html.Div(
                    id='us',
                    className='tab-pane fade p-2',
                    children=[
                        tab_us.layout()
                    ],
                    role='tabpanel',
                    **{
                        'aria-labelledby': "us-tab"
                    }
                )
            ]
        )
    ])
