import dash
import dash_html_components as html
from tabs import tab_maps, tab_performance, tab_us


def layout(application):
    return html.Div([
        html.Ul(
            className='nav nav-tabs',
            role='tablist',
            children=[
                html.Li(
                    className='nav-item',
                    children=[
                        html.A(
                            className='nav-link active',
                            id='maps-tab',
                            role='tab',
                            href='#maps',
                            **{
                                'data-toggle': 'tab',
                                'aria-controls': "maps",
                                'aria-selected': "true"
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
                            id='performance-tab',
                            role='tab',
                            href='#performance',
                            **{
                                'data-toggle': 'tab',
                                'aria-controls': "performance",
                                'aria-selected': "false"
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
                            id='us-tab',
                            role='tab',
                            href='#us',
                            **{
                                'data-toggle': 'tab',
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
            children=[
                html.Div(
                    id='maps',
                    className='tab-pane fade show active',
                    children=[
                        tab_maps.layout(application)
                    ],
                    role='tabpanel',
                    **{
                        'aria-labelledby': "maps-tab"
                    }
                ),
                html.Div(
                    id='performance',
                    className='tab-pane fade',
                    children=[
                        tab_performance.layout
                    ],
                    role='tabpanel',
                    **{
                        'aria-labelledby': "performance-tab"
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
