# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_html_components as html
#from application import application


nav_item = dbc.NavItem(dbc.NavLink(html.H2("DS4A"), href="#"))




#def layout(application):
  #  return
def Navbar(application):
    navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(


                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [   

                        dbc.Col(html.Img(src=application.get_asset_url("Logo_EPM_blanco.png"), height="50px")),
                        dbc.Col(dbc.NavbarBrand(html.H2("Electricity Distribution Failure Model",  style={'color': '#284730'}), className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                #href="",
            ),


            #dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="#83ac07",

    #dark=True,
    #className="mb-5",
    )
    return navbar