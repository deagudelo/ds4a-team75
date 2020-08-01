import dash_html_components as html

carreta1="When there is a problem over whichever piece of the energy infrastructure in certain place, and it makes a costumer or a group of them do not receive power supply, EPM generates a work order, in which they specify some tasks that a technical crew have to execute over energy infrastructure to fix the problem."
carreta2="In our dashboard, we use the work order as identifier of failure, and we will show you several interactions of the count of failures with another variables the will allow you to understand how the failures are distributed over the region of Urabá and also identify some situations related with their occurrence."



def layout():
    return html.Div(
        className="container",
        children=[
            html.Div(
                className="row justify-content-center text-center  mb-3",
                children=[
                    html.H2("What is the problem we are trying to solve?")
                ]
            ),
            html.Div(
                className="row",
                children=[
                    html.Div(
                        className="col-12 my-2",
                        children=[
                            html.Img(
                                src="https://1-engineer.ru/wp-content/uploads/2018/08/elektroenergetika-pryamoug-2.jpg",
                                width="100%",
                                height="auto"
                            )   
                        ]
                    ),
                    html.Div(
                        className="col-8 mx-auto my-2",
                        children=[
                            html.P(carreta1),
                            html.Br(),
                            html.P(carreta2)
                        ]
                    )
                ]
            )
        ]
    )
