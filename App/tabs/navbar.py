# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Empresa de servicios públicos de Medellín y Colombia",
        color="#83ac07",
        dark=True,
    )
    return navbar